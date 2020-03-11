---
# Page settings
layout: default
keywords:
comments: false

# Hero section
title: Package Index
description: A comprehensive listing of the Python libraries used by the AOS community.

# Micro navigation
micro_nav: true

# Page navigation
page_nav:
    prev:
        content: Previous page
        url: '/install'
    next:
        content: Next page
        url: '/training'
---

<div class="callout callout--success">
    <p><strong>If you'd like to see a package added to this list,
    check whether it's within
    <a href="https://github.com/PyAOS/pyaos.github.io/blob/master/README.md#scope">scope</a>
    and then submit an issue or pull request at the
    <a href="https://github.com/PyAOS/pyaos.github.io/">GitHub repository</a>.</strong>
    </p>
</div>


As discussed in the [overview of the PyAOS stack](https://pyaos.github.io/stack/),
most Python users in the atmosphere and ocean sciences
base their data analysis around one of the following all-purpose packages:
* [xarray](http://xarray.pydata.org/en/stable/) (supported by the PyData community)
* [iris](https://scitools.org.uk/iris/docs/latest/) (supported by the [SciTools](https://scitools.org.uk/) project)
* [cdat](https://cdat.llnl.gov/) (supported by Lawrence Livermore National Laboratory)

There are then a myriad of packages available for specific AOS analysis tasks,
many of which extend the functionality of the all-purpose PyAOS packages
and/or the more generic data science packages such as [NumPy](http://www.numpy.org/)
and [matplotlib](https://matplotlib.org/). 

## General utilities

**[GeoCAT-comp](https://geocat-comp.readthedocs.io/en/latest/)** ([GeoCAT](https://geocat.ucar.edu/) project)  
Computational routines from the NCAR Command Language (NCL).

**[PyFerret](https://ferret.pmel.noaa.gov/Ferret/documentation/pyferret)** (PMEL)  
Quick exploration of oceanographic data.

**[eofs](https://ajdawson.github.io/eofs/latest/)** (Andrew Dawson)  
EOF analysis of spatial-temporal data.

**[windspharm](https://ajdawson.github.io/windspharm/latest/)** (Andrew Dawson)  
Computations on global wind fields in spherical geometry.

**[Siphon](https://www.unidata.ucar.edu/software/siphon/)** ([UniData](https://www.unidata.ucar.edu/))  
Utilities for downloading data from remote data services.

## Visualisation

**[Cartopy](https://scitools.org.uk/cartopy/docs/latest/)** ([SciTools](https://scitools.org.uk/) project)  
Geographic map projections for plotting.

**[geoviews](http://geoviews.org/)** ([HoloViz](https://holoviz.org/) project)  
Interactive exploration and visualisation of geographical, meteorological, and oceanographic datasets.

**[cmocean](https://matplotlib.org/cmocean/)** (Kristen Thyng)  
Beautiful colormaps for oceanography.

## Meteorology

**[MetPy](https://www.unidata.ucar.edu/software/metpy/)** ([UniData](https://www.unidata.ucar.edu/))  
Tools for reading, visualising and performing calculations with weather data.

**[Satpy](https://satpy.readthedocs.io/en/latest/)** ([PyTroll community](http://pytroll.github.io/))  
Reading, manipulating, and writing data from remote-sensing earth-observing meteorological satellite instruments.

**[Py-ART](https://arm-doe.github.io/pyart/)** ([ARM User Facility](https://www.arm.gov/data/work-with-arm-data))  
Weather radar algorithms and utilities.

**[ACT](https://arm-doe.github.io/ACT/)** ([ARM User Facility](https://www.arm.gov/data/work-with-arm-data))  
Toolkit for working with atmospheric time-series datasets of varying dimensions.

**[PyDSD](http://josephhardinee.github.io/PyDSD/)** (Joseph Hardin and Nick Guy)  
Utilities for working with disdrometer data.

## Oceanography

**[GSW-Python](https://teos-10.github.io/GSW-Python/)**  
Python implementation of the Thermodynamic Equation of Seawater 2010 (TEOS-10).

## Climate

**[climtas](https://climtas.readthedocs.io/en/latest/)** (Scott Wales)  
Climtas is a package for working with large climate analyses.
It focuses on the time domain with custom functions for Xarray and Dask data.

**[climate-indices](https://climate-indices.readthedocs.io/en/latest/)** (James Adams)  
Various climate index algorithms relating to precipitation and temperature.

## Regridding

**[xESMF](https://xesmf.readthedocs.io/en/latest/)** (Jiawei Zhuang)  
Universal regridder for geospatial data.

**[gridded](https://noaa-orr-erd.github.io/gridded/)** (NOAA-ORR-ERD)  
A single way to work with results from any hydrodynamic/oceanographic model regardless of what type of grid it was computed on.

**[pyResample](https://pyresample.readthedocs.io/en/latest/)** ([PyTroll community](http://pytroll.github.io/))  
Resampling geospatial image data.

**[ESMPy](https://earthsystemcog.org/projects/esmpy/)**  
Interface to the Earth System Modeling Framework (ESMF) regridding utility.

**[pyproj](https://pyproj4.github.io/pyproj/stable/)**  
Interface to PROJ (cartographic projections and coordinate transformations library).

## Modeling

**[wrf-python](https://wrf-python.readthedocs.io/en/latest/)** ([GeoCAT](https://geocat.ucar.edu/) project)   
A collection of diagnostic and interpolation routines for use with output from the Weather Research and Forecasting (WRF-ARW) Model.

**[climlab](https://climlab.readthedocs.io/en/latest/)** (Brian Rose)  
Process-oriented climate modeling.

**[climt](https://climt.readthedocs.io/en/latest/)** (Joy Monteiro et al)  
Climate modelling and diagnostics toolkit.

**[pyrcel](https://github.com/darothen/pyrcel)** (Daniel Rothenberg)  
Adiabatic cloud parcel model for studying aerosol activation.

**[PyCLES](https://github.com/pressel/pycles)**  (Kyle Pressel and Colleen Kaul)  
Atmospheric large eddy simulation infrastructure designed to simulate boundary layer clouds and deep convection.

## Workflow management

**[aospy](https://aospy.readthedocs.io/en/stable/)** (Spencer Hill)  
Automated climate data analysis and management.

**[cmdline-provenance](https://cmdline-provenance.readthedocs.io/en/latest/)** (Damien Irving)  
For keeping track of your data processing steps.
 
