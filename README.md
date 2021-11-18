# ODP App template

This template-project includes the basic building blocks needed to deploy and application to our platform.

The components of this template:

* Example application
    - Python flask-application
* Dockerfile
* Azure DevOps pipeline definition

## Getting started

### Installation

In order to use this template, you must first install cookiecutter. This is simply done with pip

```shell
$ pip install cookiecutter
```

Windows users may need to do some extra steps. Please refer to
the [cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html).

### Usage - Directly from remote Git repo

Simply run cookiecutter to generate your project:

```shell
$ cookiecutter git+https://oceandatafoundation@dev.azure.com/oceandatafoundation/ODP/_git/app-template
```

Cookiecutter will prompt your to input some options, then finally generate a new directory containing the full project
and named by cookiecutter based on the `project_name` you specified.

### Usage - Using local template

First clone this project template:

```shell
$ git clone https://oceandatafoundation@dev.azure.com/oceandatafoundation/ODP/_git/app-template <MY_DIR>/app-template
```

You can then generate your own project using cookiecutter:

```shell
$ cookiecutter <MY_DIR>/app-template
```

Cookiecutter will prompt your to input some options, then finally generate a new directory containing the full project
and named by cookiecutter based on the `project_name` you specified.


## Template description

### Example Python Application

This application serves as a placeholder for your application. It also includes some packages to serve as inspiration
for app-developers:

* **[Poetry](https://python-poetry.org/) Package manager** - A modern Python package manager
* **[Click](https://click.palletsprojects.com/en/8.0.x/options/#boolean-flags)** - Parser for command-line arguments
* **[Flask](https://flask.palletsprojects.com/en/2.0.x/)** - Web-framework for Python

### Dockerfile

The Dockerfile holds the definition of the containerized environment your application will run in.

If your project is a simple Python {{cookiecutter.python_version}} app that uses Poetry as its package manager, you will
likely not have to make any changes to this file. If your uses different ports or needs custom assets such as images,
then you may have to update this file.

## Azure DevOps pipeline definition

The Azure DevOps pipeline definition, located at `.azure-devops/pipelines/azure-pipeline.yml`, holds instructions on how
to build and deploy your application. It has to be manually deployed from Azure DevOps in order to use it.

The pipeline consists of two jobs - `Build` and `Deploy`. `Build` will build the Dockerfile and save the resulting image
to our Azure Container Registry. `Deploy` will deploy the application using the definition in
`deployment_config.yml`.

This template is built in such a way that you should not need make any changes to the `azure-pipeline.yml`-file.
However, if you have more than one Dockerfile or your app requires specialized build-steps, then you will need to update
this file.

### Using `deployment_config.yml`

`deployment_config.yml` is processed by
the [`app-deployer`](https://dev.azure.com/oceandatafoundation/ODP/_git/app-deployer), and holds all the information
necessary to deploy your app. Here you can add supporting services, configure the deployment URL and add environment
variables.
