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

Type: `make help` to see other commands

### Default User password

`pass123`

### How to debug the app with remote database connection

Here's some information on how to set up the environment so that you will be
connected to dev DB or produciton one using your local docker-compose setup.

1. Copy `.envrc.example` to `.envrc`

```bash
cp .envrc.example .envrc
```

2. Edit the `.envrc` file, paste in the secret values,
which you can get by asking one of the admins of our Infrastructure.

```bash
vim .envrc
```

3. Load the environment variables.
You can also install `direnv` for automatic loading, but it's not required.

```bash
source .envrc
```

4. Set up SSH tunnel to bastion. Config can be optained the same way as
secrets - by asking admins of Infrastructure.

```bash
ssh bastion
```

5. Restart the environment, open up shell or the application in browser.

```bash
make stop
make start
```

How to confirm that it works:

```bash
$ make bash
docker-compose exec backend bash
root@a68d3611d0e7:/cfp_v3/backend# env | grep DB
DB_PASSWORD=supersecretvalueasdasdadas
DB_PORT=55432
[...]
```

You can also open up flask shell to interact with the DB directly:

```bash
$ make bash
docker-compose exec backend bash
root@a68d3611d0e7:/cfp_v3/backend# flask shell
Python 3.8.8 (default, Feb 19 2021, 17:55:44)
[GCC 8.3.0] on linux
App: backend.app [development]
Instance: /cfp_v3/instance
>>>
>>> from backend.models import User
>>> User.query.all()
[<User 1>, <User 2>, <User 3>, <User 4>]
```

Once you set it up correctly then only steps 3-5 are required next time.

Please note that this isn't a real 1:1 reproduction of the live-like
environment beacuse we're skipping the AWS lambda execution and the
AWS Gateway proxy, but it shouldn't make any difference when developing the app.
