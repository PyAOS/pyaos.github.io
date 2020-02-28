---
# Page settings
layout: default
keywords:
comments: false

# Hero section
title: Installation Guide
description: How to install the PyAOS stack.

# Micro navigation
micro_nav: true

# Page navigation
page_nav:
    prev:
        content: Previous page
        url: '/stack'
    next:
        content: Next page
        url: '/packages'
---

<div class="callout callout--success">
    <p><strong>Most people in the PyAOS community install and manage
    their Python environments using Anaconda/conda.</strong>
    </p>
</div>

## The Python Package Installer (pip)

As you might expect,
the default approach to installing Python on your computer
(if it doesn’t already come with it)
is to simply download and run the installer from
[python.org/downloads](https://www.python.org/downloads/).
This will install what is known as the Python standard library –
the few hundred modules that together perform the core functions of the programming language.
These modules are very important
(e.g. without them Python wouldn’t know how to interact with the operating system or the Internet),
but unless you’re a software developer you probably don’t need to know that much about them.
Instead, what research scientists are usually interested in are the various Python packages
that software developers have written (using the standard library)
for doing things like data visualization, statistics and reading/writing netCDF files.
The authors of such packages will typically make them available via the
[Python Package Index](https://pypi.org/),
so that people can then install them using a command line function called
[pip](https://pip.pypa.io/en/stable/)
(which comes with the standard library).

## Python Distributions

While using pip to install and manage your Python environment sounds simple,
the task of identifying all the packages you need and then
installing them in such a way that they interact nicely together can be very difficult.
The problem arises because many packages have *dependencies* –
other modules and libraries that they depend on to function properly.
Sometimes it is possible to simply install dependencies using pip,
but until recently pip only worked for libraries written in pure Python.
This is a major limitation for the data science community,
because many scientific Python libraries have C and/or Fortran dependencies.
Even if all the dependencies you need are written in pure Python,
problems can arise if different packages depend on different versions of the same library.

To spare people the pain of installing dependencies,
a number of scientific Python "distributions" have been released over the years.
These come with the most popular data science libraries and their dependencies pre-installed.
Some also come with a package manager to assist with installing additional libraries
that weren't pre-installed. 

## Anaconda

The most widely used scientific Python distribution (by far) is [Anaconda](https://www.anaconda.com/distribution/).
According to the [latest documentation](https://docs.anaconda.com/anaconda/#anaconda-navigator-or-conda),
Anaconda comes with over 250 of the most widely used data science libraries (and their dependencies) pre-installed.
In addition, thousands more of the most popular data science libraries can be added/installed
using their [conda](https://docs.conda.io/en/latest/) package manager.
Data Carpentry have a great
[PyAOS conda tutorial](https://carpentrieslab.github.io/python-aos-lesson/01-conda/index.html)
to get you started.

#### Anaconda Cloud

A potential problem for the PyAOS community is that many of the packages we use are
highly discipline-specific,
which means they are unlikely to ever make the list of the few thousand most popular
data science libraries supported by Anaconda.
This is where the [Anaconda Cloud](https://anaconda.org) comes in.
Developers of PyAOS libraries can contribute a conda installation package to that site,
which is essentially a set of instructions that conda can use to install the library.
Many of your favorite PyAOS packages will suggest that you install their library
using a conda installation package that they've uploaded to Anaconda Cloud.

<div class="callout callout--info">
    <p><strong>Pangeo</strong></p>
    <p>Anaconda has got you covered for installing the PyAOS stack
    on a Windows, Mac or Linux computer.
    If you're working with big data on a HPC system or cloud cluster,
    the <a href="https://pangeo.io/index.html">Pangeo</a> project
    has additional information and resources for getting the PyAOS stack up and running. 
    </p>
</div>



 

 