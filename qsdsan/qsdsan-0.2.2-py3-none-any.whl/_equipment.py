#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
QSDsan: Quantitative Sustainable Design for sanitation and resource recovery systems

This module is developed by:
    Yalin Li <zoe.yalin.li@gmail.com>

This module is under the University of Illinois/NCSA Open Source License.
Please refer to https://github.com/QSD-Group/QSDsan/blob/main/LICENSE.txt
for license details.
'''


# %%

from biosteam.utils import NotImplementedMethod
from ._units_of_measure import auom

__all__ = ('Equipment',)

hasattr = hasattr

class Equipment:
    '''
    A flexible class for the design of individual equipment of a :class:`SanUnit`,
    this class can be dependent on but will not affect the mass flows within
    the unit.
    
    A non-abstract instance of this class must have:
        
        - A :func:`Equipment._design` method for equipment design.
        
            - This method should be called in the ``_design`` method of the unit
              the equipment belongs to using :func:`SanUnit.add_equipment_design`.
            - It should only take the unit this equipment belongs to as the parameter.    
            - It should return a dict that contains the design (e.g., dimensions)
              of this equipment.
            - Unit (e.g., m, kg) of the design parameters should be stored in
              the attribute ``Equipment._units``.

        - A :func:`Equipment._cost` method for equipment cost.
        
            - This method should be called in the ``_cost`` method of the unit
              the equipment belongs to using :func:`SanUnit.add_equipment_cost`.
            - It should only take the unit this equipment belongs to as the parameter.    
            - It should return a float that contains the total purchase cost of this
              equipment.
            - Installed cost (:math:`C_{BM}`) of this equipment will be caluculated \
            based on the purchase cost (:math:`C_{Pb}`)
            
                .. math::
                
                   C_{BM} = C_{Pb} (F_{BM} + F_{D}F_{P}F_{M} - 1)

    
    Parameters
    ----------
    Name : str
        Name of this equipment, can be left as None.
    design_units: dict
        Unit (e.g., m, kg) of design parameters.
    F_BM: float
        Bare module factor of this equipment.
    F_D: float
        Design factor of this equipment.
    F_P: float
        Pressure factor of this equipment.
    F_M: float
        Material factor of this equipment.
    lifetime: float
        Lifetime of this equipment.
    lifetime_unit: str
        Unit of the lifetime.
    '''    
    
    __slots__ = ('_linked_unit', 'name', 'design_units', 'F_BM', 'F_D', 'F_P', 'F_M',
                 'lifetime')
    
    def __init_subclass__(self, isabstract=False):
        if isabstract: return
        for method in ('_design', '_cost'):
            if not hasattr(self, method):
                raise NotImplementedError(
                    f'Equipment subclasses must have a {method} method unless `isabstract` is True.')
    
    _design = _cost = NotImplementedMethod
    
    def __init__(self, name=None, design_units=dict(), F_BM=1., F_D=1., F_P=1., F_M=1.,
                 lifetime=None, lifetime_unit='yr'):
        self._linked_unit = None
        self.name = name
        self.design_units = design_units
        self.F_BM = F_BM
        self.F_D = F_D
        self.F_P = F_P
        self.F_M = F_M
        self.lifetime = auom(lifetime_unit).convert(lifetime, 'yr')

    def __repr__(self):
        line = f'<{type(self).__name__}'
        line += f': {self.name}' if self.name else ''
        line += f' in {self.linked_unit}>' if self.linked_unit else '>'
        return line

    @property
    def linked_unit(self):
        '''
        :class:`SanUnit` The unit that this equipment belongs to.
        
        .. note::
            
            This property will be updated upon initiation of the unit.
        '''
        return self._linked_unit
    
    @property
    def design(self):
        '''[dict] Design information generated by :func:`Equipment._design`.'''
        return self._design()
        
    @property
    def purchase_cost(self):
        '''[float] Total purchase cost generated by :func:`Equipment._cost`.'''
        return self._cost()
    
    @property
    def installed_cost(self):
        '''[float] Total installed cost based on purchase cost and bare module factor.'''
        return self.purchase_cost*(self.F_BM+self.F_D*self.F_P*self.F_M-1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    