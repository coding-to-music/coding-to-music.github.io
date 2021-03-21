General Computer Setup
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
.. contents::
    :local:



Setup your computer, we will cover each item     
--------------------------------------------------------------------

Enable Linux on your Chromebook     
--------------------------------------------------------------------

In your Chromebook settings, enable the Linux (Beta)

Details about your computer and operating system    
------------------------------------------------------

Chromebook is Debian ::
~~~~~~~~~~~~~~~~~~~~~~~

    connorstom@penguin:~$ cat /etc/os-release
    PRETTY_NAME="Debian GNU/Linux 10 (buster)"
    NAME="Debian GNU/Linux"
    VERSION_ID="10"
    VERSION="10 (buster)"
    VERSION_CODENAME=buster
    ID=debian
    HOME_URL="https://www.debian.org/"
    SUPPORT_URL="https://www.debian.org/support"
    BUG_REPORT_URL="https://bugs.debian.org/"


Digitalocean is Ubuntu   ::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    // this chart would be different on Ubuntu. Here is a Debain example
    connorstom@penguin:~$ cat /etc/os-release
    PRETTY_NAME="Debian GNU/Linux 10 (buster)"
    NAME="Debian GNU/Linux"
    VERSION_ID="10"
    VERSION="10 (buster)"
    VERSION_CODENAME=buster
    ID=debian
    HOME_URL="https://www.debian.org/"
    SUPPORT_URL="https://www.debian.org/support"
    BUG_REPORT_URL="https://bugs.debian.org/"

Handy aliases and abbreviations into .bashrc and .bash_aliases   
--------------------------------------------------------------------


There are some useful aliases in .bash_alias of this repo:

https://github.com/coding-to-music/bash_aliases_docker_alias_cheat_sheet

In this file here [.bash_aliases](https://raw.githubusercontent.com/coding-to-music/bash_aliases_docker_alias_cheat_sheet/master/.bash_aliases)


Edit the file .bash_aliases and put the contents from GitHub
```java
source ~/.bashrc

// in the future, you will just need to type 'sc' and it will source your .bashrc which calls .bash_aliases
```
## Installing Git so you can work with GitHub

Download and install Git
```java
$ sudo apt-get install git
// Now git should be installed. To check use
$ git --version
git version 2.19.1
```

Configuring GitHub git config user.name user.email 
--------------------------------------------------------------------

Once the installation has successfully completed, the next thing to do is to set up the configuration details of the GitHub user. To do this use the following two commands by replacing "user_name" with your GitHub username and replacing "email_id" with your email-id you used to create your GitHub account.
```java
git config --global user.name coding-to-music
git config --global user.email connors.tom@gmail.com
```

The following image shows an example of my configuration with my "user_name" being "akshaypai" and my "email_id" being "abc123@gmail.com"


VS Code install for Debian and Ubuntu based distributions
--------------------------------------------------------------------

[https://code.visualstudio.com/docs/setup/linux](https://code.visualstudio.com/docs/setup/linux)

The easiest way to install Visual Studio Code for Debian/Ubuntu based distributions is to download and install the [.deb package (64-bit)](https://go.microsoft.com/fwlink/?LinkID=760868), either through the graphical software center if it's available, or through the command line with:


```java
sudo apt install ./<file>.deb

download the file from the website to downloads and move it to linux file system then run:

https://code.visualstudio.com/docs/setup/linux
https://github.com/nodesource/distributions/blob/master/README.md#debinstall

# If you're on an older Linux distribution, you will need to run this instead:
# sudo dpkg -i <file>.deb
# sudo apt-get install -f # Install dependencies
connorstom@penguin:~$ code --version
1.51.1
e5a624b788d92b8d34d1392e4c4d9789406efe8f
x64
```


Installing the .deb package will automatically install the apt repository and signing key to enable auto-updating using the system's package manager. Note that 32-bit and .tar.gz binaries are also available on the [VS Code download page](https://code.visualstudio.com/Download).

The repository and key can also be installed manually with the following script:


```java
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
```


Then update the package cache and install the package using:


```java
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install code # or code-insiders

sudo apt install gnome-keyring
```

### Installing Visual Studio Code on Ubuntu

[https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-18-04/](https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-18-04/)

To install Visual Studio Code on your Ubuntu system, follow these steps:

1. First, update the packages index and install the dependencies by typing:
2. `sudo apt update`
3. `sudo apt install software-properties-common apt-transport-https wget`
4. Next, import the Microsoft GPG key using the following [wget command](https://linuxize.com/post/wget-command-examples/):
5. `wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -`
6. And enable the Visual Studio Code repository by typing:
7. `sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"`
8. Once the [apt repository is enabled](https://linuxize.com/post/how-to-add-apt-repository-in-ubuntu/), install the latest version of Visual Studio Code with:
9. `sudo apt update`
10. `sudo apt install code`

That’s it. Visual Studio Code has been installed on your Ubuntu desktop and you can start using it.


Starting Visual Studio Code
--------------------------------------------------------------------


Now that VS Code is installed on your Ubuntu system you can launch it either from the command line by typing `code` or by clicking on the VS Code icon (`Activities -> Visual Studio Code`).

When you start VS Code for the first time, a window like the following should appear:

<img width="800px" src="https://github.com/coding-to-music/battlecode2021/blob/main/Assets/vscode-default-home-screen.jpg?raw=true" align="center" alt="vscode-default-home-screen.jpg" />
</b>

Connect with vscode in the cloud so your settings persist over devices and sessions
--------------------------------------------------------------------------------------------

vscode->settings->Sync Data

There is a very good set of detailed instructions about vscode cloud settings sync [HERE](https://code.visualstudio.com/docs/editor/settings-sync)

### Setup a password for cloud sync - you will be prompted each time you start vscode  


<img width="800px" src="https://github.com/coding-to-music/battlecode2021/blob/main/Assets/choose-password-for-vscode-sync-data.png?raw=true" align="center" alt="choose-password-for-vscode-sync-data.png" />
</b>



### If you previously have a cloud account you can merge your data    

<br />  
<img width="800px" src="https://github.com/coding-to-music/battlecode2021/blob/main/Assets/merge-or-replace-cloud-sync-data.png?raw=true" align="center" alt="merge-or-replace-cloud-sync-data.png" />
</b>
<br />  
  

You can now start installing extensions and configuring VS Code according to your preferences.



How to update VS code to the latest version in linux
------------------------------------------------------------------------------

How to update VS code to the latest version in linux ::

    sudo apt-get install --only-upgrade code



Updating Visual Studio Code - every month need to do this
--------------------------------------------------------------------


When a new version is released you can update the Visual Studio Code package through your desktop standard Software Update tool or by running the following commands in your terminal: ::

    sudo apt update
    sudo apt upgrade
    // or just this
    sudo apt update
    sudo apt upgrade code

Create .ssh directory and generate SSH public and private keys  
--------------------------------------------------------------------

Create a directory for the public keys ::

    // In root
    Mkdir .ssh
    Chmod 700 .ssh
    Cd .ssh
    // Create SSH public and private keys  
    // Store them here  

    Chmod 600 private_key

Create SSH Key for Github
--------------------------------------------------------------------

Now you need to create your SSH key for Github

```java  
ssh-keygen -t rsa -C “connors.tom@gmail.com”  

// It will get saved to 
home/tom/.ssh/id_rsa                // this is the private key, very long paragraph
home/tom/.ssh/id_rsa.pub         // this is the public key,         short paragraph
// Copy that key in that file. I would suggest using Win SCP to download the file similar to FTP
```

file: ssh-rsa 
- 7 lines long private key 
- a short paragraph 
- this is what you will paste into GitHub and Digitalocean
  e1f0vfsMPOANChLOUWbSJTtf4s4P2x6CAYCOQYcd “connors.tom@gmail.com”

-----BEGIN RSA PRIVATE KEY-----
really big long private key
-----END RSA PRIVATE KEY-----

## GitHub - set your ssh key and get your GitHub token for vscode   

Once you copy the key, 
- sign into Github and 
- goto “Settings->SSH and GPG Keys” and 
- add and name of the new key   

<img width="800px" src="https://github.com/coding-to-music/battlecode2021/blob/main/Assets/ssh-keys-in-GitHub.png?raw=true" align="center" alt="Battlecode 2021 Image" />
</b>


Get your vscode token from github account settings 
--------------------------------------------------------------------

</b>
<img width="400px" src="https://github.com/coding-to-music/battlecode2021/blob/main/Assets/vscode-github-token.png?raw=true" align="center" alt="vscode-github-token.png" />
</b>


Let vscode know about the GitHub token at the bottom left of vscode click bottom-left and paste github token into the command prompt area in the top menu toolbar 

<br />  
<img width="600px" src="https://github.com/coding-to-music/battlecode2021/blob/main/Assets/bottom-left-of-vscode-click-and-paste-github-token.png?raw=true" align="center" alt="bottom-left-of-vscode-click-and-paste-github-token.png" />
</b>
<br />  
  
Last change: |today|