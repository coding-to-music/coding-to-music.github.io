Kubernetes
==============

.. toctree::
    :maxdepth: 2
    :caption: Contents:
 

.. contents::
    :local:


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

Goals 
-------------------

- Install Docker
- Install a Docker image with DigitalOcean's Kubernetes and doctl 
- Install doctl -- DigitalOcean's CLI

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