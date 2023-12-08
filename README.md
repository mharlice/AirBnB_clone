# AirBnB Clone

## Project Description

The AirBnB Clone project is a web application that mimics the basic functionality of the AirBnB website. It gives customers information about the AirBnB.

## Console

The console is a text-based interface that enables us to interact with the AirBnB Clone functionality. It supports various commands for managing objects such as creating, updating, and deleting instances of classes like User, Place, and Review.

## How to Start the Console

To start the AirBnB Clone command interpreter, you need to:
1. Clone the repository to your local machine:
2. cd into the AirBnB_clone directory.
3. Run ./console.py

## Usage: 
### In interactive mode:
```
MBP:AirBnB_clone User1$ ./console.py
(hbnb) 
(hbnb) Create BaseModel
f9bc61d8-e103-42f6-a646-4c573229134d
(hbnb) all BaseModel
{"BaseModel.8d3d24e3-c214-43d8-b8c0-67625bd9a4c2": 
{"id": "8d3d24e3-c214-43d8-b8c0-67625bd9a4c2", "__class__": "BaseModel", 
"created_at": "2023-12-06T10:25:09.564938", "updated_at": "2023-12-06T10:25:09.564985"}, "BaseModel.f9fc8e2a-bd46-4b94-b6af-d74f95e1f9ed": 
{"id": "f9fc8e2a-bd46-4b94-b6af-d74f95e1f9ed", "__class__": "BaseModel", "created_at": "2023-12-06T10:35:06.813156", "updated_at": "2023-12-06T10:35:06.813211"}, 
"BaseModel.f9bc61d8-e103-42f6-a646-4c573229134d": 
{"id": "f9bc61d8-e103-42f6-a646-4c573229134d", "__class__": "BaseModel", "created_at": "2023-12-06T10:59:21.412718", "updated_at": "2023-12-06T10:59:21.412764"}}
(hbnb) quit
MBP:AirBnB_clone User1$
 
```
### In non-interactive mode: 
```
MBP:AirBnB_clone User1$ echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  create  destroy  help  quit  show

MBP:AirBnB_clone User1$ 
```
