## The PyAOS Census

The Python for Atmosphere and Ocean Science (PyAOS; https://pyaos.github.io/) website and mailing list
was established almost a decade ago to provide information and resources to the user community.
In order to keep the site up-to-date, the first ever PyAOS census was launched in May 2021.
Over 140 people participated in the survey, allowing for a detailed analysis
of how Python is being used by those working and studying in the weather, ocean and climate sciences.
Census respondents were overwhelmingly male (75%), young (74% were under 40) and based in the USA (57%).
They had typically been using Python for at least two years (82%) and were self-taught (mainly from Stack Overflow).
Only 30% reported having attended a Python workshop of any kind and only 19% encountered Python during university.
Almost all respondents primarily work with raster (i.e. gridded) data stored in netCDF format,
but the GRIB and Zarr raster formats were also widely used (35% and 26% of respondents, respectively).
About half of respondents also do at least some work with vector data, typically in the form of Shapefiles.
Two-thirds of people indicated that they do at least some of their analysis on a supercomputer
(e.g. hosted by their institution or a national facility) and one-third on the cloud (e.g. Amazon Web Services),
but over half said a personal computer is still the platform they most commonly use for data science.
Jupyter was the most popular development environment by a wide margin,
with a quarter of respondents listing no other IDE or text editor.
In terms of specific Python libraries, xarray dominates the reported PyAOS stack.
It had a much larger user base than competing general purpose PyAOS libraries (iris and CDAT)
and most of the new libraries entering the stack build upon the xarray DataArray.
So far there has been little take up of libraries that allow for interactive
(as opposed to static) data exploration/visualisation (e.g. geoviews, hvplot),
while the use of libraries that test code (e.g. unittest) or parse the command line (e.g. argparse) is rare.
A clear inference from the survey is that for many respondents data processing workflows are coordinated exclusively from a Jupyter notebook.
If the results of the census are representative of the wider PyAOS community,
they have important implications for the future development of the PyAOS stack,
education initiatives (from workshops to package documentation),
and also efforts to make weather, ocean and climate science more open and reproducible.
