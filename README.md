# Student Management API -- Prototype
## Overview
This repository is to implement a RESTful API of a simple student system prototyping web services.
CRUD interfaces are provided for students and schools. school and students is in one-many relationship. Token-Based 
Authentication is also provided.

## Endpoints
* POST /register
* POST /login
* POST /logout
* DELETE /user/{username}


* GET /students 
* GET /student/{id}
* POST /student/{id}
* DELETE /student/{id}

* GET /schools 
* GET /school/{id}
* POST /school/{id}
* DELETE /school/{id}

### Return Values:
* 200 OK
* 201 CREATED
* 400 BAD REQUEST
* 404 NOT FOUND
* 500 INTERNAL SERVER ERROR

## Requirements
Refer to .Pipfile

## System Design
### Technical
* Python 3.7+
* Flask - an extensible web micro framework for building web applicaitons
* SQLAlchemy - Python SQL toolkit and object-relational mapper that gives application developers the full power and 
flexibility of SQL
* Marshmallow - simplified object serialization; an ORM/ODM/framework-agnostic library for converting complex datatypes
* Flask-RESTX - an extension for Flask that adds support for quickly building REST APIs. It provides a coherent 
collection of decorators and tools to describe API and expose its documentation properly using Swagger






```bash
brew cask install java
```
* Install Scala
```bash
brew install Scala
```
* Install Apache Spark
```bash
brew install apache-spark
```
* Install Python
```bash
brew install python3

## Requirements
* Spark
* Python3
* pyspark

### Installation Guide on Mac
* Install Java
```bash
brew cask install java
```
* Install Scala
```bash
brew install Scala
```
* Install Apache Spark
```bash
brew install apache-spark
```
* Install Python
```bash
brew install python3
```
* Install pyspark
```bash
pip3 install pyspark
```

### Running the Application 
* Run in a standalone local env
```bash
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.5/libexecexport

$Spark_HOME/bin/spark-submit --master local <working_directory>/spark_test.py
```

### Starting a standalone cluster
* Manual Launch
  * Start the master process on the machine that we want to run on. Then the masterprints out a spark://HOST:PORT URI ( http://master-ip-address:8080 by default ) 
 ```bash
        $SPARK_HOME/sbin/start-master.sh
``` 
-  * Start worker nodes by logging into each machine and running the following script using the URI you just received from the master node.
 ```bash
        $SPARK_HOME/sbin/start-slave.sh <master-spark-URI>
```
* Cluster launch scripts
  * Create conf/slaves in your Spark directoryto contain the hostnames of all the machines one per line. The master will 
  access workers via SSH which needed to be setup. Then launch or stop your cluster by scripts. Details at [here](http://spark.apache.org/docs/latest/spark-standalone.html#cluster-launch-scripts)
  
  ```bash
      $SPARK_HOME/sbin/start-all.sh 
      $SPARK_HOME/sbin/stop-all.sh
    ```

* Run a Python application on a Spark standalone cluster. Details at [here](https://spark.apache.org/docs/latest/submitting-applications.html)
```bash
./bin/spark-submit \
  --master spark://207.184.161.138:7077 \
  examples/src/main/python/pi.py
```


