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
    │   │   ├── _static             # relatively unchanging assets that get copied to build such as custom.css
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


here is the current requirements.txt via a literalinclude directive with some random lines emphasized
----------------------------------------------------------------------------------------------------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude

.. code:: java    

    .. literalinclude:: /requirements.txt.inc
        :language: ruby
        :emphasize-lines: 12,15-18
        :linenos:



.. literalinclude:: /requirements.txt
    :language: ruby
    :emphasize-lines: 12,15-18
    :linenos:


DNS and Domain configuration and setup
-----------------------------------------

Three items noted in the documentation https://docs.readthedocs.io/en/stable/custom_domains.html

1. We don’t currently support pointing subdomains or root domains to a project using A records. DNS A records require a static IP address and our IPs may change without notice.
2. For a subdomain like docs.example.com, add a CNAME record in your DNS that points the domain to readthedocs.io.
3. For a root domain like example.com use an ANAME or ALIAS record pointing to readthedocs.io

  
  


.. figure:: /assets/dns-domain-setup/custom-domain-support-documentation.png
  :align: center
  :width: 80 %
  
  ReadTheDocs Custom Domain support documentation

ReadTheDocs Custom Domain support documentation 


.. figure:: /assets/dns-domain-setup/domain-details-data-entry.png
  :align: center
  :width: 80 %
  
  ReadTheDocs Domain Settings

ReadTheDocs Domain Settings


.. figure:: /assets/dns-domain-setup/Unable-to-add-readthedocs.io.png
  :align: center
  :width: 80 %
  
  GoDaddy.com - Unable to add readthedocs.io as an A record

GoDaddy.com - Unable to add readthedocs.io as an A record



To add content
----------------

To add content:

- add or modify a .rst file in the docs/source/ directory
- in the docs directory 'make html'
- in the docs directory push the change to github 'git push' 
- the built objects are not transferred to ReadTheDocs, they only use the changed source files, 
- ReadTheDocs build their own build directory and your one new file in source is built and those build files are added to whatever you aready published. 
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
  

Sphinx Extensions Used for this website, using intersphinx
-------------------------------------------------------------

Example of intersphinx mapping:: 

  intersphinx_mapping = {
      'numpy': ('https://docs.scipy.org/doc/numpy/', None),
      'python': ('https://docs.python.org/3/', None),
      'pydagogue': ('https://matthew-brett.github.io/pydagogue/', None),
      'matplotlib': ('https://matplotlib.org/', None),
      'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
      'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
      'sphinx': ('https://sphinx.readthedocs.io/', None),
      'docutils': ('https://docutils.readthedocs.io/', None),
      'sphinx_rtd_theme': ('https://sphinx_rtd_theme.readthedocs.io/', None),
      'readthedocs-sphinx-ext': ('https://readthedocs-sphinx-ext.readthedocs.io/', None),
      'sphinx_material': ('https://sphinx_material.readthedocs.io/', None),
      'sphinx-panels': ('https://sphinx-panels.readthedocs.io/', None),
      'sphinx-tabs': ('https://sphinx-tabs.readthedocs.io/', None),
      'sphinxcontrib-actdiag': ('https://sphinxcontrib-actdiag.readthedocs.io/', None),
      'sphinxcontrib-blockdiag': ('https://sphinxcontrib-blockdiag.readthedocs.io/', None),
      'sphinxcontrib-contentui': ('https://sphinxcontrib-contentui.readthedocs.io/', None),
      'sphinxcontrib-seqdiag': ('https://sphinxcontrib-seqdiag.readthedocs.io/', None),
      'sphinxcontrib-nwdiag': ('https://sphinxcontrib-nwdiag.readthedocs.io/', None),
      'sphinxcontrib-plantuml': ('https://sphinxcontrib-plantuml.readthedocs.io/', None),
      'sphinx-prompt': ('https://sphinx-prompt.readthedocs.io/', None),
      'sphinxext-remoteliteralinclude': ('https://sphinxext-remoteliteralinclude.readthedocs.io/', None),
      'sphinxext-linkcheckdiff': ('https://sphinxext-linkcheckdiff.readthedocs.io/', None),
      'sphinxnotes-lilypond': ('https://pandas.readthedocs.io/', None),
      'sphinx-Timeline': ('https://sphinx-Timeline.readthedocs.io/', None),
      'sphinx-copybutton': ('https://sphinx-copybutton.readthedocs.io/', None),
      'sphinx-Hoverxref': ('https://sphinx-Hoverxref.readthedocs.io/', None),
      'sphinx_issues': ('https://sphinx_issues.readthedocs.io/', None),
      'sphinx-gallery': ('https://sphinx-gallery.readthedocs.io/', None),
      'sphinxcontrib-images': ('https://sphinxcontrib-images.readthedocs.io/', None),
      'sphinx-gitstamp': ('https://sphinx-gitstamp.readthedocs.io/', None),
      'sphinx-notfound-page': ('https://sphinx-notfound-page.readthedocs.io/', None),
      'sphinxext.rediraffe': ('https://sphinxext.rediraffe.readthedocs.io/', None),
      'sphinx-Sitemap': ('https://github.com/jdillard/sphinx-sitemap', None),
      'sphinx-Jinja': ('https://jinja.palletsprojects.com/en/3.0.x/', None),
  }


:ref:`numpy <numpy:>`    
:ref:`python <python:>`    
:ref:`pydagogue <pydagogue:>`    
:ref:`matplotlib <matplotlib:>`    
:ref:`scipy <scipy:>`    
:ref:`pandas <pandas:>`    
:ref:`sphinx <sphinx:>`    
:ref:`docutils <python:>`    
:ref:`sphinx_rtd_theme <sphinx_rtd_theme:>`    
:ref:`readthedocs-sphinx-ext <readthedocs-sphinx-ext:>`    
:ref:`sphinx_material <sphinx_material:>`    
:ref:`sphinx-panels <sphinx-panels:>`    


Last change: |today|