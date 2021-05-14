:index:`\ <single: Werkzeug WSGI web application library>`\

.. meta::
    :description lang=en: DESCRIPTIONWerkzeug WSGI Server / Gateway invokes callable object served by the WSGI Application / Framework
    :headline lang=en: HEADLINEWerkzeug WSGI web application library
    :image lang=en: https://pandemic-overview.readthedocs.io/en/latest/_images/WSGI-web-application-library.png
    :author lang=en: Thomas Connors
    :publisher lang=en: all-knowledge.info
    :datePublished lang=en: May 12 2021
    :dateModified lang=en: May 14 2021
    :mainEntityOfPage lang=en: https://pandemic-overview.readthedocs.io/en/latest/myGuides/Werkzeug-comprehensive-WSGI-web-application-library.html


ogp_type = "article"
ogp_title="OGP_TITLE Werkzeug WSGI web application library"
ogp_site_url = "OGP_URL http://example.org/"

ogp_image = "OGP_IMAGE http://example.org/image.png"
ogp_description_length = 300
ogp_description="Werkzeug WSGI web application library" 
ogp_headline="Werkzeug WSGI web application library" 
ogp_article:modified_time="2021-05-14T12:48:53+00:00" 
ogp_article:published_time="2021-05-12T11:55:38+00:00" 
ogp_article:expiration_time="2025-05-12T11:55:38+00:00"
ogp_article:author="Thomas Connors"
ogp_article:section="Technology"
ogp_article:tag=[Word1, word2, word3]
ogp_custom_meta_tags = [
'MetaTag1',
'MetaTag2',
'MetaTag3',
'MetaTag4',
]

ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
    '<meta name="theme-color" content="#AC2B37" />',
]



Werkzeug WSGI web application library
======================================================================

.. Note:: 
    
    | This page was:
    | Created May 12 2021
    | Updated May 13 2021
    | Last Built |today|

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


Last change: |today|