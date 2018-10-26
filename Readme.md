# How to use odo to debug a python application on openshift with a postgesql database

## Summary

This project contains the sources for a demo application using python and postgresql to show how to setup and debug a python application with openshift and the odo and oc commands. The debugger we'll be using is ptvsd and Visual Studio Code.

We will setup the application in openshift, deploy a sample database, fill it with some data and display it with the sample application.

We will then setup the 

## Prerequisites

1. [vscode](https://code.visualstudio.com/Download)
2. [git](https://git-scm.com/downloads)
3. [oc](https://github.com/openshift/origin/releases)
4. [odo](https://github.com/redhat-developer/odo/releases)
5. Access to an openshift instance (version > 3.10)

## Project creation

1. Log into Openshift with an empty project

2. Create the application and the python component with odo

```sh
odo app create python-test

odo create python

```

3. Add the postgresql database

```sh
odo service create postgresql-persistent

odo link postgresql-persistent --component python
```

This will create a new instance of postgresql and link it to our new component. This means that new environment variables will be available in the python pod:

* database_name
* password
* uri
* username

These variables will be available in the python pod.


4. Push the application code and configure the database

```sh
odo push

oc get pods

oc rsh python-<hash>

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

5. Insert sample data in the database

```sh
oc rsh postgres-<hash>

psql sampledb
insert into tests(mydata) values ('this'),('is'),('a'),('test');
```

6. Check the application is working

Create a url for the application

```sh
odo url create
```

Go to the url that has been created and the application should be there

7. Debug the application

We need to connect on port 5678 of the python process running in the pods. To allow that we will forward the 5678 port of the pod to the port 5678 of our local environement

```sh
oc port-forward python-<pod id> 5678
```

Then we can use the "Attach (Remote Debug)" configuration to connect to the application and debug it.



