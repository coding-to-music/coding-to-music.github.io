Limitation
==========

.. Note:: 
    
    This page was Retrieved and copied April 16 2021
    
    https://github.com/bareos/blob/master/docs/manuals/bareos/BareosSpecificFormatting/Limitation.rst



If you want to point out a limitation in the Bareos functionality, the following formatting should be used::

   .. limitation:: <Component>: <Short description>

      Long description,
      can contain multiple lines.

Besides showing this text, the limitation markup will also create indices.

The short description should be as short as possible, as it will get part of the index.

Example:

.. literalinclude:: /bareos/example/limitation-example.rst.inc
   :language: none

This will be displayed as:

.. include:: /bareos/example/limitation-example.rst.inc

Last change: |today|