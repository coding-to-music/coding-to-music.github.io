:index:`\ <single: Werkzeug WSGI web application library>`\

.. meta::
    :description: Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.
    :keywords: werkzeug German noun: "tool". Etymology: werk ("work"), zeug ("stuff")
    :title: Werkzeug WSGI web application library
    :headline lang=en: Werkzeug WSGI web application library
    :image: https://pandemic-overview.readthedocs.io/en/latest/_images/WSGI-web-application-library.png
    :author lang=en: Thomas Connors
    :publisher lang=en: all-knowledge.info
    :datePublished lang=en: May 12 2021
    :dateModified lang=en: May 14 2021
    :mainEntityOfPage lang=en: https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html
    :twitter:site: all-knowledge.info
    :twitter:card: summary_large_image
    :twitter:url: https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html
    :twitter:title: Werkzeug WSGI web application library
    :twitter:description: Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.
    :twitter:image: https://pandemic-overview.readthedocs.io/en/latest/_images/WSGI-web-application-library.png
    :og:site_name: all-knowledge.info
    :og:type: article
    :og:url: https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html
    :og:title: Werkzeug WSGI web application library
    :og:image: https://pandemic-overview.readthedocs.io/en/latest/_images/WSGI-web-application-library.png


Werkzeug WSGI web application library
======================================================================

.. figure:: /assets/Software/WSGI-web-application-library.png
  :align: center
  :width: 80 %
  
  WSGI Server / Gateway invokes callable object served by the WSGI Application / Framework  


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:



Werkzeug is a WSGI web application library
--------------------------------------------------------------------------------------------

https://github.com/pallets/werkzeug


Werkzeug Definition
----------------------------

werkzeug German noun: "tool". Etymology: werk ("work"), zeug ("stuff")

Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.

It includes:

An interactive debugger that allows inspecting stack traces and source code in the browser with an interactive interpreter for any frame in the stack.

    * A full-featured request object with objects to interact with headers, query args, form data, files, and cookies.
    * A response object that can wrap other WSGI applications and handle streaming data.
    * A routing system for matching URLs to endpoints and generating URLs for endpoints, with an extensible system for capturing variables from URLs.
    * HTTP utilities to handle entity tags, cache control, dates, user agents, cookies, files, and more.
    * A threaded WSGI server for use while developing applications locally.
    * A test client for simulating HTTP requests during testing without requiring running a server.

Werkzeug doesn't enforce any dependencies. It is up to the developer to choose a template engine, database adapter, and even how to handle requests. It can be used to build all sorts of end user applications such as blogs, wikis, or bulletin boards.

`Flask <https://www.palletsprojects.com/p/flask/>`_ wraps Werkzeug, using it to handle the details of WSGI while providing more structure and patterns for defining powerful applications.


Example of embedded YouTube video
--------------------------------------

This screencast will help you get started or you can
`read our guide below <https://pandemic-overview.readthedocs.io/en/latest/bareos/guides/intro/getting-started-with-sphinx>`_.

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://www.youtube-nocookie.com/embed/oJsUvBQyHBs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>


Example of embedded GitHub Project Issue Kanban board - for this project (does not work)
----------------------------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://github.com/coding-to-music/coding-to-music.github.io/projects/1?fullscreen=true" frameborder="0" allowfullscreen></iframe>
    </div>


Example of embedded Twitter page (does not work)
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://twitter.com" frameborder="0" allowfullscreen></iframe>
    </div>

Example of embedded Facebook photo (does not work)
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://www.facebook.com/photo/?fbid=259355012646906&set=gm.543252166842990" frameborder="0" allowfullscreen></iframe>
    </div>

Example of embedded CNN (does not work)
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://www.cnn.com/" frameborder="0" allowfullscreen></iframe>
    </div>


An embedded HTML page using embed and drudgereport:

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <embed type="text/html" src="https://drudgereport.com" width="500" height="200">
    </div>


An embedded HTML page using object and drudgereport:

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <object data="https://drudgereport.com" width="500" height="200"></object>
    </div>


Example of embedded other website drudgereport using iframe
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://drudgereport.com" frameborder="0" allowfullscreen></iframe>
    </div>


Example of embedded other website
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://drudgereport.com" frameborder="0" allowfullscreen></iframe>
    </div>


How to insert a javascript in a single Sphinx page?
------------------------------------------------------

.. raw:: html

    <script>
    function myFunction() {
     alert("I am an alert box!");
    }
    </script>


<button onclick="myFunction()">Try it</button>

How can i insert html and css and javascript both in a sphinx's reStructuredText file ?
----------------------------------------------------------------------------------------------

The html content:

https://cloudstack.ninja/showkey/how-to-embed-html-and-css-and-javascript-in-sphinxs-restructuredtext-file/

.. code-block:: 

    <div id="mytest">test</div>


The css content:

.. code-block:: 

    <style type='text/css'>
    #mytest{
        border:1px solid red;
        height:80px;
        width:80px;
    }
    </style>

The javascript content:

.. code-block:: 

    <script type='text/javascript'>
    var ob = document.getElementById('mytest');
    ob.onmouseover = function(){
        this.innerHTML = 'text in box changed';
    } 
    </script>






.. Note:: 
    
    | This page was:
    | Created May 12 2021
    | Updated May 13 2021
    | Last Built |today|



Last change: |today|