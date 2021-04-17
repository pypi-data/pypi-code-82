from networkdisk.sql.dialect import sqldialect as dialect
from networkdisk.tupledict.rekey_functions import SortFirstTwo
dialect = dialect.provide_submodule("schemata")

## Defining default undirected graph schema
@dialect.register(True)
def ungraph(dialect, symmode='auto', index=True, readonly=False, table_suffix="", **columns):
	"""Generates a GraphSchema.

	Returns a valid, sqlite-optimized GraphSchema, that uses five tables and
	one view, as described in Notes, below.

	Parameters
	----------
	dialect : Dialect
		The SQL dialect to use.

	columns : dictable, default=()
		Mapping to be passed to `dialect.graph_schema.setup_graph_columns`
		function as keyworded parameters.  Accepted keys are `'node'`,
		`'datakey'`, `'datavalue'`, and the two former ones prefixed by one of
		`'node_'`, `'edge_'`, or `'graph_'`.  Accepted values are `None` (same
		as missing key), string (the SQL type to use, e.g., `'INT'`, `'TEXT'`,
		`'JSON'`), or type/encoder pairs whose first coordinate is required to
		be a string, and whose second coordinate might be a string or `None`.

	symmode : 'auto' or None or bool, default=None
		Symmode variant of the generated `ndsqlite.GraphSchema`.  The value
		`None` and `'auto'`, which are equivalent, and indicate that the
		`ReadWriteTupleDictSchema` for asymmetric edges is given to the schema
		constructor.  By contrasts, it is not given with a Boolean value.  If
		 `True`, triggers for INSERTing/DELETing edges from the asymmmetric
		 VIEW `asymedges` are defined.  If `False`, no triggers are created.

	index : bool, default=True
		Whether to add useful INDEX to the schema.

	readonly : bool, default=False
		Whether the generated schema is read only.

	table_suffix : str, default=''
		A suffix to append to each SQL TABLE and VIEW name.

	Notes
	-----
	+	TABLE nodes
		stores the vertex ids in its single column 'name' of type
		`node_type`, which is a PRIMARY KEY.
	+	TABLE node_data
		stores in two columns 'key' and 'value' the data of each
		vertex. The table has a third column 'name' which references
		the column 'name' of TABLE 'nodes'. The pair ('name', 'key')
		has the UNIQUE constraint. The 'key' column is indexed.
	+	TABLE edges
		stores the asymmetric edges in two columns, named 'source'
		and 'target' respectively, which are both references to the
		column 'name' of the TABLE 'nodes'. Each pair ('source',
		'target') is UNIQUE, with 'source' being less than or equal
		to 'target'. There is a third column 'id' that stores an
		AUTOINCREMENTed integer id for the edge. There is a reversed
		index on pairs ('target', 'source').
	+	TABLE edge_data
		stores the edge data in two columns 'key' and 'value'. The
		third column 'id' references the column 'id' of TABLE
		'nodes'. The pair ('id', 'key') is UNIQUE. The 'key' column
		is indexed.
	+	VIEW symedges
		view on the rows ('id', 'source', 'target') and ('id',
		'target', 'source') from TABLE 'edges'. The view supports
		INSERTion and DELETion via triggers, that propagate the
		corresponding alteration on the TABLE edges.
	+	TABLE graph_info
		stores the graph data in two columns 'key' and 'value'. The
		column 'key' is a PRIMARY KEY for the table, and the column
		'value' does not accept the NULL value.
	"""
	columns = dialect.graph_schema.setup_graph_columns(**columns)
	table_suffix = str(table_suffix)
	trace = dict(method="ungraph", columns=columns, table_suffix=table_suffix, symmode=symmode, readonly=readonly, index=index)

	schema = dialect.schema.Schema("ungraphs")
	#NODES
	nodesT = schema.add_table("nodes"+table_suffix)
	sqltype, encoder = columns['node']
	nnamC = nodesT.add_column("name", sqltype=sqltype, encoder=encoder, primarykey="IGNORE", notnull="IGNORE")
	#NODE DATA
	nodeDataT = schema.add_table("node_data"+table_suffix)
	consfk = dialect.constraints.ForeignkeyConstraint(
		nnamC, container=nodesT, on_delete="CASCADE", on_update="CASCADE", deferrable=True, initially_deferred=True)
	nfidC = nodeDataT.add_column("name", references=nnamC, notnull="IGNORE", constraints=(consfk,))
	sqltype, encoder = columns['node_datakey']
	nkeyC = nodeDataT.add_column("key", sqltype=sqltype, encoder=encoder, notnull="IGNORE")
	sqltype, encoder = columns['node_datavalue']
	nvalC = nodeDataT.add_column("value", sqltype=sqltype, encoder=encoder, notnull=True)
	nodeDataT.add_constraint(dialect.constraints.TableUniqueConstraint(nfidC, nkeyC, on_conflict="REPLACE"))
	if index:
		schema.add_index(nodeDataT, columns=(nkeyC,nvalC))
	#EDGES
	edgesT = schema.add_table("edges"+table_suffix)
	eidC = edgesT.add_column("id", sqltype="INTEGER", primarykey=True, autoincrement=True, notnull=True)
	esrcC = edgesT.add_column("source", sqltype=nnamC, references=nnamC, constraints=(consfk,), notnull=True)
	etrgtC = edgesT.add_column("target", sqltype=nnamC, references=nnamC, constraints=(consfk,), notnull="IGNORE")
	edgesT.add_constraint(dialect.constraints.TableUniqueConstraint(esrcC, etrgtC, on_conflict="IGNORE"))
	if symmode is not False:
		edgesT.add_constraint(dialect.constraints.CheckConstraint(esrcC.le(etrgtC)))
	if index:
		schema.add_index(edgesT, columns=(etrgtC, esrcC))
	#EDGE DATA
	edgeDataT = schema.add_table("edge_data"+table_suffix)
	efidC = edgeDataT.add_column("id", references=eidC, on_delete="CASCADE", on_update="CASCADE", notnull=True)
	sqltype, encoder = columns['edge_datakey']
	ekeyC = edgeDataT.add_column("key", sqltype=sqltype, encoder=encoder, notnull=True)
	sqltype, encoder = columns['edge_datavalue']
	evalC = edgeDataT.add_column("value", sqltype=sqltype, encoder=encoder, notnull=True)
	edgeDataT.add_constraint(dialect.constraints.TableUniqueConstraint(efidC, ekeyC, on_conflict="REPLACE"))
	if index:
		schema.add_index(edgeDataT, columns=(ekeyC,evalC))
	#SYMMETRIC EDGES
	if symmode is False:
		symedgesV = edgesT
	else:
		vdefq = dialect.queries.UnionQuery(
			edgesT.select_query(columns=(eidC, esrcC, etrgtC)),
			edgesT.select_query(columns=(eidC, etrgtC, esrcC))
		)
		symedgesV = schema.add_view("symedges"+table_suffix, defquery=vdefq)

		if symmode: #and not readonly:
			newSRC = dialect.columns.TriggerNewColumn(symedgesV[1])
			newTRGT = dialect.columns.TriggerNewColumn(symedgesV[2])
			iNodeQ = nodesT.insert_values((newSRC,), (newTRGT,), columns=(nnamC,))
			minNew = dialect.columns.TransformColumn("min", newSRC, newTRGT)
			maxNew = dialect.columns.TransformColumn("max", newSRC, newTRGT)
			coalescol = dialect.columns.TransformColumn("coalesce", newSRC, newTRGT)
			iEdgeQ = edgesT.insert_values((minNew.ifnull(coalescol), maxNew), columns=(esrcC, etrgtC))
			schema.add_trigger(symedgesV, "INSTEAD OF", "INSERT", iNodeQ, iEdgeQ)

			oldSRC = dialect.columns.TriggerOldColumn(symedgesV[1])
			oldTRGT = dialect.columns.TriggerOldColumn(symedgesV[2])
			minOld = dialect.columns.TransformColumn("min", oldSRC, oldTRGT)
			maxOld = dialect.columns.TransformColumn("max", oldSRC, oldTRGT)
			dEdgeQ = edgesT.delete_query(condition=esrcC.eq(minOld) & etrgtC.eq(maxOld))
			schema.add_trigger(symedgesV, "INSTEAD OF", "DELETE", dEdgeQ)
	#GRAPH DATA
	graphT = schema.add_table("graph_info"+table_suffix)
	sqltype, encoder = columns['graph_datakey']
	gkeyC = graphT.add_column("key", sqltype=sqltype, encoder=encoder, primarykey="REPLACE", notnull=True)
	sqltype, encoder = columns['graph_datavalue']
	gvalC = graphT.add_column("value", sqltype=sqltype, encoder=encoder, notnull=True)
	if index:
		schema.add_index(graphT, columns=(gkeyC,gvalC))
	#TUPLEDICTSCHEMA
	if readonly:
		TupleDictSchema = dialect.tupledict.ReadOnlyTupleDictSchema
	else:
		TupleDictSchema = dialect.tupledict.ReadWriteTupleDictSchema
	nodesTDS = TupleDictSchema(nodesT, nodeDataT, columns=(nnamC, nkeyC, nvalC), joinpairs=[(nnamC, nfidC)])
	if symmode is not None or readonly:
		edgesTDS = TupleDictSchema(
			symedgesV, edgeDataT,
			columns=[symedgesV[esrcC.name], symedgesV[etrgtC.name], ekeyC, evalC],
			joinpairs=[(symedgesV[eidC.name], efidC)]
		)
	#GRAPHSCHEMA
	graphTDS = TupleDictSchema(graphT, columns=[gkeyC, gvalC])
	if symmode in [True, False]:
		gS = dialect.graph_schema.GraphSchema(nodesTDS, edgesTDS, graphTDS, symmode=symmode, schema=schema)
	else:
		asymedgesTDS = TupleDictSchema(
			edgesT, edgeDataT,
			columns=(esrcC, etrgtC, ekeyC, evalC),
			joinpairs=[(eidC, efidC)],
			rekey=SortFirstTwo())
		if symmode is None and not readonly:
			edgesTDS = TupleDictSchema(
				symedgesV, edgeDataT,
				columns=[symedgesV[esrcC.name], symedgesV[etrgtC.name], ekeyC, evalC],
				joinpairs=[(symedgesV[eidC.name], efidC)],
				write_target=asymedgesTDS
			)
		gS = dialect.graph_schema.GraphSchema(nodesTDS, edgesTDS, graphTDS, asymedgesTDS, schema=schema, schema_trace=trace)
	return gS

@dialect.register(True)
def ungraph_unsplitted(dialect, table_suffix="", symmode='auto', readonly=False, index=True, **columns):
	"""Generates a GraphSchema.

	Returns a valid, sqlite-optimized GraphSchema, that uses three tables and
	one view.

	Parameters
	----------
	dialect : Dialect
		The SQL dialect to use.

	columns : dictable, default=()
		Mapping to be passed to `dialect.graph_schema.setup_graph_columns`
		function as keyworded parameters.  Accepted keys are `'node'`,
		`'datakey'`, `'datavalue'`, and the two former ones prefixed by one of
		`'node_'`, `'edge_'`, or `'graph_'`.  Accepted values are `None` (same
		as missing key), string (the SQL type to use, e.g., `'INT'`, `'TEXT'`,
		`'JSON'`), or type/encoder pairs whose first coordinate is required to
		be a string, and whose second coordinate might be a string or `None`.

	symmode : 'auto' or None or bool, default=None
		Symmode variant of the generated `ndsqlite.GraphSchema`.  The value
		`None` and `'auto'`, which are equivalent, and indicate that the
		`ReadWriteTupleDictSchema` for asymmetric edges is given to the schema
		constructor.  By contrasts, it is not given with a Boolean value.  If
		 `True`, triggers for INSERTing/DELETing edges from the asymmmetric
		 VIEW `asymedges` are defined.  If `False`, no triggers are created.

	index : bool, default=True
		Whether to add useful INDEX to the schema.

	readonly : bool, default=False
		Whether the generated schema is read only.

	table_suffix : str, default=''
		A suffix to append to each SQL TABLE and VIEW name.
	"""
	columns = dialect.graph_schema.setup_graph_columns(**columns)
	table_suffix = str(table_suffix)
	trace = dict(method="ungraph_unsplitted", columns=columns, table_suffix=table_suffix, symmode=symmode, readonly=readonly, index=index)

	schema = dialect.schema.Schema("ungraphs")
	#NODES
	nodesT = schema.add_table("nodes"+table_suffix)
	sqltype, encoder = columns['node']
	nnamC = nodesT.add_column("name", sqltype=sqltype, encoder=encoder)
	sqltype, encoder = columns['node_datakey']
	nkeyC = nodesT.add_column("key", sqltype=sqltype, encoder=encoder)
	sqltype, encoder = columns['node_datavalue']
	nvalC = nodesT.add_column("value", sqltype=sqltype, encoder=encoder)
	if index:
		schema.add_index(nodesT, columns=(nnamC,))
		schema.add_index(nodesT, columns=(nkeyC, nvalC))
	#EDGES
	edgesT = schema.add_table("edges"+table_suffix)
	esrcC = edgesT.add_column("source", sqltype=sqltype, encoder=encoder)
	etrgtC = edgesT.add_column("target", sqltype=sqltype, encoder=encoder)
	sqltype, encoder = columns['edge_datakey']
	ekeyC = edgesT.add_column("key", sqltype=sqltype, encoder=encoder)
	sqltype, encoder = columns['edge_datavalue']
	evalC = edgesT.add_column("value", sqltype=sqltype, encoder=encoder)
	if index:
		schema.add_index(edgesT, columns=(esrcC, etrgtC))
		schema.add_index(edgesT, columns=(etrgtC, esrcC))
		schema.add_index(edgesT, columns=(ekeyC, evalC))
	#SYMMETRIC EDGES
	vdefq = dialect.queries.UnionQuery(
		edgesT.select_query(columns=(esrcC, etrgtC, ekeyC, evalC)),
		edgesT.select_query(columns=(etrgtC, esrcC, ekeyC, evalC))
	)
	symedgesV = schema.add_view("symedges"+table_suffix, defquery=vdefq)

	if symmode: #and not readonly:
		newSRC = dialect.columns.TriggerNewColumn(symedgesV[0])
		newTRGT = dialect.columns.TriggerNewColumn(symedgesV[1])
		iNodeQ = nodesT.insert_values((newSRC,), (newTRGT,), columns=(nnamC,))
		minNew = dialect.columns.TransformColumn("min", newSRC, newTRGT)
		maxNew = dialect.columns.TransformColumn("max", newSRC, newTRGT)
		iEdgeQ = edgesT.insert_values((minNew, maxNew), columns=(esrcC, etrgtC))
		schema.add_trigger(symedgesV, "INSTEAD OF", "INSERT", iNodeQ, iEdgeQ)

		oldSRC = dialect.columns.TriggerOldColumn(symedgesV[0])
		oldTRGT = dialect.columns.TriggerOldColumn(symedgesV[1])
		minOld = dialect.columns.TransformColumn("min", oldSRC, oldTRGT)
		maxOld = dialect.columns.TransformColumn("max", oldSRC, oldTRGT)
		dEdgeQ = edgesT.delete_query(condition=esrcC.eq(minOld) & etrgtC.eq(maxOld))
		schema.add_trigger(symedgesV, "INSTEAD OF", "DELETE", dEdgeQ)
	#GRAPH DATA
	graphT = schema.add_table("graph_info"+table_suffix)
	sqltype, encoder = columns['graph_datakey']
	gkeyC = graphT.add_column("key", sqltype=sqltype, encoder=encoder)
	sqltype, encoder = columns['graph_datavalue']
	gvalC = graphT.add_column("value", sqltype=sqltype, encoder=encoder)
	if index:
		schema.add_index(graphT, columns=(gkeyC,gvalC))
	#TUPLEDICTSCHEMA
	if readonly:
		TupleDictSchema = dialect.tupledict.ReadOnlyTupleDictSchema
	else:
		TupleDictSchema = dialect.tupledict.ReadWriteTupleDictSchema
	nodesTDS = TupleDictSchema(nodesT, columns=(nnamC, nkeyC, nvalC))
	edgesTDS = TupleDictSchema(symedgesV, columns=tuple(range(4)))
	asymedgesTDS = TupleDictSchema(edgesT, columns=(esrcC, etrgtC, ekeyC, evalC), rekey=SortFirstTwo())
	graphTDS = TupleDictSchema(graphT, columns=[gkeyC, gvalC])
	#GRAPHSCHEMA
	if symmode in [True, False]:
		gS = dialect.graph_schema.GraphSchema(nodesTDS, edgesTDS, graphTDS, symmode=symmode, schema=schema, schema_trace=trace)
	else:
		gS = dialect.graph_schema.GraphSchema(nodesTDS, edgesTDS, graphTDS, asymedgesTDS, schema=schema, schema_trace=trace)
	return gS

methods = dict(ungraph=dialect.ungraph, ungraph_unsplitted=dialect.ungraph_unsplitted)
dialect.register(methods, name="ungraph_methods")

@dialect.register(True)
def load_ungraph(dialect, **state):
	method = state.pop("method", "ungraph")
	methods = dialect.schemata
	if method in methods:
		method = methods[method]
		columns = state.pop("columns", {})
		return method(**state, **columns)
	elif method is not None:
		raise ValueError(f"Unknown ungraph schema generator method {method}")
	raise ValueError(f"Unknown ungraph schema dump {state}")

#TODO: def ungraph_splitted
