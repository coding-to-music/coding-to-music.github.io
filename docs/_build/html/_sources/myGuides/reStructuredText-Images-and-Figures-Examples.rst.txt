reStructuredText Images and Figures Examples
================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:


Try and reduce the 

❌ Bad:
   Things that don't work yet


And get more of the good

✅ Good:
   Things that work



 Images
--------

There are two image directives: "image" and "figure".


Image
--------------

:Directive Type: "image"
:Doctree Element: image_
:Directive Arguments: One, required (image URI).
:Directive Options: Possible.
:Directive Content: None.

An "image" is a simple picture::

    .. image:: picture.png

Inline images can be defined with an "image" directive in a `substitution
definition`_

The URI for the image source file is specified in the directive
argument.  As with hyperlink targets, the image URI may begin on the
same line as the explicit markup start and target name, or it may
begin in an indented text block immediately following, with no
intervening blank lines.  If there are multiple lines in the link
block, they are stripped of leading and trailing whitespace and joined
together.

Optionally, the image link block may contain a flat field list, the
_`myimage options`.  For example::

    .. image:: picture.jpeg
       :height: 100px
       :width: 200 px
       :scale: 50 %
       :alt: alternate text
       :align: right

The following options are recognized:

``alt`` : text
    Alternate text: a short description of the image, displayed by
    applications that cannot display images, or spoken by applications
    for visually impaired users.

``height`` : `length`_
    The desired height of the image.
    Used to reserve space or scale the image vertically.  When the "scale"
    option is also specified, they are combined.  For example, a height of
    200px and a scale of 50 is equivalent to a height of 100px with no scale.

``width`` : `length`_ or `percentage`_ of the current line width
    The width of the image.
    Used to reserve space or scale the image horizontally.  As with "height"
    above, when the "scale" option is also specified, they are combined.

``scale`` : integer percentage (the "%" symbol is optional)
    The uniform scaling factor of the image.  The default is "100Â %", i.e.
    no scaling.

    If no "height" or "width" options are specified, the `Python
    Imaging Library`_ (PIL/Pillow_) may be used to determine them, if
    it is installed and the image file is available.

``align`` : "top", "middle", "bottom", "left", "center", or "right"
    The alignment of the image, equivalent to the HTML ``<img>`` tag's
    deprecated "align" attribute or the corresponding "vertical-align" and
    "text-align" CSS properties.
    The values "top", "middle", and "bottom"
    control an image's vertical alignment (relative to the text
    baseline); they are only useful for inline images (substitutions).
    The values "left", "center", and "right" control an image's
    horizontal alignment, allowing the image to float and have the
    text flow around it.  The specific behavior depends upon the
    browser or rendering software used.

``target`` : text (URI or reference name)
    Makes the image into a hyperlink reference ("clickable").  The
    option argument may be a URI (relative or absolute), or a
    `reference name`_ with underscore suffix (e.g. ```a name`_``).

and the common options `:class:`_ and `:name:`_.


Figure
--------------


:Directive Type: "figure"
:Doctree Elements: figure_, image_, caption_, legend_
:Directive Arguments: One, required (image URI).
:Directive Options: Possible.
:Directive Content: Interpreted as the figure caption and an optional
                    legend.

A "figure" consists of image_ data (including `myimage options`_), an optional
caption (a single paragraph), and an optional legend (arbitrary body
elements). For page-based output media, figures might float to a different
position if this helps the page layout.
::

    .. figure:: picture.png
       :scale: 50 %
       :alt: map to buried treasure

       This is the caption of the figure (a simple paragraph).

       The legend consists of all elements after the caption.  In this
       case, the legend consists of this paragraph and the following
       table:

       +-----------------------+-----------------------+
       | Symbol                | Meaning               |
       +=======================+=======================+
       | .. image:: tent.png   | Campground            |
       +-----------------------+-----------------------+
       | .. image:: waves.png  | Lake                  |
       +-----------------------+-----------------------+
       | .. image:: peak.png   | Mountain              |
       +-----------------------+-----------------------+

There must be blank lines before the caption paragraph and before the
legend.  To specify a legend without a caption, use an empty comment
("..") in place of the caption.

The "figure" directive supports all of the options of the "image"
directive (see `myimage options`_ above). These options (except
"align") are passed on to the contained image.

``align`` : "left", "center", or "right"
    The horizontal alignment of the figure, allowing the image to
    float and have the text flow around it.  The specific behavior
    depends upon the browser or rendering software used.

In addition, the following options are recognized:

``figwidth`` : "image", length_, or percentage_ of current line width
    The width of the figure.
    Limits the horizontal space used by the figure.
    A special value of "image" is allowed, in which case the
    included image's actual width is used (requires the `Python Imaging
    Library`_). If the image file is not found or the required software is
    unavailable, this option is ignored.

    Sets the "width" attribute of the "figure" doctree element.

    This option does not scale the included image; use the "width"
    `image`_ option for that. ::

        +---------------------------+
        |        figure             |
        |                           |
        |<------ figwidth --------->|
        |                           |
        |  +---------------------+  |
        |  |     image           |  |
        |  |                     |  |
        |  |<--- width --------->|  |
        |  +---------------------+  |
        |                           |
        |The figure's caption should|
        |wrap at this width.        |
        +---------------------------+

``figclass`` : text
    Set a `"classes"`_ attribute value on the figure element.  See the
    class_ directive below.

.. _Python Imaging Library: 
    https://en.wikipedia.org/wiki/Python_Imaging_Library
.. _Pillow: https://pypi.org/project/Pillow/





Image
---------------------------------------------------------------------


An "image" is a simple picture::

    .. image:: ../static/yi_jing_01_chien.jpg

.. image:: ../static/yi_jing_01_chien.jpg

Inline images can be defined with an "image" directive in a `substitution
definition`_

The URI for the image source file is specified in the directive
argument.  As with hyperlink targets, the image URI may begin on the
same line as the explicit markup start and target name, or it may
begin in an indented text block immediately following, with no
intervening blank lines.  If there are multiple lines in the link
block, they are stripped of leading and trailing whitespace and joined
together.

Example 1 Right 30% scale
---------------------------------------------------------------------

Optionally, the image link block may contain a flat field list, the
_`image options`.  For example::

    .. image:: ../static/yi_jing_01_chien.jpg
       :height: 100 %
       :width: 100 %
       :scale: 10 cm
       :alt: alternate text
       :align: right

.. image:: ../static/yi_jing_01_chien.jpg
    :scale: 30 %
    :alt: alternate text
    :align: right


Example 2 Right 50% width
---------------------------------------------------------------------

Here is another image example 

    .. image:: ../static/yi_jing_01_chien.jpg
       :width: 50 %
       :alt: alternate text
       :align: right


.. figure:: ../static/yi_jing_01_chien.jpg
  :width: 50 %
  :alt: alternate text
  :align: right

  Here is a caption or empty text ".."

  Inner Legend 

"Outer Caption here"

There must be blank lines before the caption paragraph and before the
legend.  To specify a legend without a caption, use an empty comment
("..") in place of the caption.

Example 3 Left 50% width
---------------------------------------------------------------------

.. figure:: ../static/yi_jing_01_chien.jpg
  :width: 50 %
  :alt: alternate text
  :align: left

  Here is a caption or empty text ".."

  Legend 

Example 4 Centered 80% width 
---------------------------------------------------------------------

.. figure:: ../static/yi_jing_01_chien.jpg
  :width: 80 %
  :alt: alternate text
  :align: center

  Here is a caption or empty text ".."

  Legend 

Example 5 Centered 100% width 
---------------------------------------------------------------------

.. figure:: ../static/yi_jing_01_chien.jpg
  :width: 100 %
  :alt: alternate text
  :align: center

  Here is a caption or empty text ".."

  Legend 

Example 6 
---------------------------------------------------------------------

.. figure:: ../static/yi_jing_01_chien.jpg
  :width: 50 %
  :alt: alternate text
  :align: right

  Here is a caption or empty text ".."

  Legend 

Example 7 
---------------------------------------------------------------------


Common Options
--------------

Most of the directives that generate doctree elements support the following
options:

.. _class-option:

_`:class:` : text
    Set a `"classes"`_ attribute value on the doctree element generated by
    the directive. See also the class_ directive.

_`:name:` : text
    Add `text` to the `"names"`_ attribute of the doctree element generated
    by the directive. This allows `hyperlink references`_ to the element
    using `text` as `reference name`_.

    Specifying the `name` option of a directive, e.g., ::

      .. image:: bild.png
         :name: my picture

    is a concise syntax alternative to preceding it with a `hyperlink
    target`_ ::

      .. _my picture:

      .. image:: bild.png

    New in Docutils 0.8.



``figclass`` : text
    Set a `"classes"`_ attribute value on the figure element.  See the
    class_ directive below.

.. _Python Imaging Library: 
    https://en.wikipedia.org/wiki/Python_Imaging_Library
.. _Pillow: https://pypi.org/project/Pillow/

.. _reference name:
.. _reference names: restructuredtext.html#reference-names
.. _hyperlink target: restructuredtext.html#hyperlink-targets
.. _hyperlink references: restructuredtext.html#hyperlink-references
.. _class names: ../doctree.html#classnames-type
.. _"classes": ../doctree.html#classes
.. _identifier keys: ../doctree.html#ids-type
.. _"ids": ../doctree.html#ids
.. _"names": ../doctree.html#names
.. _admonition: ../doctree.html#admonition
.. _block_quote: ../doctree.html#block-quote
.. _caption: ../doctree.html#caption
.. _compound: ../doctree.html#compound
.. _container element: ../doctree.html#container
.. _decoration: ../doctree.html#decoration
.. _figure: ../doctree.html#figure
.. _footnote: ../doctree.html#footnote
.. _footnote_reference: ../doctree.html#footnote-reference
.. _generated: ../doctree.html#generated
.. _image: ../doctree.html#image
.. _inline elements: ../doctree.html#inline-elements
.. _interpreted text role: roles.html
.. _literal_block: ../doctree.html#literal-block
.. _legend: ../doctree.html#legend
.. _length: restructuredtext.html#length-units
.. _line_block: ../doctree.html#line-block
.. _math_block: ../doctree.html#math-block
.. _pending: ../doctree.html#pending
.. _percentage: restructuredtext.html#percentage-units
.. _raw: ../doctree.html#raw
.. _rubric: ../doctree.html#rubric
.. _sidebar: ../doctree.html#sidebar
.. _table: ../doctree.html#table
.. _title: ../doctree.html#title
.. _topic: ../doctree.html#topic
.. _substitution definition:


.. _classes:

Class
=====

:Directive Type: "class"
:Doctree Element: pending_
:Directive Arguments: One or more, required (class names / attribute
                      values).
:Directive Options: None.
:Directive Content: Optional.  If present, it is interpreted as body
                    elements.

The "class" directive sets the `"classes"`_ attribute value on its content
or on the first immediately following [#]_ non-comment element [#]_.
The directive argument consists of one or more space-separated class
names. The names are transformed to conform to the regular expression
``[a-z](-?[a-z0-9]+)*`` (see `Identifier Normalization` below).

Examples::

    .. class:: special

    This is a "special" paragraph.

    .. class:: exceptional remarkable

    An Exceptional Section
    ======================

    This is an ordinary paragraph.

    .. class:: multiple

       First paragraph.

       Second paragraph.

The text above is parsed and transformed into this doctree fragment::

    <paragraph classes="special">
        This is a "special" paragraph.
    <section classes="exceptional remarkable">
        <title>
            An Exceptional Section
        <paragraph>
            This is an ordinary paragraph.
        <paragraph classes="multiple">
            First paragraph.
        <paragraph classes="multiple">
            Second paragraph.


.. [#] This is also true, if the class directive is "nested" at the end of
   an indented text block, for example::

       .. note:: the class values set in this directive-block do not apply to
          the note but the next paragraph.

          .. class:: special

       This is a paragraph with class value "special".

   This allows the "classification" of individual list items (except the
   first, as a preceding class directive applies to the list as a whole)::

       * bullet list

         .. class:: classy item

       * second item, with class argument

.. [#] To set a "classes" attribute value on a block quote, the
   "class" directive must be followed by an empty comment::

       .. class:: highlights
       ..

           Block quote text.

   Without the empty comment, the indented text would be interpreted as the
   "class" directive's content, and the classes would be applied to each
   element (paragraph, in this case) individually, instead of to the block
   quote as a whole.



Identifier Normalization
~~~~~~~~~~~~~~~~~~~~~~~~

Docutils `class names`_ and `identifier keys`_ are normalized to conform
to the regular expression "``[a-z](-?[a-z0-9]+)*``" by converting

* alphabetic characters to lowercase,
* accented characters to the base character,
* non-alphanumeric characters to hyphens,
* consecutive hyphens into one hyphen

and stripping

* leading hyphens and number characters, and
* trailing hyphens.

For example ``"Rot.Gelb&GrÃ¼n:+2008"`` becomes ``"rot-gelb-grun-2008"`` and
``"1000_Steps!"`` becomes ``"steps"``.

.. topic:: Rationale:

    Identifier keys must be valid in all supported output formats.

    For HTMLÂ 4.1 + CSS1 compatibility, identifiers should have no
    underscores, colons, or periods.  Hyphens may be used.

    - The `HTML 4.01 spec`_ defines identifiers based on SGML tokens:

          ID and NAME tokens must begin with a letter ([A-Za-z]) and
          may be followed by any number of letters, digits ([0-9]),
          hyphens ("-"), underscores ("_"), colons (":"), and periods
          (".").

          -- http://www.w3.org/TR/html401/types.html#type-name

    - The `CSS1 spec`_ defines identifiers based on the "name" token
      ("flex" tokenizer notation below; "latin1" and "escape" 8-bit
      characters have been replaced with XML entities)::

          unicode     \\[0-9a-f]{1,4}
          latin1      [&iexcl;-&yuml;]
          escape      {unicode}|\\[ -~&iexcl;-&yuml;]
          nmchar      [-A-Za-z0-9]|{latin1}|{escape}
          name        {nmchar}+

    The CSS1 rule requires underscores ("_"), colons (":"), and
    periods (".") to be escaped [#]_,
    therefore `"classes"`_ and `"ids"`_ attributes should not
    contain these characters.  Combined with HTML4.1 requirements (the
    first character must be a letter; no "unicode", "latin1", or
    "escape" characters), this results in the regular expression
    ``[A-Za-z][-A-Za-z0-9]*``. Docutils adds a normalization by
    downcasing and merge of consecutive hyphens.

    .. [#] CSS identifiers may use underscores ("_") directly in
       `CSSÂ LevelÂ 1`__, `CSS2.1`__, CSS2.2__, and CSS3__.

       __ https://www.w3.org/TR/CSS21/syndata.html#value-def-identifier
       __ https://www.w3.org/TR/CSS/#css-level-1
       __ https://www.w3.org/TR/CSS22/syndata.html
       __ https://www.w3.org/TR/css-syntax-3/#typedef-ident-token

    .. _HTML 4.01 spec: http://www.w3.org/TR/html401/
    .. _CSS1 spec: http://www.w3.org/TR/REC-CSS1

.. _role:



Last change: |today|