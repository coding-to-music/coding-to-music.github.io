Tech stack for this website
=============================

This site is static content, written in reStructured Text, compiled by Sphinx into HTML pages that are stored on GitHub.io CDN content delivery network.

.. toctree::
    :maxdepth: 2
    :caption: Contents:
 
    

.. contents::
    :local:
  
  
The repository is here
-------------------------

The repository is here:

https://github.com/coding-to-music/coding-to-music.github.io


Here is the directory structure
------------------------------------

Here is the directory structure.::

    vscode ➜ /workspaces/coding-to-music.github.io (master) $ tree -L 3
    .
    ├── README.md                   # this is the readme when visiting the repo
    ├── binder                      # binder is like vscode in the cloud, view pull requests etc
    │   └── environment.yml         # configuration file for binder
    ├── docs                        # docs is the main home for running the make file
    │   ├── Makefile                # make html   or   make PDF   or   make clean
    │   ├── build                   # generated output that can be served
    │   │   ├── doctrees            # generated doctrees stored here
    │   │   └── html                # generated HTML stored here and images, downloads
    │   ├── examples                # used when testing image gallery
    │   │   ├── README.txt
    │   │   ├── test1
    │   │   └── test2
    │   ├── source                  # source is all the rst files (index.rst and site content)
    │   │   ├── Help-about          # About this site
    │   │   ├── How-you-can-help    # How you can get involved
    │   │   ├── License             # Open source license
    │   │   ├── Sandbox             # stuff I am working on 
    │   │   ├── __pycache__         # generated temporary cache
    │   │   ├── _ext                # extensions
    │   │   ├── _extensions         # extensions
    │   │   ├── _html
    │   │   ├── _images             # relatively unchanging assets (in build this is all generated images)
    │   │   ├── _static             # relatively unchanging assets
    │   │   ├── assets              # all the images
    │   │   ├── auto_examples       # used when testing image gallery
    │   │   ├── bareos              # excellent well-made docs examples
    │   │   ├── conf.py             # all the important settings this is a executed program actually
    │   │   ├── css                 # overrides go here
    │   │   ├── dcma                # DCMA takedown policy
    │   │   ├── examples            # used when testing image gallery
    │   │   ├── generated           # used when testing image gallery
    │   │   ├── index.rst           # landing page of the site
    │   │   ├── myGuides            # my documentation of how to do things
    │   │   ├── requirements.txt    # all the needed extensions`
    │   │   ├── static              # relatively unchanging assets
    │   │   ├── test_py_module      # sandbox item
    │   │   └── topics              # main location of content


requirements.txt is all the software that must be installed via pip (automatically)
--------------------------------------------------------------------------------------

To manually install the required python extensions referenced by requirements.txt 

.. code:: bash 

    pip install -r requirements.txt


.. include:: /requirements.txt.inc
    :number-lines: 1-100



To add content
----------------

To add content:

- add or modify a .rst file in the docs/source/ directory
- in the docs directory 'make html'
- in the main top-level directory push the change to github 'git push' 
- Then a webhook will send to ReadTheDocs which will do a build on their system https://readthedocs.org/projects/pandemic-overview/builds/
- And it will be promoted to https://pandemic-overview.readthedocs.io/
- http://all-knowledge.info points to https://pandemic-overview.readthedocs.io/

Key Technologies
------------------

Key Technologies

- GitHub      https://github.com/coding-to-music
- Sphinx      https://www.sphinx-doc.org/en/master/
- ReadTheDocs https://readthedocs.org/
- github.io   https://pages.github.com/
- sphinxext-opengraph https://pypi.org/project/sphinxext-opengraph/
  


Last change: |today|