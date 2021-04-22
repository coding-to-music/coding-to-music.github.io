Bareos Project - Their Documentation Style Guide
==================================================

.. Note:: 
    
    This page was Retrieved and copied April 11 2021
    
    https://github.com/bareos/blob/bareos-20/docs/manuals/bareos/Introduction


This is a complete guide to the language and style conventions used for Bareos Documentation. The Sphinx tool has been used to produce a presentable documentation using the reStructuredText (reST) files present in https://github.com/bareos/tree/master/docs/manuals/source\ .

The primary output format is HTML.
It is doubtfull, is PDFs can be created easily (internally, Sphinx would convert to Latex first, and than use Latex to create the PDF).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   /bareos/WhatIsBareos
   /bareos/RestOverview
   /bareos/CommonNames
   /bareos/SpecificFormatting
   /bareos/BareosSpecificFormatting
   /bareos/Gotchas
   /bareos/Bareos-conf-py
   /bareos/config-file/index

.. contents::
   :local:




Last change: |today|