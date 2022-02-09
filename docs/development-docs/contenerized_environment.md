## Running the app locally
For local development purposes we use [docker](https://www.docker.com/) to create contenerized environment. It means that all the parts of the app: frontend, backend and database are being run concurrently and continously in the indefinite loop until they are told to stop (learn more [here](https://www.docker.com/resources/what-container)). 

## Why do we do it like that?
There are few good reasons to organize project like this.
1. It simulates real-life communication between frontend, backend and database which makes development that much easier.
2. All the containers are built from the same tamplate. So as long as you updated you local copy of github repository you'll be working on exactly the same env as others (no more "works on my machine" problem).

## Using docker
* To use docker you need to install it first. You can find the most current instructions [here](https://docs.docker.com/engine/install/). 
* Running docker requires root access forcing you to use `sudo` before each command. Otherwise permission issues will pop out. You can avoid that following [this instruction](https://docs.docker.com/engine/install/linux-postinstall/).

## Maintenance
Docker caches a lot of things not to download them every time you get the local env running. So when:

1. You don't see the effect of major dependency update;
2. You face some bug that should not have been happening;

```bash
# you may find it useful to
docker image rm $(docker image ls)
```
---
>Once in a while it is also good to clean up all the resources to free up some space. In this case [here](https://gist.github.com/bastman/5b57ddb3c11942094f8d0a97d461b430) you'll find a nice guide to it.
---
