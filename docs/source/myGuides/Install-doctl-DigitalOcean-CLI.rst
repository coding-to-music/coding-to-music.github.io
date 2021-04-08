Install doctl DigitalOcean CLI
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:

   
Get doctl for Docker
--------------------------

https://hub.docker.com/r/digitalocean/doctl

doctl - command line interface for DigitalOcean ::

    docker pull digitalocean/doctl:<TAG>

The following tags are available:

- latest - The most recent doctl release
- <version> - A specific version of doctl, e.g.: 1.27.0 (list of available versions)
- 1-latest - The most recent release in the 1.x series (doctl uses semantic versioning)

Using doctl with Docker
~~~~~~~~~~~~~~~~~~~~~~~~~

When using doctl with Docker, you must set the DIGITALOCEAN_ACCESS_TOKEN environment variable inside the container. Many commands require user input, so it is recommended to pass the --interactive and --tty flags as well. For example: ::

    docker run --rm --interactive --tty \
    --env=DIGITALOCEAN_ACCESS_TOKEN=<YOUR-DO-API-TOKEN> \
    digitalocean/doctl account get

Some commands may require additional arguments, including:

doctl compute ssh
~~~~~~~~~~~~~~~~~~~

doctl allows you to connect to a Droplet over SSH without knowing its IP address by providing its ID. In order to use this feature with Docker, you must mount your SSH private key from your local file system into the container. For example: ::

    docker run --rm --interactive --tty \
    --env=DIGITALOCEAN_ACCESS_TOKEN=<YOUR-DO-API-TOKEN> \
    -v $HOME/.ssh/id_rsa:/root/.ssh/id_rsa \
    digitalocean/doctl compute ssh <DROPLET-ID>
    doctl compute ssh-key import

To upload an SSH public key to your DigitalOcean account using Docker, you must make it accessible inside the container by mounting it as a volume. For example: ::

    docker run --rm --interactive --tty \
    --env=DIGITALOCEAN_ACCESS_TOKEN=<YOUR-DO-API-TOKEN> \
    -v $HOME/path/to/id_rsa.pub:/root/id_rsa.pub \
    digitalocean/doctl compute ssh-key import <SSH-KEY-NAME> \
    --public-key-file /root/id_rsa.pub

Additional Information
~~~~~~~~~~~~~~~~~~~~~~~~

doctl is maintained on GitHub. View the source, contribute, or report issues at:

https://github.com/digitalocean/doctl
For more information about doctl, see:

How To Use Doctl, the Official DigitalOcean Command-Line Client

https://www.digitalocean.com/community/tutorials/how-to-use-doctl-the-official-digitalocean-command-line-client



Last change: |today|