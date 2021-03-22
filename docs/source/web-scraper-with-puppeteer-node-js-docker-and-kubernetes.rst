How To Build a Concurrent Web Scraper with Puppeteer, Node.js, Docker, and Kubernetes
==========================================================================================


.. toctree::
    :maxdepth: 2
    :caption: Contents:
 

.. contents::
    :local:

Build a Concurrent Web Scraper with Puppeteer, Node.js, Docker, and Kubernetes
----------------------------------------------------------------------------------------

https://www.digitalocean.com/community/tutorials/how-to-build-a-concurrent-web-scraper-with-puppeteer-node-js-docker-and-kubernetes


By Carlos Mucuho

Published onAugust 19, 2020 14.7k views

Introduction
~~~~~~~~~~~~~

Web scraping, also known as web crawling, uses bots to extract, parse, and download content and data from websites.

You can scrape data from a few dozen web pages using a single machine, but if you have to retrieve data from hundreds or even thousands of web pages, you might want to consider distributing the workload.

In this tutorial you will use Puppeteer to scrape books.toscrape, a fictional bookstore that functions as a safe place for beginners to learn web scraping and for developers to validate their scraping technologies. At the time of writing this, there are 1000 books on books.toscrape and therefore 1000 web pages that you could scrape. However, in this tutorial, you will only scrape the first 400. To scrape all these web pages in a short amount of time, you will build and deploy a scalable app containing the Express web framework and the Puppeteer browser controller to a Kubernetes cluster. To interact with your scraper, you will then build an app containing axios, a promise-based HTTP client, and lowdb, a small JSON database for Node.js.

When you complete this tutorial, you will have a scalable scraper capable of simultaneously extracting data from multiple pages. With the default settings and a three-node cluster, for instance, it will take less than 2 minutes to scrape 400 pages on books.toscrape. After scaling your cluster, it will take about 30 seconds.


Prerequisites
~~~~~~~~~~~~~~~~

To follow this tutorial, you will need a machine with:

- Docker installed. Follow our tutorial on how to install and use Docker for instructions. Docker’s website provides installation instructions for other operating systems like macOS and Windows.
- An account at Docker Hub for storing your Docker image.
- A Kubernetes 1.17+ cluster with your connection configuration set as the kubectl default. To create a Kubernetes cluster on DigitalOcean, read our Kubernetes Quickstart. To connect to the cluster, read How to Connect to a DigitalOcean Kubernetes Cluster.
- kubectl installed. Follow this tutorial on getting started with Kubernetes: A kubectl Cheat Sheet to install it.
- Node.js installed on your development machine. This tutorial was tested on Node.js version 12.18.3 and npm version 6.14.6. Follow this guide to install Node.js on macOS, or follow this guide to install Node.js on various Linux distributions.
- If you are using DigitalOcean Kubernetes, then you will also need a Personal Access Token. To create one, you can follow our guide on how to create a Personal Access Token. Save this token in a safe place; it provides full access to your account.



Last change: |today| 