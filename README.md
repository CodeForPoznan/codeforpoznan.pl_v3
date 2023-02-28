# codeforpoznan.pl_v3

[![deploy to staging](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/actions/workflows/deploy-staging.yml/badge.svg)](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/actions/workflows/deploy-staging.yml)
[![Join Slack](https://img.shields.io/badge/slack-join%20chat-4a154b)](https://join.slack.com/t/codeforpoznan/shared_invite/zt-8a7u52j8-yqB01C2YgYF4Lvd1pFM_jw)

## General Overview of the Project
This is internal project maintained by our community for our community. 

First, we maintain the landing page that contains information about 
our community and the projects we carry out for other organizations 
that help them do good more easily or efficiently. They don't have much money 
and software development is expensive. We simply try to bridge that gap 
with our voluntary work to balance the scales.

Second we develop the intranet for our community. We try to create the tools 
which can help us organize ourselves better by storing the relevant information
in one place, streamlining our practices and managing our responsibilities. 
If you want to learn the general direction we try to accomplish, here you'll 
find the general description of features we pursue at the moment:
[Features we currently pursue](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3AEpic)

### Wanna help us develop the product?
* [Content - tasks that need some writing](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3A%22content+needed%22+sort%3Acreated-asc)
* [Design - tasks that could use UX expertise](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3A%22UX+needed%22)

## How to get started

---
> Join codeforpoznan_v3 channel on [our slack](https://join.slack.com/t/codeforpoznan/shared_invite/zt-8a7u52j8-yqB01C2YgYF4Lvd1pFM_jw) - this is the place where we discuss all the issues and help each other by sharing tips and knowledge. You can also ping [OtisRed](https://github.com/OtisRed) on github or @Otis in the slack DM if you need any help.
---

#### 1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) onto your github account. Go to your account and open repo you just copied. Find the "Code" button and copy HTTPS adress unless you're [using SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) or GitHub CLI. Then:  
```bash
# Open the terminal, choose the location on your computer where you want to keep it and paste in the command: 
git clone https://github.com/YOUR_USERNAME/codeforpoznan.pl_v3.git
```
This way any commit you push will affect only your fork (so you can break anything you like).

#### 2. [Install docker](https://docs.docker.com/engine/install/) to run the app locally on your computer. 
```bash
# Once you install it, go to the location of the repo on your computer and run command: 
sudo make start 
```
Now you'll be able to access Frontend in you browser tab under the URL: ```localhost:8080``` and push requests to backend on ```localhost:5000```
(if you don't want to use ```sudo``` follow the instructions [here](https://docs.docker.com/engine/install/linux-postinstall/)).

#### 3. Choose a task from one if the lists below 
Please leave a comment that you're gonna work on it.

#### 4. Create a new branch for your commits 
We like to keep master branch clean so:
```bash
# create a new branch and name it descriptively starting with number of your task e.g. "123_UPDATE_SOMETHING":
git checkout -b 123_BRANCH_NAME
```
```bash
# Then, switch to your new branch that branch with command: 
git checkout 123_UPDATE_SOMETHING
```
Now you can start developing and commiting your changes!

#### 5. Push your changes to main repo
Once you're finished, run four commands to commit your changes. 
```bash
# First check your changes:
git status
# which will print the list of files you altered.
```
```bash
#add changed files to your commit: 
git add NAME/OF/THE.FILE
```
```bash
# Then wrap the commit and describe what's happening there:
git commit -m "BRIEFLY DESCRIBE YOUR CHANGES"
``` 
```bash
# Finally push the commit to your forked repo:
git push origin 123_UPDATE_SOMETHING
``` 
Then, go to our repo [here](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/pulls), make "new pull request" and find your branch on "compare" list. Provide a short description of the changes you made and "create pull request" so that others could review your code. 

### Wanna start with somthing simple?
* [Good first issue - simple tasks that don't hurry](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22+-label%3A%22Refinement+needed%22+sort%3Acreated-asc+-label%3A%22UX+needed%22+-label%3A%22content+needed%22+no%3Aassignee)
* [Debugging - tasks that help us solve problems](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3Abug+-label%3A%22Refinement+needed%22+-label%3A%22UX+needed%22+no%3Aassignee+sort%3Acreated-asc)

### Wanna work on something more advanced?
* [Frontend - we use Vue, Vuex and Axios](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3Afrontend+-label%3A%22good+first+issue%22+-label%3A%22Refinement+needed%22+-label%3A%22UX+needed%22+-label%3Abug+no%3Aassignee+sort%3Acreated-asc)
* [Backend - we use flask and postgreSQL](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3Abackend+-label%3A%22content+needed%22+-label%3A%22Refinement+needed%22+-label%3A%22good+first+issue%22+-label%3A%22UX+needed%22+no%3Aassignee+sort%3Acreated-asc+-label%3Abug)

## Documentation
You may want to familiarize yourself with our:
* [Github flow](https://github.com/CodeForPoznan/Community/blob/master/knowledge-base/github-flow.md) - a short cheatsheet with most needed commands in git.
* [Building local environment](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/blob/master/docs/development/contenerized_environment.md) - explains why we use docker and offers few maintenance hints. 
* [Our developer shorthands](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/blob/master/docs/development/developer_shorthands.md) - contains the list of makefile commands that we find the most handy.
* [How to mock data](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/blob/master/docs/development/mocking_database.md) - contains information on how to fake data for testing and development reasons.
---
> You will find more documentation on these and other more specific topics in the [docs folder](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/tree/master/docs). 
---
