How to move files when developing in a container
====================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:


Use Docker cp to move files in and out of the container

run this from OUTSIDE the container, to import files into the container

.. prompt:: bash

   ls -l 
   -rw-r--r-- 1 tmc tmc     54218 Apr 17 03:59 budesonide_3_cropped-768x992.jpg
   
   tmc@penguin:~$ docker ps
   
   CONTAINER ID   IMAGE                                                            COMMAND                  CREATED       STATUS          PORTS     NAMES
   fccc907a24a5   vsc-coding-to-music.github.io-0a59822c2d4c24fc3f5de7ea0edf5452   "/bin/sh -c 'echo Co…"   2 weeks ago   Up 11 minutes             wonderful_newton

   # general pattern
   docker cp filename [container#]:/DestinationPath
   
   docker cp budesonide_3_cropped-768x992.jpg fccc907a24a5:/tmp


Last change: |today|