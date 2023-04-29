# Grade Management System

This project was created as part of the Inclusão Tech course at Gama Academy in partnership with Ipiranga. The purpose of the system is to assist in the management of student grades, allowing for the calculation of the annual average and recording of the bimonthly grades and final averages in a SQLite3 database.

## Files

- gestnotas.py: Module responsible for grade management. This module performs the calculation of the annual average and inserts the bimonthly grades and averages into the SQLite3 database.
- login_process_esc.py: Login system based on the registration of users and roles registered in the database. This module is not yet fully functional, although it can be executed.
- main.py: Main file that imports the other two modules.

The main.py file is responsible for integrating the modules and running the system. The other modules can be executed independently, but to use all of the system's features, it is necessary to execute the main.py file.

## Known Issues

- login_process_esc.py: The module is not yet fully functional, although it can be executed.

## How to run

To run the system, you must have Python 3 (works best with 3.11+) and the PySide6 package. After cloning the repository, simply run the main.py file.

## How to contribute

Pull requests are welcome and will be evaluated. If you find any bugs or have any suggestions for improvement, please open an issue in the repository.
