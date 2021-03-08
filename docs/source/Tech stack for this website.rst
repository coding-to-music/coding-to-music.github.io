Tech stack for this website
=============================

This site is static content, written in reStructured Text, compiled by Sphinx into HTML pages that are stored on GitHub.io CDN content delivery network.

To add content, add or modify a .rst file

in the docs directory 'make html'

in the main directory push the change to github 

Then a webhook will send to ReadTheDocs which will do a build on their system

And it will be promoted to 

Key Technologies:
- Sphinx
- ReadTheDocs
- github.io
- sphinxext-opengraph 
  


Last change: |today|