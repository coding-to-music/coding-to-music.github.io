test1
=====

This is test1

For further information, please visit
https://github.com/coding-to-music

.. figure:: assets/1985-vaccine-usage.jpg
   :scale: 50 %
   :alt: map to buried treasure

.. attention::
   Begin Grid table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

.. attention::
   Begin Simple table:

=====  =====  ========
   Inputs     Output
------------  --------
  A      B    A or B
=====  =====  ========
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ========

.. DANGER::
   Beware killer rabbits!

.. attention::
   attention here

.. caution::
   caution here

.. danger::
   danger here

.. error::
   error here

.. hint::
   hint here

.. important::
   important here

.. note::
   note here

.. tip::
   tip here

.. warning::
   warning here

.. admonition:: admonition here 

   you can make your own admonition here


A transition marker is a horizontal line
of 4 or more repeated punctuation
characters.

------------

A transition should not begin or end a
section or document, nor should two
transitions be immediately adjacent.



   This is the caption of the figure (a simple paragraph).

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph and the following
   table:

   .. attention::
      Begin Table 1

   +-----------------------+-----------------------+
   | Symbol                | Meaning               |
   +=======================+=======================+
   | .. image:: assets/icons/favicon-32x32.png   | Campground            |
   +-----------------------+-----------------------+
   | .. image:: assets/icons/favicon-32x32.png  | Lake                  |
   +-----------------------+-----------------------+
   | .. image:: assets/icons/favicon-32x32.png   | Mountain              |
   +-----------------------+-----------------------+

   End Table 1

This format is the most natural and obvious. It was independently invented (no great feat of creation!), and later found to be the format supported by the Emacs table mode:

.. attention::
   Begin Table 2

+------------+------------+------------+--------------+
|  Header 1  |  Header 2  |  Header 3  |  Header 4    |
+============+============+============+==============+
|  Column 1  |  Column 2  | Column 3 & 4 span (Row 1) |
+------------+------------+------------+--------------+
|    Column 1 & 2 span    |  Column 3  | - Column 4   |
+------------+------------+------------+ - Row 2 & 3  |
|      1     |      2     |      3     | - span       |
+------------+------------+------------+--------------+

End Table 2

Tables are described with a visual outline made up of the characters '-', '=', '|', and '+':

The hyphen ('-') is used for horizontal lines (row separators).
The equals sign ('=') is optionally used as a header separator (as of version 1.5.24, this is not supported by the Emacs table mode).
The vertical bar ('|') is used for for vertical lines (column separators).
The plus sign ('+') is used for intersections of horizontal and vertical lines.
Row and column spans are possible simply by omitting the column or row separators, respectively. The header row separator must be complete; in other words, a header cell may not span into the table body. Each cell contains body elements, and may have multiple paragraphs, lists, etc. Initial spaces for a left margin are allowed; the first line of text in a cell determines its left margin.


Below is a simpler table structure. It may be better suited to manual input than alternative #1, but there is no Emacs editing mode available. One disadvantage is that it resembles section titles; a one-column table would look exactly like section & subsection titles.

.. attention::
   Begin Table 3

============ ============ ============ ==============
  Header 1     Header 2     Header 3     Header 4
============ ============ ============ ==============
  Column 1     Column 2    Column 3 & 4 span (Row 1)
------------ ------------ ---------------------------
    Column 1 & 2 span      Column 3    - Column 4
------------------------- ------------ - Row 2 & 3
      1            2       3           - span
============ ============ ============ ==============

End Table 3

The table begins with a top border of equals signs with a space at each column boundary (regardless of spans). Each row is underlined. Internal row separators are underlines of '-', with spaces at column boundaries. The last of the optional head rows is underlined with '=', again with spaces at column boundaries. Column spans have no spaces in their underline. Row spans simply lack an underline at the row boundary. The bottom boundary of the table consists of '=' underlines. A blank line is required following a table.

A minimalist alternative is as follows:

.. attention::
   Begin Table 4


+====  =====  ========  ========  =======  ====  =====  =====+
Old State    Input     Action             New State    Notes
+-----------  --------  -----------------  -----------+
ids   types  new type  sys.msg.  dupname  ids   types
+====  =====  ========  ========  =======  ====  =====  =====+
--    --     explicit  --        --       new   True
--    --     implicit  --        --       new   False
None  False  explicit  --        --       new   True
old   False  explicit  implicit  old      new   True
None  True   explicit  explicit  new      None  True
old   True   explicit  explicit  new,old  None  True   [1]
None  False  implicit  implicit  new      None  False
old   False  implicit  implicit  new,old  None  False
None  True   implicit  implicit  new      None  True
old   True   implicit  implicit  new      old   True
=========================================================

End Table 4

There are three forms of hyperlink currently in StructuredText:

(Absolute & relative URIs.) Text enclosed by double quotes followed by a colon, a URI, and concluded by punctuation plus white space, or just white space, is treated as a hyperlink:

"Python":http://www.python.org/
(Absolute URIs only.) Text enclosed by double quotes followed by a comma, one or more spaces, an absolute URI and concluded by punctuation plus white space, or just white space, is treated as a hyperlink:

"mail me", mailto:me@mail.com
(Endnotes.) Text enclosed by brackets link to an endnote at the end of the document: at the beginning of the line, two dots, a space, and the same text in brackets, followed by the end note itself:

Please refer to the fine manual [GVR2001].

.. [GVR2001] Python Documentation, Release 2.1, van Rossum,
   Drake, et al., http://www.python.org/doc/

The problem with forms 1 and 2 is that they are neither intuitive nor unobtrusive (they break design goals 5 & 2). They overload double-quotes, which are too often used in ordinary text (potentially breaking design goal 4). The brackets in form 3 are also too common in ordinary text (such as [nested] asides and Python lists like [12]).

===============
 Section Title 1
===============

---------------
 Section Title 2
---------------

Section Title 3
=============

Section Title 4
-------------

Section Title 5
`````````````

Section Title 6
'''''''''''''

Section Title 7
.............

Section Title 8
~~~~~~~~~~~~~

Section Title 9
*************

Section Title 10
+++++++++++++

Section Title 11
^^^^^^^^^^^^^