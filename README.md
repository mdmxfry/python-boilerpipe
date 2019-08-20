# Boilerpipe Api Quickstart
### Before we start
Boilerpipe is Java library that provides algorithms to detect and remove the surplus "clutter" (boilerplate, templates) around the main textual content of a web page.

To read more about Boilerpipe: [https://boilerpipe-web.appspot.com/](https://boilerpipe-web.appspot.com/)

### Prerequisites
Tested on droplet: 1 CPU / 1 GB Memory / 25 GB Disk / Ubuntu 16.04/18.04

### Installation on a new machine

#### 1. Initial setup

* Connect to your server via ssh:

```
ssh root@SERVER_IP
```

* Create user with root privilidges

```
adduser boilerpipe 
```

* Create `docker` group and add `boilerpipe` user

```
sudo groupadd docker &&
sudo usermod -aG docker boilerpipe &&
sudo usermod -aG sudo boilerpipe
```

* Switch to created user

```
su boilerpipe
```

* Create SSH key and add to git account _(Optional. In case of private git repository with ssh keys)_

```
ssh-keygen -o -t rsa -b 4096 -C "email@example.com"
```

Keygen will ask 3 questions:

	Location to store public/private rsa key pair (default: /home/boilerpipe/.ssh/id_rsa): 

	Passphrase (empty for no passphrase):

	Repeat passphrase:

* When generating proccess would be finished it will show you a `fingerprint` and `randomart` image. To view generated public key type:

```
cat /home/boilerpipe/.ssh/id_rsa.pub
```

* Copy that key including `ssh-rsa` and your `email`, then add it to your git account.

#### 2. Install [Docker](https://www.docker.com/) 
* Command to install docker form official repository:

```
sudo apt-get update &&
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D &&
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main' &&
sudo apt-get update &&
sudo apt-get install -y docker-engine
```

* Make sure that docker is installed properly:

```
sudo systemctl status docker
```

Example of proper output:

```
docker-engine:
  Installed: (none)
  Candidate: 1.11.1-0~xenial
  Version table:
     1.11.1-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages
     1.11.0-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages

```
 (**q to exit**)

#### 3. Install docker-compose and git:

```
sudo apt-get install -y docker-compose && 
sudo apt-get install -y git-core
```

* Check docker-compose version

```
docker-compose --version
```

* **For Ubuntu release less than 18.04** 

In order to run `docker-compose.yml` of version `3.0`, you need to make sure that docker-compose is `1.13.0+` 

If it's not, please, use instruction below:

```
sudo apt-get remove docker-compose &&
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose &&
sudo chmod +x /usr/local/bin/docker-compose
```

### Installing boilerpipe-api

* Go to user working directory:

```
cd ~
```

* Clone git repository. 

_In case of private repository this operation could require username and password from your git account or ssh key_

```
git clone git@gitlab.com:turian/boilerpipe-api-mdmxfry.git
```

* Open folder with repository and run docker-compose

```
cd boilerpipe-api-mdmxfry 
```

* Run docker-compose

```
docker-compose up -d

```

**Usefull commands:**

* Launch docker-compose in direct way, without `--detach` flag:

```
docker-compose up
```

* Check if API is working:

```
curl localhost:8080
```

Response should be ``Hi, API is working``

_If you would like to change ``PORT``, please change ``PORT=8080`` line in ``.env`` file_

* Check launched docker containers:

```
docker ps
```

* Stop docker container:

```
docker stop boilerpipe-api-mdmxfry_boilerpipe_api_1
```

* Stop all docker containers:

```
docker stop $(docker ps -a -q)
```

* Rebuild and compose docker container:

```
docker-compose up -d --build
```

### How To Use

Python client example in **client.ipynb**
