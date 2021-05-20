# codeforpoznan.pl_v3

[![Build Status](https://travis-ci.com/CodeForPoznan/codeforpoznan.pl_v3.svg?branch=master)](https://travis-ci.com/CodeForPoznan/codeforpoznan.pl_v3)
[![Join Slack](https://img.shields.io/badge/slack-join%20chat-4a154b)](https://join.slack.com/t/codeforpoznan/shared_invite/zt-8a7u52j8-yqB01C2YgYF4Lvd1pFM_jw)

## General Overview of the Project
This is internal project maintained by our community for our comminity. 

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
* [Design - tasks that could use UX experise]()

## How to get started
1. Join codeforpoznan_v3 channel on [our slack](https://join.slack.com/t/codeforpoznan/shared_invite/zt-8a7u52j8-yqB01C2YgYF4Lvd1pFM_jw) - this is the place where we discuss all the issues and help each other by sharing tips and knowledge. You can also ping @Otis in the private channel if you need any help.
2. Fork the repository onto your github account, choose the location on your computer where you want to keep it  and ```git clone PASTE URL``` in the terminal, using the URL link from your copy of the repo - this way any commit you push will affect only your fork (so you can break anything you like).
3. Install docker according to the instruction you'll fine [here](https://docs.docker.com/engine/install/) to run and develop the app locally on your computer. Once you do it, got to the location of the repo on your computer and run command ```make start``` in the terminal (add ```sudo``` before the command in case of permission troubles) you'll be able to access the frontend on ```localhost:8080``` and push requests to backend on ```localhost:5000```.
4. Choose a task from one if the lists below and leave a comment that you're gonna work on it.
5. We like to keep ```master``` branch clean so create a new branch ```git checkout -b BRANCH NAME``` - name the branch descriptively e.g. ```update_something``` so that you know what's there. Then, switch branch ```git checkout update_something``` and start developing!
6. Once you're finished ```git add .``` your changes, ```git commit -m "description of changes"``` describing shortly what's happening there and ```git push origin update_something``` so it gets pushed to your github. Then,  go to [our repo](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/pulls), make "new pull request" and find your branch on "compare" list. Describe briefly the changes and "create pull request" to leave it for others to review your code. 

### Wanna start with somthing simple?
* [Good first issue - simple tasks that don't hurry](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22+-label%3A%22Refinement+needed%22+sort%3Acreated-asc+-label%3A%22UX+needed%22+-label%3A%22content+needed%22+no%3Aassignee)
* [Debugging - tasks that help us solve problems](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3Abug+-label%3A%22Refinement+needed%22+-label%3A%22UX+needed%22+no%3Aassignee+sort%3Acreated-asc)

### Wanna work on something more advanced?
* [Frontend - we use Vue, Vuex and Axios](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3Afrontend+-label%3A%22good+first+issue%22+-label%3A%22Refinement+needed%22+-label%3A%22UX+needed%22+-label%3Abug+no%3Aassignee+sort%3Acreated-asc)
* [Backend - we use flask and postgreSQL](https://github.com/CodeForPoznan/codeforpoznan.pl_v3/issues?q=is%3Aopen+is%3Aissue+label%3Abackend+-label%3A%22content+needed%22+-label%3A%22Refinement+needed%22+-label%3A%22good+first+issue%22+-label%3A%22UX+needed%22+no%3Aassignee+sort%3Acreated-asc+-label%3Abug)


## Development environment

We use Docker for development purposes. To start working, your computer needs to support it.

### Commands

| command      | what it does   |
|--------------|----------------|
| `make start` | starts project |
| `make stop`  | stops project  |
| `make logs`  | shows logs     |
| `make test`  | runs tests     |
| `make lint`  | runs linters   |

Type `make help` to see other commands.

### Default User password

`pass123`

### How to debug the app with remote database connection

---
> Please note that this step is optional.
> You most likely do not need to follow it.
---

Here's some information on how to set up the environment
so that you will be connected to dev DB or produciton
one using your local docker-compose setup.

</br>

#### 1. Copy `.envrc.example` to `.envrc`

This is needed to avoid making changes to the
`.envrc.example` file which could be commited by
accident, because it's not ignored.  
On the other hand, `.envrc` is ignored,
so it's safe to modify it without ever worrying about
commiting it by accident.


```bash
# run this in terminal, in the project directory
cp .envrc.example .envrc
```

</br>

#### 2. Edit the `.envrc` file using your favourite text editor

Replace the secret values (database name, login, password secret key).
You can get by asking one of the admins of our
Infrastructure  
([@arturtamborski](https://github.com/arturtamborski)
& [@magul](https://github.com/magul))
and stating your need for it.

```bash
# edit with `vim`, `code`, or whatever you like :)
code .envrc
```

</br>

#### 3. Load the modified environment variables into your terminal

We've just modified the `.envrc` file with secrets,
but they are not used by default, we first have to load
them using `source` command in terminal.  
There are two ways of doing that.

You can do that manually:

```bash
# run this in terminal, in the project directory
source .envrc
```

or you can install [direnv](https://direnv.net/)
which will load it automatically for you, but this
program is not required.

</br>

#### 4. Set up SSH tunnel to CodeForPoznan's bastion

SSH config can be obtained the same way as
secrets - by asking admins of Infrastructure.

In order to set up this SSH tunnel you'll need:

- SSH access to codeforpoznan-bastion (ask admins)
- SSH config of the connection (ask admins)
- new terminal window (the tunnel will keep your terminal busy)

```bash
# ask admins for config of `.ssh/config` and bastion
# run this command in new terminal
ssh codeforpoznan-bastion
```

</br>

#### 5. Restart the environment

This is required in order to load the newly modified
and sourced environment variables so that the values
can be used by docker and by backend app.  
Again, environment variables are not automatically
passed over on their change, so we need to give it
a little push for this to work.

```bash
# run this in terminal, in the project directory
make stop
make start
```

</br>

How to confirm that it works:

```bash
# this will open up shell in backend container
$ make bash

# in the container, view all environment variables
root@a68d3611d0e7:/cfp_v3/backend# env | grep DB
DB_PASSWORD=super-secret-value-will-be-shown-here
DB_PORT=55432

# I've cut the output here, more vars should follow
[...]
```

Notice that the environment variables are showing the
secret strings that you've typed in the `.envrc` file.
This tells us that everything worked well - docker
used our environment variables which were loaded by
us from the `.envrc` file.

Other way of checking if everything's fine is to
open up flask shell and interact with the DB directly:

```bash
# this will open up shell in backend container
$ make bash

# open up flask shell, interactive python session
root@a68d3611d0e7:/cfp_v3/backend# flask shell
Python 3.8.8 (default, Feb 19 2021, 17:55:44)
[GCC 8.3.0] on linux
App: backend.app [development]
Instance: /cfp_v3/instance
>>>
>>> from backend.models import User  # import model
>>> User.query.all()                 # run test query
[<User 1>, <User 2>, <User 3>, <User 4>]
```

You can see that it fetched users from different databse
by inspecting the details of fetched objects.

</br>

Once you set up the `.envrc` correctly only steps 3-5
are required to use this connection again.

Please note that this isn't a real 1:1 reproduction of
the live-like environment beacuse we're skipping the AWS
lambda execution and the AWS Gateway proxy, but it
shouldn't make any difference when developing the app.  
Another thing to note is to not rely on this method for
regular debugging. It's very useful in some situations
when you have no idea what's going on or when there's
a very specific bug to resolve, but generally, the 99%
of cases are possible to solve without connecting to
live DB but instead to rely on the local environment.
