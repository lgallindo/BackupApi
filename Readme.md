# Backup API

[![PyPI](https://img.shields.io/pypi/pyversions/BackupApi.svg)]()
![](https://img.shields.io/travis/michagrandel/BackupApi/develop.svg)
![](https://img.shields.io/codecov/c/github/michagrandel/BackupApi/develop.svg)
![GitHub release](https://img.shields.io/github/release/michagrandel/BackupApi.svg)
![PyPI](https://img.shields.io/pypi/v/BackupApi.svg)
[![license](https://img.shields.io/github/license/michagrandel/BackupApi.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

This **Backup API** let's you *upload* and *store* images from your computer
to a cloud service like Google Photos. You can use this to Backup Photos
from your Computer.

## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes. See deployment for notes on 
how to deploy the project on a live system.

### Prerequisites

This project is based on [Flask][flask] and [Python 2.7.x][python]. 
The Backup API is made to run on a server. It assumes a setup like the one
used at uberspace.de, i.e. CentOS 6 or higher, Apache 2 and FastCGI.



#### Install on your local machine


However, you can also run it locally. To prepare for installation, make sure, you have at least [Python 2.7][python] and 
[pip][pip] up and running!

On **Windows**, download the [latest version of Python 2.7][python] and install it.
Make sure to set your **PATH** variable accordingly!

If you need help on Windows, you will find more information in the
[Python 2 Installation guide][How To Install Python 2.7.md].

On **macOS** and most **Linux**, python is pre-installed. There is no need to install
anything as a prerequisite.


### Installing

#### Install on any server or local machine

Bare in mind that the Backup API was written with a uberspace server in mind.
This means, it assumes Apache 2 and FastCGI.

You may have to customize the API to fit your needs if not using uberspace.

It should be sufficient to change the `script/backup.fcgi`.

#### Install on a uberspace Server

Download the Backup API and extract:

```bash
[jasmin@fornax ~]$ url="`curl -s https://api.github.com/repos/michagrandel/BackupApi/releases/latest | grep tarball_url | cut -d '"' -f 4`"
[jasmin@fornax ~]$ wget $url -O BackupAPI.tar
[jasmin@fornax ~]$ tar -xvf BackupAPI.tar > name.txt
[jasmin@fornax ~]$ mv $(head -n 1 "name.txt") BackupAPI
[jasmin@fornax ~]$ rm BackupAPI.tar name.txt
```

Install the python module:

```
[jasmin@fornax ~]$ cd ~/BackupAPI 
[jasmin@fornax BackupAPI]$ python2.7 setup.py install
```

Copy the content of the script directory into `~/fcgi-bin`:

```bash
[jasmin@fornax ~]$ cp ~/BackupAPI/script/* ~/fcgi-bin/
```

You are ready!


## Running the tests

If you like to run the tests, just open a terminal in the project directory and run:

```
python -m unittest discover -s ~/BackupAPI/test -p "*_test.py"
```

## Built With

*
* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

First of all: Thank you very kindly for your interest in contributing to our code!

Please take a moment and read [CONTRIBUTING.md](Contributing.md) to get you started!

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, 
see the [releases on this repository][github-releases]. 

## Authors

* **Micha Grandel** - *Author and maintainer* - [Github][github]

We thank all of our [contributors][github-contributors], 
who participated in this project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) 
file for details

<!--## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
-->

[github]: https://github.com/michagrandel
[github-releases]: https://github.com/michagrandel/BackupApi/releases
[github-contributors]: https://github.com/michagrandel/BackupApi/graphs/contributors
[python]: https://www.python.org/downloads/
[pip]: https://pypi.python.org/pypi/pip
[flask]: http://flask.pocoo.org
[gitflow]: https://danielkummer.github.io/git-flow-cheatsheet/
[gitflow-model]: http://nvie.com/posts/a-successful-git-branching-model/