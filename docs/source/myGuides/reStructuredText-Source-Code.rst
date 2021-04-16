reStructuredText: Source Code Blocks
=======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:





Source Code
-----------

Source code will be formatted by the directive ``code-block``.

Example::

   .. code-block:: sh
      :caption: CaptionHere

      Line 1
      Line 2
      ...

Output:

.. code-block:: sh
   :caption: CaptionHere

   Line 1
   Line 2
   ...



Valid values for the highlighting language are:

  * ``none`` (no highlighting)
  * ``python`` (the default)
  * ``bareosconfig`` (Bareos configuration files or parts thereof)
  * ``bconsole`` (Bareos console (bconsole) sessions)
  * ``bareoslog`` (Bareos log files)
  * ``bareosmessage`` (Bareos messages)
  * ``sh`` (Shell scripts)
  * ``shell-session`` (Shell sessions)
  * ``dosbatch`` (DOS/Windows Batch file)
  * ``doscon`` (MSDOS sessions)
  * ``cfg`` (Generic configuration file, mostly INI files)
  * ``sql`` (Generic SQL commands)
  * ``registry`` (Windows Registry files produced by regedit)
  * ``guess`` (let Pygments guess the lexer based on contents, only works with
    certain well-recognizable languages)
  * ``rest``
  * ``c``
  * ... and any other `lexer alias that Pygments supports
    <http://pygments.org/docs/lexers/>`_.

If the text resides in a seperate file, use::

   .. literalinclude:: /include/config/backup-client1.cfg
      :language: bareosconfig

All included files should be located under :file:`/include`.

The beginning :file:`/` means, root directory of the documenation source directory.
Without it, the path is relative to the directory of the including file.

Configuration files should be located under :file:`/include/config/`\ .

Last change: |today|