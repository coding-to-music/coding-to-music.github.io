reStructuredText: References and Footnotes Examples
=======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:



Hyperlinks
----------

External links
~~~~~~~~~~~~~~

Use ```Link text <http://target>`_`` for inline web links.  If the link text
should be the web address, you don't need special markup at all, the parser
finds links and mail addresses in ordinary text.

Example:

.. literalinclude:: /bareos/example/urls.rst.inc
   :language: none

Output:

.. include:: /bareos/example/urls.rst.inc


Internal links
~~~~~~~~~~~~~~

Internal linking is done via a special reST role, see the section on specific
markup, :ref:`doc-ref-role`.


.. _doc-ref-role:

Cross-linking markup
--------------------

To support cross-referencing to arbitrary sections in the documentation, the standard reST labels are used in a specific way. Every label must precede a section title and every label name must be unique throughout the entire documentation source.

The label must begin with an underscore. Example::

   .. _my-reference-label:

   Section to cross-reference
   --------------------------

   This is the text of the section.

You can reference this section using the ``:ref:`label-name``` role. Remark that the preceding underscore from the label must not be used in the role: ``:ref:`my-reference-label```.

The ``:ref:`` invocation is then replaced with a link to the referred section. The text of the link is the same as the section title.

Alternatively, you can reference any label (not just section titles) if you provide the link text in the role like this: ``:ref:`link text <my-reference-label>``` (`<` and `>` are mandatory).

Manual defined labels should use following naming rules:

   * without spaces
   * without columns (:)

.. warning::

   If the label is not defined immediately before a section title and no link text is given,
   ``:ref:`` will fail and not create a link at all.
   Instead it produces a warning (``WARNING: undefined label: mytestlabel (if the link has no caption the label must precede a section header)``)
   and writes the parameter as plain text.

It is possible, however uncommon,
to define multiple labels before a section header::

   .. _section-feature1:

   .. _section-feature2:

   Section about Feature 1 and Feature 2
   -------------------------------------

   This is the text of the section.



In the Bareos documentation we use the Sphinx extension **sphinx.ext.autosectionlabel**
with the parameter ``autosectionlabel_prefix_document = True``.

With this, all section titles do automatically create a section label.
This causes warnings when there are multiple sections with the same title.
To reduce the number of warnings, the parameter ``autosectionlabel_prefix_document = True`` is set,
This prefix each section label with the name (including the relative path from the top directory) of the document it is in, followed by a colon.

Example::

  :ref:`bareos/RestOverview:Cross-linking markup`

This will link to :ref:`bareos/RestOverview:Cross-linking markup`\ .





Last change: |today|