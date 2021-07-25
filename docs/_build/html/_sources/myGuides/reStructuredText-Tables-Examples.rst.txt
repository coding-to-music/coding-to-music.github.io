reStructuredText Tables Examples
================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:


Table
-----

Sphinx offers multiple methods to create tables, see https://www.sphinx-doc.org/en/2.0/usage/restructuredtext/basics.html#tables\ .

Choose whatever sucks least.

For simple tables :rst:dir:`csv-table` is a good choice.

Example:

.. literalinclude:: /bareos/example/csv-table.rst.inc
   :language: none

This will be displayed as:

.. include:: /bareos/example/csv-table.rst.inc


.. Note:: 
    
    This page was Retrieved and copied April 15 2021
    https://docutils.sourceforge.io/docs/ref/rst/directives.html


--------
 Tables
--------

Formal tables need more structure than the reStructuredText syntax
supplies.  Tables may be given titles with the table_ directive.
Sometimes reStructuredText tables are inconvenient to write, or table
data in a standard format is readily available.  The csv-table_
directive supports CSV data.


Table
=====

:Directive Type: "table"
:Doctree Element: table_
:Directive Arguments: One, optional (table title).
:Directive Options: Possible (see below).
:Directive Content: A normal reStructuredText table.

(New in Docutils 0.3.1)

The "table" directive is used to associate a
title with a table or specify options, e.g.::

    .. table:: Truth table for "not"
       :widths: auto

       =====  =====
         A    not A
       =====  =====
       False  True
       True   False
       =====  =====

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====


The following options are recognized:

``align`` : "left", "center", or "right"
    The horizontal alignment of the table.
    (New in Docutils 0.13)

``widths`` : "auto", "grid" or a list of integers
    A comma- or space-separated list of column widths.
    The default is the width of the input columns (in characters).

    The special values "auto" or "grid" may be used by writers to decide
    whether to delegate the determination of column widths to the backend
    (LaTeX, the HTML browser, ...).
    See also the `table_style`_ configuration option.

``width`` : `length`_ or `percentage`_ of the current line width
    Forces the width of the table to the specified length or percentage
    of the line width.  If omitted, the renderer determines the width
    of the table based on its contents.

and the common options `:class:`_ and `:name:`_.

.. _table_style: ../../user/config.html#table-style

.. _csv-table:

CSV Table Example
===================

:Directive Type: "csv-table"
:Doctree Element: table_
:Directive Arguments: One, optional (table title).
:Directive Options: Possible (see below).
:Directive Content: A CSV (comma-separated values) table.

.. WARNING::

   The "csv-table" directive's ":file:" and ":url:" options represent
   a potential security holes.  They can be disabled with the
   "file_insertion_enabled_" runtime setting.

(New in Docutils 0.3.4)

The "csv-table" directive is used to create a table from CSV
(comma-separated values) data.  CSV is a common data format generated
by spreadsheet applications and commercial databases.  The data may be
internal (an integral part of the document) or external (a separate
file).

Example::

    .. csv-table:: Frozen Delights!
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30

       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"


.. csv-table:: Frozen Delights!
    :header: "Treat", "Quantity", "Description"
    :widths: 15, 10, 30

    "Albatross", 2.99, "On a stick!"
    "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
    crunchy, now would it?"
    "Gannet Ripple", 1.99, "On a stick!"

Block markup and inline markup within cells is supported.  Line ends
are recognized within cells.

Working limitations:

* There is no support for checking that the number of columns in each
  row is the same.  However, this directive supports CSV generators
  that do not insert "empty" entries at the end of short rows, by
  automatically adding empty entries.

  .. Add "strict" option to verify input?

.. [#whitespace-delim] Whitespace delimiters are supported only for external
   CSV files.

.. [#ASCII-char] With PythonÂ 2, the valuess for the ``delimiter``,
   ``quote``, and ``escape`` options must be ASCII characters. (The csv
   module does not support Unicode and all non-ASCII characters are
   encoded as multi-byte utf-8 string). This limitation does not exist
   under PythonÂ 3.

The following options are recognized:

``widths`` : integer [, integer...] or "auto"
    A comma- or space-separated list of relative column widths.  The
    default is equal-width columns (100%/#columns).

    The special value "auto" may be used by writers to decide
    whether to delegate the determination of column widths to the backend
    (LaTeX, the HTML browser, ...).

``width`` : `length`_ or `percentage`_ of the current line width
    Forces the width of the table to the specified length or percentage
    of the line width.  If omitted, the renderer determines the width
    of the table based on its contents.

``header-rows`` : integer
    The number of rows of CSV data to use in the table header.
    Defaults to 0.

``stub-columns`` : integer
    The number of table columns to use as stubs (row titles, on the
    left).  Defaults to 0.

``header`` : CSV data
    Supplemental data for the table header, added independently of and
    before any ``header-rows`` from the main CSV data.  Must use the
    same CSV format as the main CSV data.

``file`` : string (newlines removed)
    The local filesystem path to a CSV data file.

``url`` : string (whitespace removed)
    An Internet URL reference to a CSV data file.

``encoding`` : name of text encoding
    The text encoding of the external CSV data (file or URL).
    Defaults to the document's encoding (if specified).

``delim`` : char | "tab" | "space" [#whitespace-delim]_
    A one-character string\ [#ASCII-char]_ used to separate fields.
    Defaults to ``,`` (comma).  May be specified as a Unicode code
    point; see the unicode_ directive for syntax details.

``quote`` : char
    A one-character string\ [#ASCII-char]_ used to quote elements
    containing the delimiter or which start with the quote
    character.  Defaults to ``"`` (quote).  May be specified as a
    Unicode code point; see the unicode_ directive for syntax
    details.

``keepspace`` : flag
    Treat whitespace immediately following the delimiter as
    significant.  The default is to ignore such whitespace.

``escape`` : char
    A one-character\ [#ASCII-char]_ string used to escape the
    delimiter or quote characters.  May be specified as a Unicode
    code point; see the unicode_ directive for syntax details.  Used
    when the delimiter is used in an unquoted field, or when quote
    characters are used within a field.  The default is to double-up
    the character, e.g. "He said, ""Hi!"""

    .. Add another possible value, "double", to explicitly indicate
       the default case?

``align`` : "left", "center", or "right"
    The horizontal alignment of the table.
    (New in Docutils 0.13)

and the common options `:class:`_ and `:name:`_.


List Table
==========

:Directive Type: "list-table"
:Doctree Element: table_
:Directive Arguments: One, optional (table title).
:Directive Options: Possible (see below).
:Directive Content: A uniform two-level bullet list.

(New in Docutils 0.3.8.  This is an initial implementation; `further
ideas`__ may be implemented in the future.)

__ ../../dev/rst/alternatives.html#list-driven-tables

The "list-table" directive is used to create a table from data in a
uniform two-level bullet list.  "Uniform" means that each sublist
(second-level list) must contain the same number of list items.

Example::

    .. list-table:: Frozen Delights!
       :widths: 15 10 30
       :header-rows: 1

       * - Treat
         - Quantity
         - Description
       * - Albatross
         - 2.99
         - On a stick!
       * - Crunchy Frog
         - 1.49
         - If we took the bones out, it wouldn't be
           crunchy, now would it?
       * - Gannet Ripple
         - 1.99
         - On a stick!

The following options are recognized:

``widths`` : integer [integer...] or "auto"
    A comma- or space-separated list of relative column widths.  The
    default is equal-width columns (100%/#columns).

    The special value "auto" may be used by writers to decide
    whether to delegate the determination of column widths to the backend
    (LaTeX, the HTML browser, ...).

``width`` : `length`_ or `percentage`_ of the current line width
    Forces the width of the table to the specified length or percentage
    of the line width.  If omitted, the renderer determines the width
    of the table based on its contents.

``header-rows`` : integer
    The number of rows of list data to use in the table header.
    Defaults to 0.

``stub-columns`` : integer
    The number of table columns to use as stubs (row titles, on the
    left).  Defaults to 0.

``align`` : "left", "center", or "right"
    The horizontal alignment of the table.
    (New in Docutils 0.13)

and the common options `:class:`_ and `:name:`_.



Last change: |today|