Flipkart Log Harvester System

Author

Kandan Logesh

Project Description

This project is a Python based Log Harvester System that collects log messages from a simulated Flipkart server using TCP socket communication. The harvest server receives logs from multiple clients, validates them using regular expressions, stores them in binary files according to their log level, and allows the stored logs to be viewed later.

The project demonstrates networking, multithreading, binary file handling, regular expressions, and data serialization using Python.

Features

Collects log data through TCP socket communication

Supports multiple client connections using multithreading

Validates incoming log messages with regular expressions

Stores logs in binary files using pickle

Separates logs based on INFO and ERROR levels

Reads and displays stored binary log records

Simple and easy to understand implementation

Technologies Used

Python

Socket Programming

Threading

Regular Expressions

Pickle

Binary File Handling

Project Files

harvest_server.py

server.py

readbinary.py

INFO.bin

ERROR.bin

Execution Steps

Run harvest_server.py to start the log harvesting server.

Run server.py in another terminal to send Flipkart log messages.

Run readbinary.py to display the stored log records from the binary files.

Sample Log Format

Timestamp | Server | Level | Message

Example

2026 07 12 10:30:15 | ORDER | INFO | Order Created

Learning Outcomes

Understanding TCP client server communication

Working with multithreading in Python

Using regular expressions for data validation

Storing structured data in binary files

Reading serialized data using pickle

Managing log files efficiently

Future Enhancements

Support additional log levels such as WARNING and CRITICAL

Store logs in a database

Provide a graphical user interface

Add log search and filtering features

Generate log analysis reports

License

This project is developed for educational and learning purposes.
