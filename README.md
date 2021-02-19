Hello and welcome!!

You are lookating at this repository https://github.com/coding-to-music/coding-to-music.github.io 

My main repo/profile/README is over here https://github.com/coding-to-music

This repo you are looking at is where the website https://pandemic-overview.readthedocs.io is hosted from 

Currently now all-knowledge.info is pointing to here

```java
// put all the files that will be the content of the table of contents here:
// https://coding-to-music.github.io/docs/source/

```

Install sphinx
```javascript
sudo apt-get install python3-sphinx

mkdir project
cd project
sphinx-quickstart .
```

How to build:
```java
cd docs
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