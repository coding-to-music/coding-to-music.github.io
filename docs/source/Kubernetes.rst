Kubernetes
==============

.. toctree::
    :maxdepth: 2
    :caption: Contents:
 
    Install-Nodejs-and-npm
    Install-and-Set-Up-kubectl
    Install-Docker
    Install-a-Docker-image-with-DigitalOcean-Kubernetes-and-doctl 
    Install-doctl-DigitalOcean-CLI
    Get-a-token-from-DigitalOcean
    Create-a-DigitalOcean-Kubernetes-cluster
    Connect-to-DigitalOcean-Kubernetes-cluster 

.. contents::
    :local:



Goals 
-------------------

- Install Node.js and npm
- Install and Set Up kubectl
- Install Docker
- Install a Docker image with DigitalOcean's Kubernetes and doctl 
- Install doctl -- DigitalOcean's CLI
- Get a token from DigitalOcean
- Create a DigitalOcean's Kubernetes cluster
- Connect to DigitalOcean's Kubernetes cluster 


How to Install Node.js and npm on Debian 10 Linux
----------------------------------------------------

https://linuxize.com/post/how-to-install-node-js-on-debian-10/


To install Node.js and npm on your Debian use the following commands: :: 

    sudo apt install nodejs npm

One the installation is completed, verify it by typing: ::

    nodejs --version

The command will display the Node.js version: ::

    v10.24.0

This is the easiest way to install Node.js and npm on Debian and should be sufficient for most use cases.


Install and Set Up kubectl on Linux
--------------------------------------

Install kubectl binary with curl on Linux

#. Download the latest release with the command: ::

    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

#. Validate the binary (optional)

Download the kubectl checksum file: ::

    curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

Validate the kubectl binary against the checksum file: ::

    echo "$(<kubectl.sha256) kubectl" | sha256sum --check

If valid, the output is: ::

    kubectl: OK

If the check fails, sha256 exits with nonzero status and prints output similar to: ::

    kubectl: FAILED
    sha256sum: WARNING: 1 computed checksum did NOT match

3. Test to ensure the version you installed is up-to-date:  ::

    kubectl version --client

4. Install kubectl ::

    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl


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




Docker Hub
-----------------------

https://hub.docker.com/

Kubernetes Quickstart
-----------------------

https://www.digitalocean.com/docs/kubernetes/quickstart/


How to Connect to a DigitalOcean Kubernetes Cluster
----------------------------------------------------

https://www.digitalocean.com/docs/kubernetes/how-to/connect-to-cluster/

Getting Started with Kubernetes: A kubectl Cheat Sheet
----------------------------------------------------------

https://www.digitalocean.com/community/cheatsheets/getting-started-with-kubernetes-a-kubectl-cheat-sheet







Last change: |today|