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
base their data analysis around one of the following all-purpose packages
(listed in order of popularity/usage):
* [xarray](http://xarray.pydata.org/en/stable/) (supported by the [PyData](https://pydata.org/) community)
* [iris](https://scitools.org.uk/iris/docs/latest/) (supported by the [SciTools](https://scitools.org.uk/) project)
* [cf-python](https://ncas-cms.github.io/cf-python/) (supported by the [NCAS-CMS](https://cms.ncas.ac.uk/))
* [PyGeode](https://pygeode.github.io/)

There are then a myriad of packages available for general geospatial and specific AOS analysis tasks,
many of which extend the functionality of the all-purpose PyAOS packages
and/or the more generic data science packages such as [NumPy](http://www.numpy.org/)
and [matplotlib](https://matplotlib.org/). 

The package listing below captures Python packages that are unique to the atmosphere and ocean sciences.
The focus is on packages that are under active development and/or maintenance,
have a non-trivial user-base (i.e. more users than just the author/s) and offer unique functionality.
Check out the [awesome-spatial](https://github.com/RoboDonut/awesome-spatial#readme),
[awesome-open-geoscience](https://github.com/softwareunderground/awesome-open-geoscience#readme)
and [awesome-earth-artificial-intelligence](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence/blob/master/README.md)
lists for more general (i.e. not specific to AOS) packages that might be of use.
There is some overlap between the scope of the list below and the
[awesome-coastal](https://github.com/chrisleaman/awesome-coastal#readme), 
[awesome-open-climate-science](https://github.com/pangeo-data/awesome-open-climate-science#readme) and 
[xarray related projects](https://docs.xarray.dev/en/latest/ecosystem.html) lists.

## General utilities

**[GeoCAT-comp](https://geocat-comp.readthedocs.io/en/latest/)** ([GeoCAT](https://geocat.ucar.edu/) project)  
Computational routines from the NCAR Command Language (NCL).

**[PyFerret](https://ferret.pmel.noaa.gov/Ferret/documentation/pyferret)** (PMEL)  
Quick exploration of oceanographic data.

**[xCDAT](https://xcdat.readthedocs.io/en/latest/)** (Lawrence Livermore National Laboratory)  
An extension of xarray for climate data analysis on structured grids.
Serves as a spiritual successor to the Community Data Analysis Tools (CDAT) library.

## Data access

**[acccmip6](https://acccmip6.readthedocs.io/)** (Taufiq Hassan Mozumder)  
Access and search the CMIP6 database in real time. 

**[CliMetLab](https://climetlab.readthedocs.io/)** ([ECMWF](https://www.ecmwf.int/))  
Simplified access to climate and meteorological datasets.

**[Siphon](https://www.unidata.ucar.edu/software/siphon/)** ([UniData](https://www.unidata.ucar.edu/))  
Utilities for downloading data from remote data services.

## Visualisation

**[Cartopy](https://scitools.org.uk/cartopy/docs/latest/)** ([SciTools](https://scitools.org.uk/) project)  
Geographic map projections for plotting.

**[cf-plot](http://ajheaps.github.io/cf-plot/)**  
cf-python related functions for common contour, vector and line plots used in climate research.

**[cmocean](https://matplotlib.org/cmocean/)** (Kristen Thyng)  
Beautiful colormaps for oceanography. See [xcmocean](https://xcmocean.readthedocs.io/) for xarray integration.

**[GeoCAT-viz](https://geocat-viz.readthedocs.io/)** ([GeoCAT](https://geocat.ucar.edu/) project)  
Visualization routines from the NCAR Command Language (NCL).
Examples at [GeoCAT-examples](https://geocat-examples.readthedocs.io/en/latest/).

**[geoviews](http://geoviews.org/)** ([HoloViz](https://holoviz.org/) project)  
Interactive exploration and visualisation of geographical, meteorological, and oceanographic datasets.

**[xmovie](https://xmovie.readthedocs.io/)** (Julius Busecke)  
Movies from xarray objects.

## Meteorology

**[ACT](https://arm-doe.github.io/ACT/)** ([ARM User Facility](https://www.arm.gov/data/work-with-arm-data))  
Toolkit for working with atmospheric time-series datasets of varying dimensions.

**[MetPy](https://www.unidata.ucar.edu/software/metpy/)** ([UniData](https://www.unidata.ucar.edu/))  
Tools for reading, visualising and performing calculations with weather data.

**[Py-ART](https://arm-doe.github.io/pyart/)** ([ARM User Facility](https://www.arm.gov/data/work-with-arm-data))  
Weather radar algorithms and utilities.

**[PyDDA](https://openradarscience.org/PyDDA/)**  
Direct data assimilation framework for wind retrievals.

**[PyDSD](http://josephhardinee.github.io/PyDSD/)** (Joseph Hardin and Nick Guy)  
Utilities for working with disdrometer data.

**[pyet](https://pyet.readthedocs.io)** (Matevz Vremec & Raoul Collenteur)  
Estimation of potential evapotranspiration.

**[pyPI](https://github.com/dgilford/pyPI)** (Daniel Gilford)  
Tropical cyclone potential intensity calculations.

**[pyThermalComfort](https://pythermalcomfort.readthedocs.io/)** (Center for the Built Environment at UC Berkeley)  
Toolkit for calculating thermal comfort indices, heat/cold stress metrics, and thermophysiological responses.

**[Satpy](https://satpy.readthedocs.io/)** ([PyTroll community](http://pytroll.github.io/))  
Reading, manipulating, and writing data from remote-sensing earth-observing meteorological satellite instruments.

**[thermofeel](https://thermofeel.readthedocs.io/)** (ECMWF)  
A library to calculate human thermal comfort indexes.

**[tobac](https://tobac.readthedocs.io/)**  
Tracking and object-based analysis of clouds.

**[windspharm](https://ajdawson.github.io/windspharm/latest/)** (Andrew Dawson)  
Computations on global wind fields in spherical geometry.

**[xcape](https://xcape.readthedocs.io/)**  
Fast convective parameters for numpy, dask, and xarray.

## Oceanography

**[argopy](https://argopy.readthedocs.io/)** (Guillaume Maze)  
Argo data access, visualisation and manipulation.

**[CloudDrift](https://cloud-drift.github.io/clouddrift/)** (University of Miami)  
A platform for accelerating research with Lagrangian climate data.

**[glidertools](https://glidertools.readthedocs.io/en/latest/)**  
Toolbox for processing underwater glider data.

**[GSW-Python](https://teos-10.github.io/GSW-Python/)**  
Python implementation of the Thermodynamic Equation of Seawater 2010 (TEOS-10).  
See [gsw-xarray](https://gsw-xarray.readthedocs.io/) for a wrapper that adds CF attributes to xarray outputs.

**[mixsea](https://mixsea.readthedocs.io/)** (Jesse Cusack & Gunnar Voet)  
Turbulence parameter estimation from fine scale oceanographic data.

**[neutralocean](https://neutralocean.readthedocs.io/)** (Geoff Stanley)  
Calculate oceanic neutral surfaces and related things.

**[OceanParcels](https://oceanparcels.org/)**  
Customisable particle tracking simulations using output from Ocean Circulation models.

**[ocetrac](https://ocetrac.readthedocs.io/)** (Hillary Scannell)  
Label and track the evolution of unique geospatial features in gridded datasets.

**[PyCO2SYS](https://PyCO2SYS.readthedocs.io/)** (Matthew Humphreys et al.)  
Marine carbonate system solver.

## Climate

**[climate-indices](https://climate-indices.readthedocs.io/)** (James Adams)  
Various climate index algorithms relating to precipitation and temperature.

**[climpred](https://climpred.readthedocs.io/)** (Riley Brady and Aaron Spring)  
Verification of weather and climate forecasts.

**[icclim](https://icclim.readthedocs.io/)** ([CERFACS GLOBC](https://cerfacs.fr/en/climate-modelling-and-global-change-globc/))  
Index Calculation for CLIMate.

**[xclim](https://xclim.readthedocs.io/)** ([Ouranos](https://ouranos.ca/))  
Functions to compute climate indices from observations or model simulations.

**[xmip](https://cmip6-preprocessing.readthedocs.io/)** (Julius Busecke)  
Tools for cleaning/standardization of the metadata associated with CMIP6 data files.

## Data reduction (temporal or spatial)

**[climtas](https://climtas.readthedocs.io/)** (Scott Wales)  
Climtas is a package for working with large climate analyses.
Focuses on the time domain with custom functions for Xarray and Dask data.

**[clisops](https://clisops.readthedocs.io)** ([ROOCS](https://roocs.github.io/))  
Climate simulation operations (temporal and spatial subsetting and averaging of xarray data sets).
Related to [daops](https://daops.readthedocs.io).

**[eofs](https://ajdawson.github.io/eofs/latest/)** (Andrew Dawson)  
EOF analysis of spatial-temporal data.

**[regionmask](https://regionmask.readthedocs.io/)** (Mathias Hauser)  
Masking of of geographic regions.

**[xeofs](https://xeofs.readthedocs.io)** (Niclas Rieger)  
EOF analysis in Python with xarray.

## Spatial grids

**[ESMPy](https://earthsystemcog.org/projects/esmpy/)**  
Interface to the Earth System Modeling Framework (ESMF) regridding utility.

**[GCM-Filters](https://gcm-filters.readthedocs.io/)** ([Ocean Transport and Eddy Energy Climate Process Team](https://ocean-eddy-cpt.github.io/))  
Diffusion-based spatial filtering of gridded data.

**[gridded](https://noaa-orr-erd.github.io/gridded/)** (NOAA-ORR-ERD)  
A single way to work with results from any hydrodynamic/oceanographic model regardless of what type of grid it was computed on.

**[pyproj](https://pyproj4.github.io/pyproj/stable/)**  
Interface to PROJ (cartographic projections and coordinate transformations library).

**[pyResample](https://pyresample.readthedocs.io/)** ([PyTroll community](http://pytroll.github.io/))  
Resampling geospatial image data.

**[Uxarray](https://uxarray.readthedocs.io/)** ([Project Raijin](https://raijin.ucar.edu/))  
Reading and recognizing unstructured grid models.

**[xarray-regrid](https://xarray-regrid.readthedocs.io/)**  
Extends xarray with regridding methods, making it possible to easily and effiently regrid between two rectilinear grids.

**[xESMF](https://xesmf.readthedocs.io/)** (Jiawei Zhuang)  
Universal regridder for geospatial data.

## Modeling

**[climlab](https://climlab.readthedocs.io/)** (Brian Rose)  
Process-oriented climate modeling.

**[climt](https://climt.readthedocs.io/)** (Joy Monteiro et al)  
Climate modelling and diagnostics toolkit.

**[PyCLES](https://github.com/pressel/pycles)**  (Kyle Pressel and Colleen Kaul)  
Atmospheric large eddy simulation infrastructure designed to simulate boundary layer clouds and deep convection.

**[pyrcel](https://github.com/darothen/pyrcel)** (Daniel Rothenberg)  
Adiabatic cloud parcel model for studying aerosol activation.

**[scores](https://scores.readthedocs.io/)** (Australian Bureau of Meteorology)  
Verification and evaluation for forecasts and models.

**[wrf-python](https://wrf-python.readthedocs.io/)** ([GeoCAT](https://geocat.ucar.edu/) project)   
A collection of diagnostic and interpolation routines for use with output from the Weather Research and Forecasting (WRF-ARW) Model.

**[xgcm](https://xgcm.readthedocs.io/)**  
General circulation model post-processing with xarray.

**[xsdba](https://xsdba.readthedocs.io/)** ([Ouranos](https://ouranos.ca/))  
Statistical downscaling and bias adjustment with xarray and dask.

**[xskillscore](https://xskillscore.readthedocs.io/)**  
Metrics for verifying model forecasts.

**[xWRF](https://xwrf.readthedocs.io/)**  
Interface for working with the Weather Research and Forecasting (WRF) model output in xarray.

## Climate and Forecast (CF) metadata conventions

**[cf-checker](https://github.com/cedadev/cf-checker)** ([CEDA](https://www.ceda.ac.uk/))  
Check compliance of netCDF files against the CF Convention.

**[cfdm](https://ncas-cms.github.io/cfdm/)** ([NCAS-CMS](https://cms.ncas.ac.uk/))  
Implements the data model of the CF metadata conventions.

**[cf-xarray](https://cf-xarray.readthedocs.io/)** (Deepak Cherian)  
Lightweight accessor for xarray objects that interprets CF attributes.

**[compliance-checker](https://github.com/ioos/compliance-checker)** ([IOOS](https://ioos.noaa.gov/))  
Check compliance of netCDF files against CF, ACDD, and IOOS Metadata Profile file standards.

## Workflow management

**[aospy](https://aospy.readthedocs.io/en/stable/)** (Spencer Hill)  
Automated climate data analysis and management.

**[cmdline-provenance](https://cmdline-provenance.readthedocs.io/)** (Damien Irving)  
For keeping track of your data processing steps.
 
