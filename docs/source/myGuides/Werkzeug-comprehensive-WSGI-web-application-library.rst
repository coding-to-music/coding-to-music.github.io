:index:`\ <single: Werkzeug WSGI web application library>`\

.. meta::
    :description: Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.
    :keywords: werkzeug German noun: "tool". Etymology: werk ("work"), zeug ("stuff")
    :title: Werkzeug WSGI web application library
    :headline lang=en: HEADLINEWerkzeug WSGI web application library
    :image lang=en: https://pandemic-overview.readthedocs.io/en/latest/_images/WSGI-web-application-library.png
    :author lang=en: Thomas Connors
    :publisher lang=en: all-knowledge.info
    :datePublished lang=en: May 12 2021
    :dateModified lang=en: May 14 2021
    :mainEntityOfPage lang=en: https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html

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


<!-- HTML Meta Tags -->
<title>Werkzeug WSGI web application library</title>
<meta name="description" content=":title lang=en: Werkzeug WSGI web application library :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs. :description lang=en: Werkzeug W...">

<!-- Facebook Meta Tags -->
<meta property="og:url" content="https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html">
<meta property="og:type" content="website">
<meta property="og:title" content="Werkzeug WSGI web application library">
<meta property="og:description" content=":title lang=en: Werkzeug WSGI web application library :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs. :description lang=en: Werkzeug W...">
<meta property="og:image" content="../_images/WSGI-web-application-library.png">

<!-- Twitter Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta property="twitter:domain" content="pandemic-overview.readthedocs.io">
<meta property="twitter:url" content="https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html">
<meta name="twitter:title" content="Werkzeug WSGI web application library">
<meta name="twitter:description" content=":title lang=en: Werkzeug WSGI web application library :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs. :description lang=en: Werkzeug W...">
<meta name="twitter:image" content="../_images/WSGI-web-application-library.png">

<!-- Meta Tags Generated via https://www.opengraph.xyz -->
      

.. code::

    ogp_image = "https://pandemic-overview.readthedocs.io/en/latest/_images/Coming_Attractions-780x683.jpg"

    <!-- HTML Meta Tags -->
    <title>Werkzeug WSGI web application library</title>
    <meta name="description" content=":title lang=en: Werkzeug WSGI web application library :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs. :description lang=en: Werkzeug W...">

    <!-- Facebook Meta Tags -->
    <meta property="og:url" content="https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Werkzeug WSGI web application library">
    <meta property="og:description" content=":title lang=en: Werkzeug WSGI web application library :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs. :description lang=en: Werkzeug W...">
    <meta property="og:image" content="../_images/WSGI-web-application-library.png">

    <!-- Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta property="twitter:domain" content="pandemic-overview.readthedocs.io">
    <meta property="twitter:url" content="https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html">
    <meta name="twitter:title" content="Werkzeug WSGI web application library">
    <meta name="twitter:description" content=":title lang=en: Werkzeug WSGI web application library :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs. :description lang=en: Werkzeug W...">
    <meta name="twitter:image" content="../_images/WSGI-web-application-library.png">

    <!-- Meta Tags Generated via https://www.opengraph.xyz -->
      
    :title lang=en: Werkzeug WSGI web application library
    :description lang=en: Get started writing technical documentation with Sphinx and publishing to Read the Docs.
    :description lang=en: Werkzeug WSGI Server / Gateway invokes callable object served by the WSGI Application / Framework
    :headline lang=en: HEADLINEWerkzeug WSGI web application library
    :image lang=en: https://pandemic-overview.readthedocs.io/en/latest/_images/WSGI-web-application-library.png
    :author lang=en: Thomas Connors
    :publisher lang=en: all-knowledge.info
    :datePublished lang=en: May 12 2021
    :dateModified lang=en: May 14 2021
    :mainEntityOfPage lang=en: https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html
    :ogp_site_url: http://example.org/
    :ogp_image: http://example.org/image.png
    :ogp_description_length: 300
    :ogp_type: article
    :modified_time: May 13 2021
    :published_time: May 12 2021 
    :headline lang=en: Werkzeug WSGI web application library 
    :article:section: Technology

    # :ogp_article:tag=[Word1, word2, word3]
    # :ogp_custom_meta_tags: = [
    #     'MetaTag1',
    #     'MetaTag2',
    #     'MetaTag3',
    #     'MetaTag4',
    #     ]



    # ogp_custom_meta_tags = [
    #         '<meta property="og:ignore_canonical" content="true" />',
    #         '<meta name="theme-color" content="#AC2B37" />',
    #     ]









.. Note:: 
    
    | This page was:
    | Created May 12 2021
    | Updated May 13 2021
    | Last Built |today|



Last change: |today|