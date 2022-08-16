# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## How to use this template

<!--
TODO: Remove this section
-->

This template-project includes the basic building blocks needed to deploy and
application to our platform.

The components of this template:

- Example application
  - Python Tornado-application
- Dockerfile
- Azure DevOps pipeline definition

## Example Python Application

This application serves as a placeholder for your application. It also includes
some packages to serve as inspiration for app-developers:

- **[Poetry](https://python-poetry.org/) Package manager** - A modern Python
  package manager
- **[Click](https://click.palletsprojects.com/en/8.0.x/options/#boolean-flags)** -
  Parser for command-line arguments

* **[Tornado](https://www.tornadoweb.org/en/stable/)** - Async Web-framework for

### Dockerfile

The Dockerfile holds the definition of the containerized environment your
application will run in.

If your project is a simple Python {{cookiecutter.python_version}} app that uses
Poetry as its package manager, you will likely not have to make any changes to
this file. If your uses different ports or needs custom assets such as images,
then you may have to update this file.

In order to build the Dockerfile, simply run the following command:

```shell
$ docker build --rm -t oceandata.azurecr.io/{{cookiecutter.project_slug}}:{{cookiecutter.version}}
```

The container image can then be run locally using the following command:

```shell
$ docker run -p 5000:5000 -it oceandata.azurecr.io/{{cookiecutter.project_slug}}:{{cookiecutter.version}}
```

We recommend running your container image locally before deploying the app to
the cloud

### Azure DevOps pipeline definition

The Azure DevOps pipeline definition, located at
`.azure-devops/pipelines/azure-pipeline.yml`, holds instructions on how to build
and deploy your application. It has to be manually deployed from Azure DevOps in
order to use it.

The pipeline consists of two jobs - `Build` and `Deploy`. `Build` will build the
Dockerfile and save the resulting image to our Azure Container Registry.
`Deploy` will deploy the application using the definition in
`deployment_config.yml`.

This template is built in such a way that you should not need make any changes
to the `azure-pipeline.yml`-file. However, if you have more than one Dockerfile
or your app requires specialized build-steps, then you will need to update this
file.

### Using `deployment_config.yml`

`deployment_config.yml` is processed by the
[`app-deployer`](https://dev.azure.com/oceandatafoundation/ODP/_git/app-deployer),
and holds all the information necessary to deploy your app. Here you can add
supporting services, configure the deployment URL and add environment variables.
