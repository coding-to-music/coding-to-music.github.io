## Hello and welcome!!

[cases-vs-deaths-August-2021](https://github.com/coding-to-music/coding-to-music.github.io/blob/master/docs/source/assets/Vaccines/Death-Rates/2021-08-03-USA-covid-cases-vs-deaths-per-day.jpg?raw=true)


August 3, 2021 - USA COVID 'Cases' per Day vs Deaths per Day - two years data 

Source: `'Experts' Move The Goalposts, Declare Herd Immunity Threshold Now 90% Due To Delta August 3, 2021 <https://www.zerohedge.com/covid-19/experts-move-goalposts-declare-herd-immunity-threshold-now-90-due-delta>`_



## Introduction

### This site is full of sincere well-meaning opinion

- This site is full of opinion. We have collected a huge wide variety of items and we attempt to label these items as either True or False.
- We document why it is our opinion, our group consensus, that these items are correctly tagged as either True or False.
- Every item will be able to be tagged so you can either agree or disagree by you tagging the item yourself.
- That feature is not yet ready but you can see we are attempting to make this a community-driven collective-knowledge resource.
- This website will attempt to be kept up-to-date so you can learn what has changed since you last visited.


The content shared here is disputed, **`opinion`**, or may be misleading about COVID-19. To learn more about official COVID-19 public health recommendations visit https://www.cdc.gov/coronavirus/2019-nCoV/index.html

### To learn more about official COVID-19 public health recommendations visit https://www.cdc.gov/coronavirus/2019-nCoV/index.html

## You are free to:

### Share — copy and redistribute the material in any medium or format

### Adapt — remix, transform, and build upon the material for any purpose, even commercially.

This license is acceptable for Free Cultural Works.

The licensor cannot revoke these freedoms as long as you follow the license terms.

https://creativecommons.org/licenses/by/4.0/

Goals:
- Today's date in Eastern Standard Time
- Display a tweet
- Display image gallery

What works:
    And mirror published at https://pandemic-overview.readthedocs.io on each commit via webhook 
    (works)


What does not work:
    This site  published at https://coding-to-music.github.io/ on each commit via the repo settings
    (has not worked in a couple days, see settings, error deploying to github.io )

```java
.. |date| date::
.. |time| date:: %H:%M

Today's date is |date|.

This document was generated on |date| at |time|.

.. |repl_time| date:: %a, %d %b %Y %I:%M %p %Z


Page Built: |repl_time|

This is the substitution called today: |today|
```

------------------

This site  published at https://coding-to-music.github.io/ on each commit via the repo settings
(has not worked in a couple days, see settings, error deploying to github.io )

And mirror published at https://pandemic-overview.readthedocs.io on each commit via webhook 
(works)

https://readthedocs.org/projects/pandemic-overview/builds/

Currently now http://all-knowledge.info is pointing to here

You are looking at this repository https://github.com/coding-to-music/coding-to-music.github.io 

My main repo/profile/README is over here https://github.com/coding-to-music



```java
// put all the files that will be the content of the table of contents here:
// https://coding-to-music.github.io/docs/source/

```

https://pandemic-overview.readthedocs.io/en/latest/Tech%20stack%20for%20this%20website.html

Install sphinx
```javascript
sudo apt-get install python3-sphinx

mkdir project
cd project
sphinx-quickstart .

sudo apt-get install python3-venv
python -m venv ver3.7
source ver3.7/bin/activate
```

How to build:
```java
cd docs
make clean
make html

// common make commands
make clean
make build
make linkcheck

python3 -m http.server

http://localhost:8000/_build/htmlindex.html

// That will use the following file as a source:
// https://coding-to-music.github.io/docs/source/index.rst

// To make the following output file:
// https://coding-to-music.github.io/docs/build/html/index.html

// send it to the remote repo
git add .
git commit -m 'commit message'
git push

//The build process is triggered via a webhook, a commit in this repo causes a GitHub Action which causes ReadTheDocs to rebuild their page
```

View it on 
This is where the website [https://pandemic-overview.readthedocs.io](https://pandemic-overview.readthedocs.io) is hosted from 

The ReadTheDocs control panel [https://readthedocs.org/projects/pandemic-overview/](https://readthedocs.org/projects/pandemic-overview/)

The build process is triggered via a webhook, a commit in this repo causes a GitHub Action which causes ReadTheDocs to rebuild their page

View Live Server so you can view it locally by clicking on the bottom-right status bottom bar of vscode to display a live working version of the html file being edited

Good description of how to set up python for ReStructuredText
https://docs.restructuredtext.net/articles/prerequisites.html#install-python-for-most-features


Instructions for setting up a more recent version of Python are here:
https://linuxize.com/post/how-to-install-python-3-8-on-debian-10/

Interesting website

Let's Treat Docs Like Code

Read stories, learn through practice, share with others.

Sphinx, Jekyll, and Hugo, all are static site generators that teams use for web sites and documentation sites. Let’s go through setting up a static site generator and a common CICD system with it.
https://www.docslikecode.com/learn/

Good description in the Linux kernel documentation for how they advise people to contribute documentation, using reStructuredText 

https://www.kernel.org/doc/html/v4.13/doc-guide/sphinx.html


To embed tweets, install this:
https://pypi.org/project/sphinxcontrib.twitter/#description

```java
pip3 install sphinxcontrib.twitter
```

To install pip3
```java
sudo apt install python3-pip
```

embedding twitter’s tweet in sphinx

usage:

First of all, add sphinx_tweet_embed to sphinx extension list in conf.py

```java
extensions = ['sphinxcontrib.twitter']
```

then use *tweet* directive and *tw* role.

```java
.. tweet:: https://twitter.com/pypi/status/315214320826978305

You can use display-thread flag to display replyes.

.. tweet:: https://twitter.com/pypi/status/315214320826978305

:tw:`@shomah4a`

.. timeline:: 319830355039371264
```
finally, build your sphinx project.

```java
$ make html
```

Cheat Sheets for [Restructured Text (reST) and Syphinx CheatSheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)


https://docutils.sourceforge.io/docs/ref/rst/directives.html

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html


To create a gallery of images, we are using Sphinx Gallery - a Sphinx extension
Sphinx Gallery documentation is here: https://sphinx-gallery.github.io/stable/index.html

Changes made:
- new directory examples
- new file examples/README.rst
- ran pip3 install sphinx-gallery
- requirements.txt
- .readthedocs.yml

Removed from requirements.txt
sphinx_gallery.gen_gallery>=0.8.2
sphinx.ext.autodoc
sphinxcontrib.twitter



https://github.com/sphinx-gallery/sphinx-gallery

```java
pip3 install sphinx-gallery
```
These were in requirements.txt
'sphinx.ext.autodoc',
'sphinx_gallery.gen_gallery',
'sphinxcontrib.twitter'

sphinx.ext.autodoc
sphinx_gallery.gen_gallery
sphinxcontrib.twitter

These were in conf.py
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.twitter'
    'sphinx_gallery.gen_gallery'
    ]

.. code-block:: console

    $ git clone https://github.com/sphinx-gallery/sphinx-gallery
    $ cd sphinx-gallery
    $ pip install -r dev-requirements.txt
    $ pip install -e .



Good overview of documentation with Sphinx
https://coderefinery.github.io/documentation/
https://coderefinery.github.io/documentation/guide/
https://coderefinery.org/

Hosting websites/homepages on GitHub Pages
https://coderefinery.github.io/documentation/06-gh-pages/

https://daler.github.io/sphinxdoc-test/includeme.html

https://daler.github.io/trackhub/
https://github.com/daler/trackhub


Overview of open source collaboration, automated testing, version control, git branching, reproducable research, DevOps Automation, Continuous Integration
https://coderefinery.org/lessons/

Collaborating and sharing using GitHub without command line - using either the GitHub website or GitHub desktop application. Why? Because for many cases, it is enough
https://coderefinery.github.io/github-without-command-line/

Good overview of how modules work in Sphinx
https://stackoverflow.com/questions/53668052/sphinx-cannot-find-my-python-files-says-no-module-named

Carol Willing - Practical Sphinx - PyCon 2018
https://www.youtube.com/watch?v=0ROZRNZkPS8&ab_channel=PyCon2018


Key items to remember
```java
// Important Directives
.. image::
.. warning::
.. code:: bash

.. toctree::
    :titlesonly:
    :caption: Step zero: this is the caption


// Important Variables
_static
_build

// Important files
conf.py             main configuration
.readthedocs.yml    config for promoting to ReadTheDocs
index.rst           main viewing page
```

To view html files
```java
python3 -m http.server
```

This person has examples of how to build locally vs to github
https://github.com/annegentle/create-demo

Came from this article 

https://www.docslikecode.com/articles/github-pages-python-sphinx/

