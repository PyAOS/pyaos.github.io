The Python for Atmosphere and Ocean Science (PyAOS) website and mailing list was established almost a decade ago to provide information and resources to the user community. In order to keep the site up-to-date, the first ever PyAOS census was launched in May 2021. There were 144 participants in the survey, allowing for a detailed analysis of how Python is being used by those working and studying in the weather, ocean and climate sciences.

# Summary

Census respondents were overwhelmingly male (75%), young (74% were under 40) and based in the USA (60%).
They had typically been using Python for at least two years (82%) and were self-taught (mainly from Stack Overflow).
Only 30% reported having attended a Python workshop of any kind and only 19% encountered Python during university.
Almost all respondents primarily work with raster (i.e. gridded) data stored in netCDF format,
but older (GRIB) and newer (Zarr) raster formats were also widely used (35% and 26% of respondents, respectively).
About half of respondents also do at least some work with vector data, typically in the form of Shapefiles.
Two-thirds of people indicated that they do at least some of their analysis on a supercomputer
(e.g. hosted by their institution or a national facility) and one-third on the cloud (e.g. Amazon Web Services),
but over half said a personal computer is still the platform they most commonly use for data science.
Jupyter was the most popular development environment by a wide margin, with a quarter of respondents listing no other IDE or text editor.
In terms of specific Python libraries, xarray dominates the reported PyAOS stack.
It had a much larger user base than competing general purpose PyAOS libraries (iris and CDAT)
and most of the new libraries entering the stack build upon the xarray DataArray.
So far there has been little take up of libraries that allow for interactive (as opposed to static)
data exploration/visualisation (e.g. geoviews, hvplot),
while the use of libraries that test code (e.g. unittest) or parse the command line (e.g. argparse) is rare.
A clear inference from the survey is that for many respondents data processing workflows are coordinated exclusively from a Jupyter notebook.

<p align="left">
<img src="../images/census_main_stack.svg" width="800">
</p>
Figure 1: The PyAOS software stack, as reported by survey respondents.


# Detailed results 

### Age?

| Age group | Count | Percentage |
| :-- | :-- | :-- |
| 20-29 | 45 | 32% |
| 30-39 | 60 | 42% |
| 40-49 | 23 | 16% |
| 50-59 | 10 | 7% |
| 60-69 | 4 | 3% |

### Gender: How do you identify?

| Gender | Count | Percentage |
| :-- | :-- | :-- |
| Man | 106 | 75% |
| Woman | 35 | 25% |
| Non-binary | 1 | 0% |

### Country of residence?

| Country | Count | Percentage |
| :-- | :-- | :-- |
| United States | 82 | 60% |
| Australia | 23 | 17% |
| Great Britain | 9 | 7% |
| India | 5 | 4% |
| Brazil | 3 | 2% |
| Sweden | 2 | 1% |
| China | 2 | 1% |

Plus one respondent from each of Austria, Canada, South Korea, Netherlands, Germany, New Zealand, Spain, Taiwan, Chile and Finland.

### Primary AOS discipline/s (select all that apply)

| Discipline | Count | Percentage (of total participants) |
| :-- | :-- | :-- |
| Meteorology | 54 | 38% |
| Modelling | 53 | 37% |
| Physical Oceanography | 49 | 35% |
| Atmospheric Dynamics | 48 | 33% |
| Climate Change Processes | 29 | 20% |
| Climatology (excl. Climate Change Processes) | 28 | 20% |
| AOS Research Software Engineer | 21 | 15% |
| Cloud Physics | 18 | 13% |
| AOS Research Computing Support | 14 | 10% |
| Atmospheric Radiation | 12 | 8% |
| Biological Oceanography | 11 | 8% |
| Chemical Oceanography | 9 | 6% |
| Tropospheric and Stratospheric Physics | 8 | 6% |
| Atmospheric Chemistry | 5 | 4% |
| Atmospheric Aerosols | 5 | 4% |
| Paleoclimatology | 2 | 1% |
| Remote Sensing | 1 | 1% |

### How long have you been using Python? 

| Time | Count | Percentage |
| :-- | :-- | :-- |
| Less than 1 year | 16 | 11% |
| 1-2 years | 10 | 7% |
| 2-5 years | 54 | 38% |
| 6-10 years | 42 | 29% |
| More than 10 years | 21 | 15% |

### How have you learned Python? (select all that apply)

| Method | Count | Percentage |
| :-- | :-- | :-- |
| Self taught (from textbooks, online tutorials, etc) | 128 | 90% |
| Workshop/s (e.g. Carpentries, Unidata) | 42 | 30% |
| University semester course/s (e.g. "Introduction to Programming") | 27 | 19% |
| University degree (e.g. Bachelor of Software Engineering) | 8 | 6% |

### What types of AOS data do you work with (select all that apply)?

| Data type | Count | Percentage |
| :-- | :-- | :-- |
| Raster data | 137 | 98% |
| Tabular data | 86 | 61% |
| Vector data | 70 | 50% |

### Which type of AOS data do you most commonly work with?

| Data type | Count | Percentage |
| :-- | :-- | :-- |
| Raster data | 109 | 80% |
| Tabular data | 21 | 15% |
| Vector data | 6 | 4% |

### What file formats are your AOS data stored in? (select all that apply)

| Format | Count | Percentage | 
| :-- | :-- | :-- |
| netCDF | 141 | 99% |
| CSV | 92 | 65% |
| GRIB  | 49 | 35% |
| Shapefile | 41 | 29% |
| HDF | 40 | 28% |
| Zarr | 37 | 26% |
| GeoTIFF | 33 | 23% |
| GeoJSON | 21 | 15% |
| A custom binary format | 18 | 13% |

There were also a small number of responses for GeoPackage (5), ICARTT (3), ESRI File Geodatabase (3), SQL (2), Plain text (ASCII) (2), NPY (1), JSON (1), Video (1), SQLite (1), MAT (1), Images (1), Relational Database (1), GeoParquet (1) and Audio (1).

### Which format do you most commonly work with?

| Format | Count | Percentage |
| :-- | :-- | :-- |
| netCDF | 100 | 70% |
| CSV | 14 | 10% |
| Zarr | 11 | 8% |
| GRIB | 7 | 5% |
| Shapefile | 3 | 2% |
| HDF | 2 | 1% |
| GeoJSON | 1 | 1% |
| ICARTT | 1 | 1% |
| A custom binary format | 1 | 1% |
| JSON | 1 | 1% |

### What computing platforms do you use for your AOS data science? (select all that apply)

| Computing platform | Count | Percentage | 
| :-- | :-- | :-- |
| Personal laptop/desktop | 128 | 90% |
| Supercomputer (e.g. run by your institution or a national facility) | 91 | 64% |
| Cloud (e.g. Amazon Web Services) | 45 | 32% |
| Local server (e.g. provided by your department) | 6 | 4% |

### Which platform do you most commonly work on for your AOS data science?

| Computing platform | Count | Percentage |
| :-- | :-- | :-- |
| Personal laptop/desktop | 81 | 57% |
| Supercomputer | 46 | 32% |
| Cloud | 8 | 6% |
| Local server | 3 | 2% |

### What development environments do you regularly use for your Python coding? (select all that apply)

| Environment | Count | Participant |
| :-- | :-- | :-- |
| Jupyter | 118 | 84% |
| Vim | 50 | 35% |
| VSCode | 24 | 17% |
| Spyder | 22 | 16% |
| PyCharm | 19 | 13% |
| Atom | 10 | 7% |
| Sublime Text | 9 | 6% |
| Notepad ++ | 7 | 5% |
| Emacs | 6 | 4% |
| bbedit | 1 | 1% |
| gedit | 1 | 1% |
| Google Colab | 1 | 1% |

### Libraries

Question: Writing Python code typically begins with importing various libraries that are either part of the Python standard library or that you've installed using the Python package installer (pip) or conda. Take a look back over five Python scripts / notebooks that you've written recently for AOS data science tasks and cut and paste below all the import statements that you used in those scripts / notebooks (please remove any duplicates).

Answers: See below for all libraries listed by more than one respondent.

#### Core libraries

| Library | Count | Percentage |
| :-- | :-- | :-- |
| numpy | 120 | 86% |
| matplotlib | 111 | 80% |
| xarray | 97 | 69% |
| cartopy | 70 | 50% |
| dask | 27 | 19% |
| iris | 5 | 4% |
| cdutil | 1 | 1% |
| cdms2 | 1 | 1% |
| MV2  | 1 | 1% |

#### Remote data access

| Library | Count | Percentage |
| :-- | :-- | :-- |
| siphon | 8 | 6% |
| pydap | 3 | 2% |
| erddapy | 3 | 2% |

#### Interfaces to (non-Python) geospatial libraries

| Library | Count | Percentage |
| :-- | :-- | :-- |
| shapely | 11 | 8% |
| pyproj | 2 | 1% |

#### Interfaces to file formats

| Library | Count | Percentage |
| :-- | :-- | :-- |
| netcdf4 | 35 | 25% |
| zarr | 4 | 3% |
| pygrib | 4 | 3% |
| h5py | 4 | 3% |
| rasterio | 2 | 1% |
| shapefile | 2 | 1% |

#### AOS utilities

| Library | Count | Percentage |
| :-- | :-- | :-- |
| cmocean | 22 | 16% |
| metpy | 20 | 14% |
| pyart | 7 | 5% |
| gsw | 4 | 3% |
| glidertools | 3 | 2% |
| eofs | 3 | 2% |
| windspharm | 2 | 1% |

#### xarray extensions

| Library | Count | Percentage |
| :-- | :-- | :-- |
| xgcm | 11 | 8% |
| xesmf | 8 | 6% |
| xrft  | 5 | 4% |
| xhistogram | 2 | 1% |

#### CF utilities

| Library | Count | Percentage |
| :-- | :-- | :-- |
| cftime | 4 | 3% |
| cf_units | 3 | 2% |
| nc_time_axis | 2 | 1% |
| cfgrib | 2 | 1% |

#### Plotting

| Library | Count | Percentage |
| :-- | :-- | :-- |
| seaborn | 16 | 11% |
| pylab | 3 | 2% |
| bokeh | 2 | 1% |
| hvplot | 2 | 1% |
| plotly | 2 | 1% |
| proplot | 2 | 1% |

#### General data science

| Library | Count | Percentage |
| :-- | :-- | :-- |
| pandas | 73 | 52% |
| scipy | 53 | 38% |
| sklearn | 10 | 7% |
| geopandas | 10 | 7% |
| intake | 8 | 6% |
| statsmodels | 7 | 5% |
| numba | 5 | 4% |
| pyresample | 2 | 1% |
| sparse | 2 | 1% |
| skimage | 2 | 1% |
| descartes | 2 | 1% |

#### Standard library

| Library | Count | Percentage |
| :-- | :-- | :-- |
| datetime | 49 | 35% |
| os | 47 |  34% |
| sys | 37 | 26% |
| glob | 28 | 20% |
| pathlib | 14 | 10% |
| re | 13 | 9% |
| math | 12 | 9% |
| warnings | 11 | 8% |
| copy | 10 | 7% |
| time | 9 | 6% |
| pickle | 8 | 6% |
| csv | 8 | 6% |
| shutil | 8 | 6% |
| argparse | 8 | 6% |
| collections | 7 | 5% |
| subprocess | 7 | 5% |
| urllib | 6 | 4% |
| json | 6 | 4% |
| gzip | 4 | 3% |
| logging |  4| 3% |
| string | 3 | 2% |
| importlib | 3 | 2% |
| io | 3 | 2% |
| multiprocessing | 3 | 2% |
| itertools | 3 | 2% |
| fileinput | 2 | 1% |
| getopt | 2 | 1% |
| fnmatch | 2 | 1% |
| unittest | 2 | 1% |
| dataclasses | 2 | 1% |
| pdb | 2 | 1% |
| select | 2 | 1% |
| gc | 2 | 1% |
| calendar | 2 | 1% |
| uuid | 2 | 1% |
| socket | 2 | 1% |
| ctypes | 2 | 1% |
| tempfile | 2 | 1% |

#### Miscellaneous

| Library | Count | Percentage |
| :-- | :-- | :-- |
| requests | 11 | 8% |
| pytz | 5 | 4% |
| tqdm | 5 | 4% |
| psycopg2 | 3 | 2% |
| dateutil | 3 | 2% |
| fsspec | 2 | 1% |
| sqalchemy | 2 | 1% |
| gcsfs | 2 | 1% |
| lxml | 2 | 1% |
| mpi4py | 2 | 1% |
| dash | 2 | 1% |
| joblib | 2 | 1% |
| rechunker | 2 | 1% |
| yaml | 2 | 1% |

