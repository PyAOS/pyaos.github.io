---
# Page settings
layout: default
keywords:
comments: false

# Hero section
title: The PyAOS Stack
description: An overview of the Python libraries used by the AOS community.

# Micro navigation
micro_nav: true

# Page navigation
page_nav:
    next:
        content: Next page
        url: '/install'
---

<div class="callout callout--success">
    <p><strong>A group of programs that works in tandem to produce a result
    or achieve a common goal is often referred to as a software stack. 
    This page gives an overview of the PyAOS stack.</strong>
    </p>
</div>


![PyAOS Stack](../images/pyaos-stack.svg "PyAOS Stack")


## Core libraries

The dashed box in the diagram above represents the core of the PyAOS stack,
so let’s start our tour there.
The default library for dealing with numerical arrays in Python is [NumPy](http://www.numpy.org/).
It has some built in functions for calculating very simple statistics
(e.g. maximum, mean, standard deviation),
but for more complex analysis
(e.g. interpolation, integration, linear algebra)
the [SciPy](https://www.scipy.org/scipylib/index.html) library is the default.
If you’re dealing with particularly large arrays,
[Dask](https://dask.org/) works with the existing Python ecosystem
(i.e. NumPy, SciPy, etc) to scale your analysis
to multi-core machines and/or distributed clusters (i.e. parallel processing).

If you want to visualise your NumPy data arrays the default library is [matplotlib](https://matplotlib.org/).
As you can see at the [matplotlib gallery](https://matplotlib.org/gallery.html),
this library is great for any simple (e.g. bar charts, contour plots, line graphs),
static (e.g. .png, .eps, .pdf) plots.
The [cartopy](https://scitools.org.uk/cartopy/docs/latest/) library
provides additional plotting functionality for common map projections.

While pretty much all data analysis and visualisation tasks
could be achieved with a combination of these core libraries,
their flexible, all-purpose nature means relatively common/simple tasks
can often require quite a bit of work (i.e. many lines of code).
To make things more efficient for data scientists,
the scientific Python community has therefore built a number of libraries on top of the core stack.
These high-levels libraries aren’t as flexible
– they can’t do *everything* like the core stack can –
but they can do common tasks with far less effort.


## High-level libraries (generic)

Let’s first consider the generic high-level libraries.
That is, the ones that can be used in essentially all fields of data science.
The most popular of these libraries is undoubtedly [pandas](http://pandas.pydata.org/),
which has been a real game-changer for the Python data science community.
The key advance offered by pandas is the concept of labelled arrays.
Rather than referring to the individual elements of a data array using a numeric index
(as is required with NumPy),
the actual row and column headings can be used.
That means information from the cardiac ward for the year 2005
could be obtained from a medical dataset by asking for `data.sel({'ward': ’cardiac’, 'year': 2005})`,
rather than having to remember the numeric index corresponding to that ward and year.
This labelled array feature,
combined with a bunch of other features that simplify common statistical and plotting tasks
traditionally performed with SciPy and matplotlib,
greatly simplifies the code development process (read: less lines of code).

One of the limitations of pandas
is that it’s only able to handle one- or two-dimensional (i.e. tabular) data arrays.
The [xarray](http://xarray.pydata.org/) library was therefore created
to extend the labelled array concept to x-dimensional arrays.
Not all of the pandas functionality is available
(which is a trade-off associated with being able to handle multi-dimensional arrays),
but the ability to refer to array elements by their actual latitude (e.g. 20 South),
longitude (e.g. 50 East), height (e.g. 500 hPa) and time (e.g. 2015-04-27), for example,
makes the xarray data array far easier to deal with than the NumPy array.
As an added bonus, xarray also has built in functionality for reading/writing specific AOS file formats
(e.g netCDF, GRIB), which numpy and pandas don't have.

## High-level libraries (AOS-specific)

While the xarray library is a good option for those working in the atmosphere and ocean sciences
(especially those dealing with large multi-dimensional arrays from model simulations),
the [SciTools](https://scitools.org.uk/) project led by the MetOffice
has taken a different approach to building on top of the core stack.
Rather than striving to make their software generic
(xarray is designed to handle any multi-dimensional data),
they explicitly assume that users of their [Iris](https://scitools.org.uk/iris/docs/latest/)
library are dealing with weather/ocean/climate data.
Doing this allows them to make common weather/climate tasks super quick and easy,
and it also means they have added functionality specific to atmosphere and ocean science.
(The SciTools project is also behind cartopy
and a number of other useful libraries for analysing earth science data.)

In addition to Iris, you may also come across [CDAT](https://cdat.llnl.gov),
which is maintained by the team at Lawrence Livermore National Laboratory.
It was the precursor to xarray and Iris in the sense that it was the first package
for atmosphere and ocean scientists built on top of the core Python stack.
For a number of years the funding and direction of that project shifted towards
developing a graphical interface ([VCDAT](https://vcdat.llnl.gov))
for managing large workflows and visualising data
(i.e. as opposed to further developing the capabilities of the underlying Python libraries),
but it seems that CDAT is now once again under [active development](https://github.com/CDAT/cdat/wiki).
The VCDAT application also now runs as a JupyterLab extension, which is an exciting development.

<div class="callout callout--info">
    <p><strong>How to choose</strong></p>
    <p>In terms of choosing between xarray and Iris,
    some people like the slightly more AOS-centric experience offered by Iris,
    while others don’t like the restrictions that places on their work
    and prefer the generic xarray experience
    (e.g. to use Iris your input data files have to be
    <a href="http://cfconventions.org/">CF compliant</a> or close to it).
    Either way, they are both a vast improvement on the NumPy/matplotlib experience.
    </p>
</div>


## Simplifying data exploration

While the plotting functionality associated with xarray and Iris
speeds up the process of visually exploring data (as compared to matplotlib),
there’s still a fair bit of messing around involved in tweaking the various aspects of a plot
(e.g. colour schemes, plot size, labels, map projections, etc).
This tweaking burden is an issue across all data science fields and programming languages,
so developers of the latest generation of visualisation tools
are moving towards something called *declarative visualisation*.
The basic concept is that the user simply has to describe the characteristics of their data,
and then the software figures out the optimal way to visualise it
(i.e. it makes all the tweaking decisions for you).

The two major Python libraries in the declarative visualisation space are
[HoloViews](http://holoviews.org/) and [Altair](https://altair-viz.github.io/).
The former (which has been around much longer) uses matplotlib or
[Bokeh](https://bokeh.org/) (interactive plots where you can zoom and scroll) under the hood,
which means it allows for the generation of static or interactive plots.
Since HoloViews doesn’t have support for geographic plots,
[GeoViews](http://geoviews.org/) and [hvPlot](https://hvplot.holoviz.org/)
have been created on top of it and offer geographic plotting functionality 
by leveraging many elements of the PyAOS stack 
(i.e. cartopy, xarray, dask, etc).

## Sub-discipline-specific libraries

So far we’ve considered libraries that do general,
broad-scale tasks like data input/output, common statistics, visualisation, etc.
Given their large user base,
these libraries are usually written and supported by large companies
(e.g. Anaconda supports Bokeh and HoloViews/Geoviews),
large institutions (e.g. the MetOffice supports Iris, cartopy and GeoViews)
or the wider PyData community (e.g. pandas, xarray).
Within each sub-discipline of atmosphere and ocean science,
individuals and research groups take these libraries
and apply them to their very specific data analysis tasks.
Increasingly, these individuals and groups
are formally packaging and releasing their code for use within their community.
For instance, Andrew Dawson (an atmospheric scientist at Oxford)
does a lot of EOF analysis and manipulation of wind data,
so he has released his [eofs](https://ajdawson.github.io/eofs/latest/)
and [windspharm](https://ajdawson.github.io/windspharm/latest/) libraries
(which are able to handle data arrays from NumPy, Iris or xarray).
Similarly, a group at the Atmospheric Radiation Measurement (ARM) Climate Research Facility
have released their Python ARM Radar Toolkit ([Py-ART](http://arm-doe.github.io/pyart/))
for analysing weather radar data,
and a [similar story](https://www.unidata.ucar.edu/blogs/news/entry/metpy_an_open_source_python)
is true for [MetPy](https://unidata.github.io/MetPy/latest/index.html).

<div class="callout callout--info">
    <p><strong>Coming soon</strong></p>
    <p>In terms of new libraries that might be available soon,
    the <a href="https://pangeo.io/">Pangeo</a>
    project is actively supporting and encouraging
    the development of more domain-specific geoscience packages. 
    It was also recently
    <a href="https://www.ncl.ucar.edu/Document/Pivot_to_Python/">announced</a>
    that NCAR will adopt Python as their scripting language of choice,
    so expect to see many of your favourite <a href="https://www.ncl.ucar.edu/">NCL</a>
    functions re-implemented as part of the new
    <a href="https://geocat-comp.readthedocs.io/en/latest/">GeoCAT-comp</a>
    Python library over the coming months/years.
    </p>
</div>

Check out the [Package Index](https://pyaos.github.io/packages/) for a listing of all the
sub-discipline-specific libraries in your particular area of AOS research
and the results of the [2021 PyAOS Census](https://pyaos.github.io/census/)
for more information on the wide range of Python libraries used by the AOS community.

## Summary

Most Python users in the atmosphere and ocean sciences base their data analysis
around the xarray or Iris libraries.
The appeal of these high-level libraries is that they are built on top of
(and thus hide the complexity of) core data science libraries like NumPy and matplotlib.
You will occasionally find yourself needing to use a core library directly
(e.g. you might create a plot with xarray and then call a specific matplotlib
function to customise a label on that plot),
but to avoid re-inventing the wheel your first impulse should always be
to check whether a high-level library has the functionality you need.
Nothing would be more heartbreaking than spending hours writing your own function
using the netCDF4 library for extracting the metadata contained within a netCDF file,
for instance,
only to find that xarray and Iris automatically keep this information upon reading a netCDF file.
In this way, a solid working knowledge of the PyAOS stack
can save you a lot of time and effort.
