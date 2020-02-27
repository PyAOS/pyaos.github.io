# PyAOS community website

This website provides documentation and resources for people working with Python in the atmosphere and ocean sciences.

## Site notes

Jekyll theme: [Doks](https://jekyllthemes.io/theme/doks-documentation-jekyll-theme)  
Favicon: [World map](https://favicon.io/emoji-favicons/world-map/) 

## Contributing

#### Changes to existing pages
The content for each page of the website exists as a markdown file in the root directory.
Contributors are encouraged to submit pull requests with suggested changes to those markdown files.
Those less familiar with GitHub can create a new [issue](https://github.com/PyAOS/pyaos.github.io/issues) instead.

> **Previewing your changes**  
> If you'd like to preview how your changes will look on the web before submitting a pull request,
> run `jekyll serve` in the root directory of your forked repository.
> Installation instructions for Jekyll can be found [here](https://jekyllrb.com/docs/installation/).

#### Adding new pages and/or making changes to website layout
New pages can be added using `default.md` as a template.
The new page will then need to be referenced in `_config.yml` and `index.md`.
The [Doks documentation](https://doks.themejack.com/blue/) provides more details if required.

#### Figures
[`images/pyaos-stack.png`](https://github.com/PyAOS/pyaos.github.io/blob/master/images/pyaos-stack.png) was created at [draw.io](https://www.draw.io/). Open [`images/pyaos-stack.xml`](https://github.com/PyAOS/pyaos.github.io/blob/master/images/pyaos-stack.xml) at draw.io to edit that figure.

## Scope

One of the main features of the PyAOS website is the listings of packages and training resources.
The intention is for the community to submit updates to these listings via this GitHub repository,
so it is important to define the scope of the website.

In general, **the PyAOS website provides information on Python packages and training resources that are unique
to the atmosphere and ocean sciences and of interest to physical data scientists.**
The focus is on packages and resources that are under active development and/or maintenance,
have a non-trivial user-base (i.e. more users than just the author/s) and
are for a general audience.

Following that definition, here are some examples of things that would be out of scope:
* Unidata's [cftime](https://unidata.github.io/cftime/) package:
While certainly of interest to software developers in the AOS space,
physical data scientists don't need to know about it because the packages
they're using are built on top of cftime.
In other words,
physical data scientists won't typically be typing `import cftime`
at the top of their data analysis scripts.
* The [Pangeo tutorial from the 2018 NCAR SEA Conference](https://github.com/pangeo-data/pangeo-tutorial-sea-2018):
While this was no doubt a great tutorial,
it is not under active development/maintenance.
* The [CleF](https://clef.readthedocs.io/en/stable/) package:
While this package is very useful for researchers in Australia who want to search for climate data
on the National Computational Infrastructure in Canberra,
most people in the PyAOS community don't have access to that facility.
In other words, this package isn't for a general audience.
* The [GeoPandas](https://geopandas.org/) package: While this is a great package for working with geospatial vector data,
it is of interest to the much broader field of geospatial data science.
In other words, it isn't unique (or even predominantly used by or supported by) the PyAOS community.

If you're unsure whether a particular Python package or training resource is within scope,
feel free to [open an issue](https://github.com/PyAOS/pyaos.github.io/issues)
to start a discussion.
