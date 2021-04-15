reStructuredText: Sections and Headings
=======================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:



Sections
--------

Section headers are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text:

::

   #################
   This is a heading
   #################

Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings.

Our convention is to use them in this order:

* ``#`` with overline, for parts
* ``=`` for chapters
* ``-``, for sections
* ``~``, for subsections
* ``^``, for subsubsections
* ``'``, for paragraphs

::

   ####
   Part
   ####

   Chapter
   =======

   Section
   -------

   Subsection
   ~~~~~~~~~~

   Subsubsection
   ^^^^^^^^^^^^^

   Paragraph
   '''''''''


This convention has be introduced from the conversion of the original LaTex source to reST,
as :program:`pandoc` has created reST file with this section markers (except of parts, which are not created at all).

The part section header is not used at all by us.

All our regular documents starts with a section heading underlined by  ``=``.

Therefore the specific names part, chapter, section ... might not match the actual context. Generally we speak about ''sections'' (or ''section headings'' or ''section markers'').

.. note::

   With reST, there is no leaving out a section level.
   If you write a chapter it is not possible to continue with a paragraph.
   Instead the next section must be of the type section.

   If you try to do it overwise (chapter 1 ``=`` -> paragraph ``'``),
   the ''paragraph'' is treated as a section.
   And if you continue by another chapter (in the same file) (chapter 2 ``=`` -> section ``-``),
   :program:`sphinx-build` got confused and at least produces a warning (`Title level inconsistent`)
   and possibly renders the result incorrectly.


Last change: |today|