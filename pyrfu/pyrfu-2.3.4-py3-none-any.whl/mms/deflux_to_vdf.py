#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2020 Louis Richard
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so.

"""deflux_to_vdf.py
@author: Louis Richard
"""

import numpy as np
import xarray as xr

from scipy import constants

from .spectr_to_dataset import spectr_to_dataset


def deflux_to_vdf(deflux):
    """Compute differential energy flux from velocity distribution
    function.

    Parameters
    ----------
    deflux : xarray.Dataset or xarray.DataArray
        Time series of the differential energy flux in 1/(cm^2 s sr keV).

    Returns
    -------
    vdf : xarray.Dataset
        Time series of the velocity distribution function. Units must be
        either s^3/m^6.

    """

    if isinstance(deflux, xr.DataArray):
        deflux = spectr_to_dataset(deflux)

    if deflux.attrs["species"] in ["ions", "i"]:
        mass_ratio = 1
    elif deflux.attrs["species"] in ["electrons", "e"]:
        mass_ratio = constants.electron_mass / constants.proton_mass
    else:
        raise ValueError("Invalid specie")

    if deflux.attrs["UNITS"] == "keV/(cm^2 s sr keV)":
        tmp_data = deflux.data.data / 1e12 * 0.53707 * mass_ratio ** 2
    else:
        raise ValueError("Invalid unit")

    energy = deflux.energy.data

    if tmp_data.ndim == 2:
        tmp_data = tmp_data[:, :, None, None]

    data_r = np.reshape(tmp_data, (tmp_data.shape[0], tmp_data.shape[1],
                                   np.prod(tmp_data.shape[2:])))

    if energy.ndim == 1:
        energy_mat = np.tile(energy,
                             (len(deflux.time), np.prod(tmp_data.shape[2:]),1))
        energy_mat = np.transpose(energy_mat, [0, 2, 1])
    elif energy.ndim == 2:
        energy_mat = np.tile(energy, (np.prod(tmp_data.shape[2:]), 1, 1))
        energy_mat = np.transpose(energy_mat, [1, 2, 0])
    else:
        raise ValueError("Invalid energy shape")

    data_r /= energy_mat ** 2
    tmp_data = np.reshape(data_r, tmp_data.shape)

    vdf = deflux.copy()
    vdf.data.data = np.squeeze(tmp_data)
    vdf.attrs["UNITS"] = "s^3/m^6"

    return vdf
