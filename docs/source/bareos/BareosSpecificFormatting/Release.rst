Releases
========

.. Note:: 
    
    This page was Retrieved and copied April 16 2021
    
    https://github.com/bareos/bareos/blob/master/docs/manuals/source/bareos/BareosSpecificFormatting/Release.rst



Functional Changes
------------------

If the documenation wants to point out,
that a feature has been added
or some functionality changed in a specific version,
use the following role:

If you want to point out a limitation in the Bareos functionality, the following formatting should be used::

   :sinceVersion:`<version>: <Summary>`

version
   Bareos version number, e.g. ''18.2.5''.

Summary
   A short summary.

This role will only display ''Version >= <version>''. The <Summary> will appear only in the index.

The index will contain entries:

* bareos-<version>

  * Summary

and

* Summary

  * bareos-<version>

Example:

.. literalinclude:: /source/bareos/example/sinceVersion-documentation-sphinx.rst.inc
   :language: none

This will be displayed as:

.. include:: /source/bareos/example/sinceVersion-documentation-sphinx.rst.inc


Note
~~~~

``:sinceVersion:`` is a legacy role. Sphinx itself offers

  * https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionadded
  * https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionchanged
  * https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated

Until defined otherwise, you should use ``:sinceVersion:`` instead of these.


Release Notes
-------------

If you want to display the release notes of a Bareos stable release, use the following template:

.. \newcommand{\releasenote}[2]{
    \subsection*{bareos-#1}
    \addcontentsline{toc}{subsection}{\protect\numberline{}#1}%
    \label{bareos-#1}
    \index[general]{bareos-#1!Release Notes}%
    #2
   }

.. literalinclude:: /source/bareos/example/releasenotes-template.rst.inc

Example:

.. literalinclude:: /source/bareos/example/releasenotes-17.2.7.rst.inc


See the output at :ref:`bareos-17.2.7`\ .

.. COMMENT include:: /source/bareos/example/releasenotes.rst.inc



Reference to a Release
----------------------

To refer to a release, use::

    :ref:`bareos-<VERSION>`

Example:

  This refers to :ref:`bareos-17.2.7`\ .

Output:

This refers to :ref:`bareos-17.2.7`\ .


.. Release Notes - Unstable Version
   --------------------------------

   TODO: required?

  If you want to display the release notes of a bareos unstable release, the following formatting should be used:

.. \newcommand{\releasenoteUnstable}[2]{
    \subsection*{\textit{bareos-#1 (unstable)}}
    %\addcontentsline{toc}{subsection}{\protect\numberline{}#1}%
    %\index[general]{bareos-#1!Release Notes}%
    #2
   }



URLs
----

Release URL - Bareos.org
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to display the release download URL from the Bareos.org site, the following formatting should be used:

.. \newcommand{\releaseUrlDownloadBareosOrg}[1]{%
   \url{http://download.bareos.org/bareos/release/#1/}%
   }

   Post Conversion Changes
   ${PERL} 's#\\releaseUrlDownloadBareosOrg\{(.*?)\}#//http://download.bareos.org/bareos/release/\1/#g' ${DESTFILE}

http://download.bareos.org/bareos/release/18.2/


Release URL - Bareos.com
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to display the release download URL from the Bareos.com site, the following formatting should be used:

.. \newcommand{\releaseUrlDownloadBareosOrg}[1]{%
   \url{http://download.bareos.org/bareos/release/#1/}%
   }

   Post Conversion Changes
   ${PERL} 's#\\releaseUrlDownloadBareosCom\{(.*?)\}#//https://download.bareos.com/bareos/release/\1/#g' ${DESTFILE}


https://download.bareos.com/bareos/release/18.2/

Last change: |today|