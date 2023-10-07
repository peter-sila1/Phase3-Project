# Phase3-Project
# VMS (Visitor Management System) CLI

A command-line interface (CLI) for managing visitors, offices, and visits in a Visitor Management System (VMS).

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [CLI Commands](#cli-commands)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)


## Introduction

The VMS CLI is a tool for efficiently managing visitors, offices, and visits in a Visitor Management System. It provides a simple and intuitive command-line interface for performing various tasks related to visitor management.

## Features

- **Visitor Management**: Add, list, update, and delete visitor records.
- **Office Management**: Add, list, and delete office records.
- **Visit Management**: Add, list, update, and delete and searches visit records.
- **Data Validation**: Ensures data consistency and validation, such as email format.
- **Timestamps**: Automatically records timestamps for visits.
- **Database**: Utilizes SQLAlchemy for database modeling and Alembic for database migrations.
- **CLI**: Powered by the Click library for creating a robust command-line interface.
- **Package Management**: Uses Pipenv (Pipfile) for dependency management.

## Installation

1. Clone this repository to your local machine:
   `git clone https://github.com/yourusername/vms-cli.git`
    `cd vms-cli`
2. Create a virtual environment and install project dependencies using Pipenv:
`pip install --user pipenv`
3. Activate the virtual environment:
`pipenv shell`

## Usage
## CLI Commands
The VMS CLI provides the following commands:

- `visitor`: Manage visitor records.
- `office`: Manage office records.
- `visits`: Manage visit records.

Here are some examples of how to use these commands:

### Visitor Management
- Add a new visitor:
`python cli.py visitor create --name "Peter Sila" --email "peter@example.com"`

- List all visitors:
`python cli.py visitor list`

- Update a visitor's information (replace VISITOR_ID, NEW_NAME, and NEW_EMAIL with actual values):
`python cli.py visitor update VISITOR_ID --new_name "New Name" --new_email "new.email@example.com"`

- Delete a visitor (replace VISITOR_ID with the actual visitor ID):
`python cli.py visitor delete VISITOR_ID`


### Office Management

- Add a new office:
`python cli.py office add --name "Office Name"`

- List all offices:
`python cli.py office list`

- Delete an office (replace OFFICE_ID with the actual office ID):
`python cli.py office delete OFFICE_ID`

### Visit Management
- Add a new visit (the visitor and office are linked automatically, you only provide PERSON_VISITED):
`python cli.py visits add --person-visited "John Smith"`

- List all visits:
`python cli.py visits list`

- Delete a visit (replace VISIT_ID with the actual visit ID):
`python cli.py visits delete VISIT_ID`


## Technologies Used
- `SQLAlchemy`: For modeling and interacting with the database.
- `Alembic`: For database schema migrations.
- `Click`: For creating the command-line interface.
- `Pipenv`: For package management and virtual environment.
- `Python 3`: The programming language used to build the CLI.


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/issue-description`.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Author: `Peter Sila`
