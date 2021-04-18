# AUTOGENERATED! DO NOT EDIT! File to edit: update.ipynb (unless otherwise specified).

__all__ = ['Updater']

# Cell
import pandas as pd
from datetime import datetime
import pickle, json , boto3, zlib, os, logging, traceback

# Cell
try:
#   INVENTORY_BUCKET_NAME = os.environ['INVENTORY_BUCKET_NAME']
  INPUT_BUCKET_NAME = os.environ['INPUT_BUCKET_NAME']
except Exception as e:
  print(f'missing environment variable {e} in update NB')
#   INVENTORY_BUCKET_NAME = None
  INPUT_BUCKET_NAME = None

# Cell
class Updater:
  @classmethod
  def valueUpdate(cls, input):
    '''
    update products in the database, first use the helper.groupbyprcode to treat the data
    input structure is the foloowing
    - iprcode:
        ibrcode:
          ib_cf_qty: Int
          lastUpdate: Float
          new_ib_bs_stock_cv: Int
    '''
    itemsUpdated = {'success':0, 'failure': 0, 'failureMessage':[]}

    logging.info(f'there are {len(list(input.keys()))} products to update')

    # loop through each product
    for prcode, value in input.items():

      incumbentBr = None
      # check if product is in the database, if not, create an empty class with the product code
      incumbentBr = next(cls.query(prcode),cls(ib_prcode = prcode, inventory = {}))
      logging.info(f'incumbentBr is {incumbentBr}\n, prcode is {prcode}')

      # drop the data with no update
      filteredBr = {
          brcode : v2
          for brcode, v2 in value.items()
          if v2['ib_cf_qty'] != incumbentBr.inventory.get(brcode ,{}).get('ib_cf_qty',None)
      }
      logging.info(f'filteredBr is {filteredBr}')


      # check if there are data to update
      if filteredBr:
        # put the latest update into the lastupdate index
        incumbentBr.lastUpdate = max( v.get('lastUpdate') for v in filteredBr.values() )
        incumbentBr.inventory = (lambda d: d.update(filteredBr) or d)(incumbentBr.inventory)
        incumbentBr.inventory['lastUpdate'] = incumbentBr.lastUpdate
        incumbentBr.inventory['ib_prcode'] = incumbentBr.ib_prcode
        incumbentBr.needUpdate = cls.TRUE

        logging.info(f'saving result {incumbentBr}')
        # try to save the result
        saveResult = incumbentBr.save()
        # saveResult = batch.save(incumbentBr)

        # record the saving success
        if saveResult.get('ConsumedCapacity'):
          itemsUpdated['success'] += 1
        else:
          itemsUpdated['failure'] += 1
          itemsUpdated['failureMessage'].append(saveResult)

    return itemsUpdated

  @classmethod
  def bulkUpdate(cls,input, **kwargs):
    '''
    update products in the database, first use the helper.groupbyprcode to treat the data
    input structure is the foloowing
    - iprcode:
        ibrcode:
          ib_cf_qty: Int
          lastUpdate: Float
          new_ib_bs_stock_cv: Int
    '''
    itemsUpdated = {'success':0, 'failure': 0, 'failureMessage':[]}

    logging.info(f'there are {len(list(input.keys()))} products to update')

    db = cls.loadFromS3(**kwargs)

    with cls.batch_write() as batch:
      # loop through each product
      for prcode, value in input.items():

        incumbentBr = None
        # check if product is in the database, if not, create an empty class with the product code
  #       incumbentBr = next(cls.query(prcode),cls(ib_prcode = prcode, inventory = {}))
        # do this with s3 database instead of dynamodb to speed up
        incumbentBr = cls(inventory = db.get(prcode) or {}, ib_prcode = prcode)
        logging.info(f'incumbentBr is {incumbentBr}\n, prcode is {prcode}')

        # drop the data with no update
        filteredBr = {
            brcode : v2
            for brcode, v2 in value.items()
            if v2['ib_cf_qty'] != incumbentBr.inventory.get(brcode ,{}).get('ib_cf_qty',None)
        }
        logging.info(f'filteredBr is {filteredBr}')


        # check if there are data to update
        if filteredBr:
          # put the latest update into the lastupdate index
          incumbentBr.lastUpdate = max( v.get('lastUpdate') for v in filteredBr.values() )
          incumbentBr.inventory = (lambda d: d.update(filteredBr) or d)(incumbentBr.inventory)
          incumbentBr.inventory['lastUpdate'] = incumbentBr.lastUpdate
          incumbentBr.inventory['ib_prcode'] = incumbentBr.ib_prcode
          incumbentBr.needUpdate = cls.TRUE

          logging.info(f'saving result {incumbentBr}')
          # try to save the result
#           saveResult = incumbentBr.save()
          try:
            saveResult = batch.save(incumbentBr)
            itemsUpdated['success'] += 1
          except:
            itemsUpdated['failure'] += 1
            itemsUpdated['failureMessage'].append(traceback.format_exc())
    return itemsUpdated



  @classmethod
  def updateLambdaInput(cls, input):
    '''
    update products in the database by first grouping the data from lambda
    input
    - ib_prcode: String
      ib_brcode: String
      ib_cf_qty: Int
      new_ib_bs_stock: int
    '''
    groupedInput = cls.Helper.groupByProduct(input)
    return cls.valueUpdate(groupedInput)

  @classmethod
  def updateS3Input(cls, inputBucketName = INPUT_BUCKET_NAME, key = '', **kwargs):
    s3Result = cls.loadFromS3(bucketName= inputBucketName, key = key, **kwargs)
    transformedS3Result = [{
        'ib_prcode': item.get('ib_prcode') or item.get('prcode'),
        'ib_brcode': item.get('ib_brcode') or item.get('brcode'),
        'ib_cf_qty': item.get('ib_cf_qty'),
        'new_ib_vs_stock_cv': item.get('new_ib_vs_stock_cv')
        } for item in s3Result]

    logging.info(f' s3 result is {transformedS3Result}')
    groupedInput = cls.Helper.groupByProduct(transformedS3Result)
    updateResult = cls.bulkUpdate(groupedInput, **kwargs)
    return updateResult
