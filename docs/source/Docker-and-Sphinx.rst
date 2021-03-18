Docker and Sphinx
===================================

.. contents::
    :local:
    
  

Docker
--------------

Docker is a container software system 


Install Docker Engine on Debian
-----------------------------------

https://docs.docker.com/engine/install/debian/


Docker Sphinx - Good end-to-end overview
--------------------------------------------

https://github.com/coding-to-music/docker-sphinx-doc

Docker Sphinx - Good end-to-end overview

- Docker sphinx-quickstart
- Docker Run build html
- create a dockerfile
- Docker Build the image
- Docker Run the container


digitalocean/sample-dockerfile
---------------------------------

https://github.com/digitalocean/sample-dockerfile


Official docker-sphinx
-----------------------

https://github.com/sphinx-doc/docker

https://hub.docker.com/r/sphinxdoc/sphinx

Usage
Create a Sphinx project ::

    $ docker run -it --rm -v /path/to/document:/docs sphinxdoc/sphinx sphinx-quickstart

Build HTML document ::

    $ docker run --rm -v /path/to/document:/docs sphinxdoc/sphinx make html

Build EPUB document ::

    $ docker run --rm -v /path/to/document:/docs sphinxdoc/sphinx make epub

Build PDF document ::

    $ docker run --rm -v /path/to/document:/docs sphinxdoc/sphinx-latexpdf make latexpdf

Tips

If you would like to install dependencies, use sphinxdoc/sphinx as a base image::

    # in your Dockerfile
    FROM sphinxdoc/sphinx

    WORKDIR /docs
    ADD requirements.txt /docs
    RUN pip3 install -r requirements.txt


SphinXsearch Jul 7, 2014. Sphinx in Docker. The basics.    
-----------------------------------------------------------

http://sphinxsearch.com/blog/2014/07/07/sphinx-in-docker-the-basics/

Sphinx in Docker. The basics

- What is Docker?
- Docker and sphinx
- Clone and build
- Run
- sudo docker.io ps
- docker.io inspect (container id)
- indexandsearch.sh and searchd.sh
- Command line search

docker-sphinxsearch
-----------------------

https://github.com/coding-to-music/docker-sphinxsearch

Docker image for Sphinx search engine ::

    docker pull macbre/sphinxsearch
 
    
Usage example
~~~~~~~~~~~~~~~

You can use this image in docker-compose-powered app: ::

    services:
    sphinx:
        image: macbre/sphinxsearch:3.3.1
        ports:
        - "127.0.0.1:36307:36307" # bind to local interface only!
        volumes:
        - ./data:/opt/sphinx/index  # directory where sphinx will store index data
        - ./sphinx.conf:/opt/sphinx/conf/sphinx.conf  # SphinxSE configuration file
        mem_limit: 512m # match indexer.value from sphinx.conf

Notes         

- First, execute `docker-compose run sphinx indexer --all` to prepare indices. Otherwise, you'd end up `with WARNING: index 'test1': prealloc: failed to open /opt/sphinx/index/test1.sph: No such file or directory; NOT SERVING` error.
- Then, execute `docker-compose up -d` to run sphinsearch daemon in the background.

Read more at https://lukaszherok.com/post/view/9/Running%20SphinxSearch%20in%20Podman%20container


sphinxdocker/Dockerfile
-------------------------

sphinxdocker/Dockerfile

https://github.com/coding-to-music/sphinxdocker/blob/master/Dockerfile

sphinxdocker/Dockerfile ::

    FROM phusion/baseimage

    RUN apt-get update
    RUN apt-get -y install software-properties-common
    RUN apt-get update
    RUN add-apt-repository -y ppa:builds/sphinxsearch-beta
    RUN apt-get update
    RUN apt-get -y install sphinxsearch
    RUN mkdir /var/lib/sphinx
    RUN mkdir /var/lib/sphinx/data
    RUN mkdir /var/log/sphinx
    RUN mkdir /var/run/sphinx
    ADD indexandsearch.sh /
    RUN chmod a+x indexandsearch.sh
    ADD searchd.sh /
    RUN chmod a+x searchd.sh
    ADD lordsearchd.sh /
    RUN chmod a+x lordsearchd.sh


Gitlab CI with Docker and Sphinx
-----------------------------------

Gitlab CI with Docker and Sphinx

https://ci-setup-docs.readthedocs.io/en/latest/Sphinxgettingstarted.html


ReadTheDocs - Getting Started with Sphinx
--------------------------------------------

ReadTheDocs - Getting Started with Sphinx

https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html


Visual Studio Code - VSCode Dev Containers
-----------------------------------------------

VSCode Remote development on Digitalocean
--------------------------------------------

https://medium.com/@klogic/vscode-remote-development-on-digitalocean-d7d65e1656ef


How To Use Visual Studio Code for Remote Development via the Remote-SSH Plugin
----------------------------------------------------------------------------------

https://www.digitalocean.com/community/tutorials/how-to-use-visual-studio-code-for-remote-development-via-the-remote-ssh-plugin


VSCode Remote Development using SSH
--------------------------------------

https://code.visualstudio.com/docs/remote/ssh


Remote Development Tips and Tricks
-------------------------------------

https://code.visualstudio.com/docs/remote/troubleshooting#_using-rsync-to-maintain-a-local-copy-of-your-source-code

vscode-theme-generator
-------------------------

https://github.com/Tyriar/vscode-theme-generator

Vagrant
=============

Install Vagrant
------------------
https://learn.hashicorp.com/tutorials/vagrant/getting-started-install

Vagrant Quick Start
--------------------

https://learn.hashicorp.com/tutorials/vagrant/getting-started-index?in=vagrant/getting-started

Sharing Objects
====================

Facebook - Using Objects
-----------------------------------

https://developers.facebook.com/docs/sharing/opengraph/using-objects

https://developers.facebook.com/docs/sharing/webmasters/getting-started/change-link


Google - Structured Data Testing for Rich Objects
------------------------------------------------------

Structured Data Testing for Rich Objects

https://search.google.com/structured-data/testing-tool

What are rich results?
~~~~~~~~~~~~~~~~~~~~~~~~

Rich results are experiences on Google surfaces, such as Search, that go beyond the standard blue link. Rich results can include carousels, images, or other non-textual elements.

https://search.google.com/test/rich-results


Rich result status reports

- See your Job postings, Recipes, and more
- Learn which rich results Google could or could not read from your site, and troubleshoot rich result errors.

Rich result reports for your site are listed under Enhancements in the menu pane. There is a separate report for each rich result type. You will see a rich result report only if:

- Google finds rich results of that type in your property, and
- The type is a supported rich result type listed here https://support.google.com/webmasters/answer/7552505?hl=en#supported-result-types

https://support.google.com/webmasters/answer/7552505?hl=en




Last change: |today|