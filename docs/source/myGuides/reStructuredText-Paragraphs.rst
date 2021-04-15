reStructuredText: Paragraphs
=======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:




Use of whitespace
-----------------

All reST files use an indentation of 3 spaces; no tabs are allowed. The maximum line length is 80 characters for normal text, but tables, deeply indented code samples and long links may extend beyond that. Code example bodies should use normal Python 4-space indentation.

Make generous use of blank lines where applicable; they help group things together.


Sphinx naming
-------------

reST/Sphinx have some specific wording.

Role
~~~~

A role is an inline markup (see :ref:`bareos/RestOverview:Inline markup`\ ). Own roles can be created.
They are used inside other text structures.

Usage::

   :strong:`text`

Output:

   :strong:`text`

Directive
~~~~~~~~~

A directive is an Explicit Markup (see :ref:`bareos/RestOverview:Explicit markup`\ ). Own directives can be created.
Directives are written as a block.

Usage::

   .. directive:: arg1 arg2 ...
      :option1: value
      :option2: value
      :option5: value
      ...

      Multiline content,
      ...

``arg1, arg2, ...``
   Arguments. The last argument can contain spaces (depending on the directive implementation).

``:option1:``
   Options are optional.

Example:

.. literalinclude:: /bareos/example/code-block-bareosconfig.rst.inc
   :language: none

Output:

.. include:: /bareos/example/code-block-bareosconfig.rst.inc


Domain
~~~~~~

A domain is a collection of markup (reStructuredText directives and roles) to describe and link to objects belonging together.



Paragraphs
----------

The paragraph is the most basic block in a reST document.  Paragraphs are simply
chunks of text seperated by one or more blank lines.  As in Python, indentation
is significant in reST, so all lines of the same paragraph must be left-aligned
to the same level of indentation.


Inline markup
-------------

The standard reST inline markup is quite simple: use

* one asterisk: ``*text*`` for emphasis (italics),
* two asterisks: ``**text**`` or ``:strong:`text``` for strong emphasis (boldface), and
* backquotes: ````text```` for code samples.

If asterisks or backquotes appear in running text and could be confused with
inline markup delimiters, they have to be escaped with a backslash.

Be aware of some restrictions of this markup:

* it may not be nested,
* content may not start or end with whitespace: ``* text*`` is wrong,
* it must be seperated from surrounding text by non-word characters.  Use a
  backslash escaped space to work around that: ``thisis\ *one*\ word``.

These restrictions may be lifted in future versions of the docutils.

reST also allows for custom "interpreted text roles"', which signify that the
enclosed text should be interpreted in a specific way.  Sphinx uses this to
provide semantic markup and cross-referencing of identifiers, as described in
the appropriate section.  The general syntax is ``:rolename:`content```.


