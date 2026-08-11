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

## task 2

# Superstore Sales & Profit Analysis

Exploratory data analysis (EDA) of the **Sample Superstore** dataset using Python, Pandas, and Seaborn/Matplotlib. The project investigates sales, profit, and discount patterns across product categories to answer key business questions.

## Dataset

`samplesuperstore.csv` — retail order-level data with the following fields:

| Column | Description |
|---|---|
| Row ID, Order ID | Record and order identifiers |
| Order Date, Ship Date | Order and shipping dates |
| Ship Mode | Shipping method used |
| Customer ID, Customer Name, Segment | Customer details |
| Country/Region, City, State/Province, Postal Code, Region | Location details |
| Product ID, Category, Sub-Category, Product Name | Product details |
| Sales, Quantity, Discount, Profit | Order financials |

## Project Structure

```
├── samplesuperstore.csv     # Raw dataset
├── superstore.py            # Analysis script (converted from Colab notebook)
└── README.md
```

## Requirements

```
pandas
numpy
matplotlib
seaborn
```

Install with:

```bash
pip install pandas numpy matplotlib seaborn
```

## What the Script Does

1. **Data Loading & Cleaning**
   - Loads the CSV into a DataFrame
   - Converts `Order Date` and `Ship Date` to datetime
   - Computes a new `Delivery Days` column (Ship Date − Order Date)
   - Checks for missing values

2. **Sales Overview**
   - Aggregates total sales by `Category`
   - Plots a bar chart of sales by category
   - Plots a histogram of the overall sales distribution

3. **Bar Plots — Category Comparison**
   - Profit by Category
   - Sales Distribution by Category

4. **Box Plots — Distribution & Outliers**
   - Overall profit distribution
   - Profit variation across categories

5. **Discount vs. Profit Analysis**
   - Scatter plot of Discount vs. Profit to identify the discount level at which profitability starts to decline

6. **Correlation Heatmap**
   - Correlation matrix of numeric fields (Sales, Quantity, Discount, Profit)
   - Visualized as a heatmap to reveal relationships between variables

## Key Questions Explored

- Which category generates the maximum profit?
- How does profit vary (and what outliers exist) across categories?
- At what discount level does profit start decreasing?
- How are Sales, Quantity, Discount, and Profit correlated?

## How to Run

1. Place `samplesuperstore.csv` in the same directory as the script (or update the file path).
2. Run the script:

```bash
python superstore.py
```

Each plot will display in sequence. If running outside a notebook environment, add `plt.show()` calls are already included, so plots will pop up as separate windows.

## Notes

- Originally developed in Google Colab; file-upload cells (`google.colab.files.upload()`) can be removed or replaced with a local file path when running outside Colab.
- Update the `pd.read_csv(...)` path to match your local file location.

## License

This project is for educational/analytical purposes.
