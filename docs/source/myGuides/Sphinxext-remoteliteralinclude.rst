Sphinx Remote Literal Include 
=========================================

sphinxext-remoteliteralinclude 


.. Note:: 
    
    | This page was:
    | Created May 26 2021
    | Updated May 26 2021
    | Last Built |today|

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Homepage

https://github.com/wpilibsuite/sphinxext-remoteliteralinclude


Here is how to call the extension for remote literal include for example.java
--------------------------------------------------------------------------------

.. code:: java

    .. rli:: https://example.com/example.java
    :language: java
    :lines: 1-29
    :linenos:
    :lineno-start: 1



For some reason this does not literal include correctly: https://example.com/example.java

.. rli:: https://example.com/example.java
   :language: java
   :lines: 1-29
   :linenos:
   :lineno-start: 1


Here is how to call the extension for remote literal include for README.md using line numbers
-----------------------------------------------------------------------------------------------

.. code:: java

    .. rli:: https://raw.githubusercontent.com/wpilibsuite/sphinxext-remoteliteralinclude/main/README.md
    :language: java
    :lines: 1-29
    :linenos:
    :lineno-start: 1


Here is a literal include README.md with shading and line numbers


.. rli:: https://raw.githubusercontent.com/wpilibsuite/sphinxext-remoteliteralinclude/main/README.md
   :language: java
   :lines: 1-29
   :linenos:
   :lineno-start: 1


Here is how to call the extension for remote literal include for README.md embedded 
--------------------------------------------------------------------------------------

.. code:: java

    .. rli:: https://raw.githubusercontent.com/wpilibsuite/sphinxext-remoteliteralinclude/main/README.md


Here is a README.md as if it was typed right into this document


.. rli:: https://raw.githubusercontent.com/wpilibsuite/sphinxext-remoteliteralinclude/main/README.md







.. contents::
    :local:







Last change: |today|