Bareos Project - Their Documentation Style Guide
==================================================

This is a complete guide to the language and style conventions used for Bareos Documentation. The Sphinx tool has been used to produce a presentable documentation using the reStructuredText (reST) files present in https://github.com/bareos/bareos/tree/master/docs/manuals/source\ .

The primary output format is HTML.
It is doubtfull, is PDFs can be created easily (internally, Sphinx would convert to Latex first, and than use Latex to create the PDF).

.. toctree::

   /bareos/RestOverview.rst
   /bareos/CommonNames.rst
   /bareos/SpecificFormatting.rst
   /bareos/BareosSpecificFormatting.rst
   /bareos/Gotchas.rst



Last change: |today|