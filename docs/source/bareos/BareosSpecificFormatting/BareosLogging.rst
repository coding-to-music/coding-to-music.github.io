Bareos Logging
==============

.. Note:: 
    
    This page was Retrieved and copied April 16 2021
    
    https://github.com/bareos/blob/master/docs/manuals/bareos/BareosSpecificFormatting/BareosLogging.rst


If you want to display Bareos specific logs, use following formatting:

.. ${PERL} 's#\{logging\}\{(.*)\}#\n.. code-block:: sh\n    :caption: \1\n#g'   ${DESTFILE}

.. literalinclude:: /bareos/example/code-block-bareoslog.rst.inc

The output will look like this:

.. include:: /bareos/example/code-block-bareoslog.rst.inc

Last change: |today|