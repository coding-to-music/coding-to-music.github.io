Hello and welcome!!

You are lookating at this repository https://github.com/coding-to-music/coding-to-music.github.io 

My main repo/profile/README is over here https://github.com/coding-to-music

This repo you are looking at is where the website https://pandemic-overview.readthedocs.io is hosted from 

Currently now all-knowledge.info is pointing to here

```java
// put all the files that will be the content of the table of contents here:
// https://coding-to-music.github.io/docs/source/

```

How to build:
```java
cd docs
make html

// That will use the following file as a source:
// https://coding-to-music.github.io/docs/source/index.rst

// To make the following output file:
// https://coding-to-music.github.io/docs/build/html/index.html

// send it to the remote repo
git add .
git commit -m 'commit message'
git push

//The build process is triggered via a webhook, a commit in this repo causes a GitHub Action which causes ReadTheDocs to rebuild their page
```

View it on 
This is where the website [https://pandemic-overview.readthedocs.io](https://pandemic-overview.readthedocs.io) is hosted from 

The ReadTheDocs control panel [https://readthedocs.org/projects/pandemic-overview/](https://readthedocs.org/projects/pandemic-overview/)

The build process is triggered via a webhook, a commit in this repo causes a GitHub Action which causes ReadTheDocs to rebuild their page

View Live Server so you can view it locally by clicking on the bottom-right status bottom bar of vscode to display a live working version of the html file being edited
