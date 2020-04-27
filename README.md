# Student Management API -- Prototype
## Overview
This repository is to implement RESTful APIs for a simple student system prototyping web services.
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
  
#### Return Values:
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
