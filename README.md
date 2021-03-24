# codeforpoznan.pl_v3

[![Build Status](https://travis-ci.com/CodeForPoznan/codeforpoznan.pl_v3.svg?branch=master)](https://travis-ci.com/CodeForPoznan/codeforpoznan.pl_v3)

Next version of Code for Poznan's website.

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
