Tech stack for this website
=============================

This site is static content, written in reStructured Text, compiled by Sphinx into HTML pages that are stored on GitHub.io CDN content delivery network.

To add content, add or modify a .rst file

in the docs directory 'make html'

in the main directory push the change to github 

Then a webhook will send to ReadTheDocs which will do a build on their system https://readthedocs.org/projects/pandemic-overview/builds/

And it will be promoted to https://pandemic-overview.readthedocs.io/

Key Technologies

- Sphinx      https://www.sphinx-doc.org/en/master/
- ReadTheDocs https://readthedocs.org/
- github.io   https://pages.github.com/
- sphinxext-opengraph https://pypi.org/project/sphinxext-opengraph/
  
.. toctree::
    :maxdepth: 2
    :caption: Contents:
 
    OpenGraph Object Sharing Image Preview System
    


Last change: |today|