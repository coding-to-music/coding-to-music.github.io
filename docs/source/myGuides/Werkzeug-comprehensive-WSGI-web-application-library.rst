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

Need to do this



Use a large figure as a cover on a link but people may not know to click it to download the PDF
---------------------------------------------------------------------------------------------------

.. figure:: /assets/2017-Spars-Pandemic-Tabletop-communications-exercise/171018-spars-pandemic-scenario-cover-page.jpg
  :align: right
  :width: 80 %
  :target: /assets/2017-Spars-Pandemic-Tabletop-communications-exercise/spars-pandemic-scenario.pdf
  :alt: SPARS Pandemic scenario book (PDF)

  Self-guided tabletop training experience challenges public health communicators and risk communication researchers to consider the complex messaging dilemmas of a future outbreak that requires development of a new vaccine

  Source `SPARS Pandemic scenario book (PDF) March 30 2021`_.

  .. _SPARS Pandemic scenario book (PDF) March 30 2021: https://www.centerforhealthsecurity.org/our-work/pubs_archive/pubs-pdfs/2017/spars-pandemic-scenario.pdf

SPARS pandemic scenario book


How to use an <object> object that embeds a PDF into a sphinx rst page 
----------------------------------------------------------------------------------------------

https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Other_embedding_technologies

https://pandemic-overview.readthedocs.io/en/latest/_images/171018-spars-pandemic-scenario-cover-page.jpg

https://pandemic-overview.readthedocs.io/en/latest/_images/spars-pandemic-scenario.pdf


.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <object data="spars-pandemic-scenario.pdf" type="application/pdf"
            width="800" height="1200">
    <p>You don't have a PDF plugin, but you can
        <a href="spars-pandemic-scenario.pdf">download the PDF file.
        </a>
    </p>
    </object>
    </div>

How to insert a javascript in a single Sphinx page and create an alert box? (does not work) 
----------------------------------------------------------------------------------------------

https://stackoverflow.com/questions/59098032/how-to-insert-a-javascript-in-a-single-sphinx-page

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <script>
    function myFunction() {
     alert("I am an alert box!");
    }
    </script>
    </div>


Example of embedded Twitter page (does not work)
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://twitter.com" frameborder="0" allowfullscreen></iframe>
    </div>

Embed a player using the IFrame Player API
---------------------------------------------------------------------------

https://developers.google.com/youtube/player_parameters


.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <div id="ytplayer"></div>

    <script>
    // Load the IFrame Player API code asynchronously.
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // Replace the 'ytplayer' element with an <iframe> and
    // YouTube player after the API code downloads.
    var player;
    function onYouTubePlayerAPIReady() {
        player = new YT.Player('ytplayer', {
        height: '360',
        width: '640',
        videoId: 'M7lc1UVf-VE'
        });
    }
    </script>
    </div>

Example of embedded GIF hosted elsewhere (need to scale or make fullscreen)
---------------------------------------------------------------------------

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://i1.wp.com/techcrunch.com/wp-content/uploads/2021/05/starline-gif.gif?ssl=1" frameborder="0" allowfullscreen></iframe>
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

    <div style="text-align: center; margin-bottom: 2em;">
    <script>
    function myFunction() {
     alert("I am an alert box!");
    }
    </script>
    </div>


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