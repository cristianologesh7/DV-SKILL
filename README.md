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
# SuperStore Sales Data Analysis

## Project Overview

This project analyzes the SuperStore sales dataset using Python. The objective is to explore sales performance, customer behavior, product categories, and regional trends through data cleaning, exploratory data analysis (EDA), and data visualization.

---

## Objectives

- Clean and preprocess the dataset.
- Perform Exploratory Data Analysis (EDA).
- Analyze sales, profit, and discount trends.
- Identify top-performing categories and sub-categories.
- Visualize business insights using charts.
- Generate meaningful conclusions from the data.

---

## Dataset

**Dataset:** `sample_-_superstore.csv`

The dataset contains information about customer orders, including:

- Order ID
- Order Date
- Ship Date
- Customer Name
- Segment
- Country
- State
- Region
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Analysis Performed

- Data Loading
- Data Cleaning
- Missing Value Analysis
- Duplicate Removal
- Data Type Conversion
- Descriptive Statistics
- Sales Analysis
- Profit Analysis
- Category-wise Analysis
- Region-wise Analysis
- Data Visualization

---

## Visualizations

The notebook includes the following visualizations:

- Sales Distribution
- Profit Distribution
- Category-wise Sales
- Region-wise Sales
- Sub-Category Analysis
- Correlation Heatmap
- Bar Charts
- Histograms
- Box Plots

---

## Key Insights

- Identified the highest-selling product categories.
- Compared sales across different regions.
- Analyzed the impact of discounts on profit.
- Identified profitable and loss-making products.
- Observed customer purchasing trends.

---

## Installation

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

## How to Run

1. Clone the repository.
2. Place the dataset (`sample_-_superstore.csv`) in the project folder.
3. Open `SuperStore.ipynb` using Jupyter Notebook.
4. Run all cells to reproduce the analysis.

---

## Project Structure

```
SuperStore/
│── SuperStore.ipynb
│── sample_-_superstore.csv
└── README.md
```

---

## Future Enhancements

- Build an interactive dashboard using Power BI or Tableau.
- Develop a sales forecasting model.
- Perform customer segmentation using machine learning.
- Deploy the project as a web application.

---

## Conclusion

This project demonstrates how Python can be used for data cleaning, exploratory data analysis, and visualization to extract meaningful business insights from the SuperStore sales dataset.

## WEEK 2

#  SuperStore Sales Data Analysis

##  Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a SuperStore sales dataset using Python.

The analysis focuses on understanding sales performance, customer segments, product categories, profitability, inventory levels, payment methods, delivery status, and delivery time.

The project is implemented using a **Google Colab / Jupyter Notebook** and uses Python data analysis and visualization libraries.

---

##  Objectives

The main objectives of this project are:

* Analyze SuperStore sales data
* Understand sales performance across different product categories
* Analyze profit and cost information
* Examine customer segments and regions
* Analyze inventory and reorder information
* Calculate delivery duration
* Identify missing values
* Generate statistical summaries
* Visualize sales performance using charts

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical data visualization
* **Google Colab** – Development environment

---

##  Dataset

The dataset contains **1,000 records** with **26 columns** before feature creation.

Important fields include:

| Column           | Description                     |
| ---------------- | ------------------------------- |
| Order ID         | Unique order identifier         |
| Order Date       | Date when the order was placed  |
| Ship Date        | Date when the order was shipped |
| Customer Name    | Customer name                   |
| Customer ID      | Unique customer identifier      |
| Customer Segment | Customer segment                |
| Category         | Product category                |
| Product Name     | Name of the product             |
| Product ID       | Unique product identifier       |
| Region           | Sales region                    |
| State            | Customer state                  |
| City             | Customer city                   |
| Quantity         | Quantity ordered                |
| Unit Price       | Price per unit                  |
| Discount (%)     | Discount applied                |
| Sales Amount     | Total sales amount              |
| Cost Price       | Product cost                    |
| Profit           | Profit generated                |
| Stock Left       | Remaining inventory             |
| Auto Reorder     | Reorder status                  |
| Reorder Quantity | Quantity to reorder             |
| Supplier Name    | Supplier information            |
| Supplier Email   | Supplier email                  |
| Payment Mode     | Payment method                  |
| Delivery Status  | Current delivery status         |
| Sales            | Sales value                     |

---

##  Data Analysis Process

### 1. Import Libraries

The project uses:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### 2. Load the Dataset

The dataset is loaded into a Pandas DataFrame.

```python
df = pd.read_csv("SuperStore.csv.csv")
```

### 3. Explore the Dataset

Initial exploration is performed using:

```python
df.head()
df.info()
df.describe()
```

The dataset contains:

* **1,000 rows**
* **26 original columns**
* Numerical and categorical features
* No missing values in the analyzed columns

### 4. Date Conversion

The `Order Date` and `Ship Date` columns are converted into datetime format.

```python
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
```

### 5. Delivery Time Analysis

A new feature called `Delivery Days` is created to calculate the number of days between ordering and shipping.

```python
df['Delivery Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days
```

### 6. Missing Value Analysis

Missing values are checked using:

```python
df.isnull().sum()
```

The analysis shows **0 missing values** across the dataset.

---

##  Sales Analysis

Sales are grouped by product category using:

```python
category_sales = (
    df.groupby('Category')['Sales Amount'].sum()
)
```

The analyzed categories are:

* Electronics
* Furniture
* Grocery
* Office Supplies

### Category Sales

| Category        | Sales Amount |
| --------------- | -----------: |
| Electronics     | 3,140,596.45 |
| Furniture       | 2,859,123.35 |
| Grocery         | 3,130,717.80 |
| Office Supplies | 3,196,907.70 |

A bar chart is also generated to visualize sales performance by category.

---

##  Visualizations

The notebook includes data visualization using Matplotlib and Seaborn.

Current analysis includes:

*  Sales by Category
*  Statistical analysis
*  Inventory-related analysis
*  Delivery-related analysis

---

##  Key Dataset Statistics

Some important numerical statistics from the dataset:

| Metric       |   Average |
| ------------ | --------: |
| Quantity     |     5.385 |
| Unit Price   |  2,589.46 |
| Discount     |    9.855% |
| Sales Amount | 12,327.35 |
| Cost Price   |  9,317.24 |
| Profit       |  3,010.10 |
| Stock Left   |     25.61 |

The maximum recorded sales amount is **47,481**, while the maximum recorded profit is **15,935.91**.

---

##  Project Structure

```text
SuperStore-Sales-Analysis/
│
├── SuperStore_Sales_Analysis.ipynb
├── SuperStore.csv
└── README.md
```

---

## How to Run the Project

### Option 1: Google Colab

1. Upload the `.ipynb` file to Google Colab.
2. Upload the `SuperStore.csv` dataset.
3. Update the dataset path if required.
4. Run the notebook cells sequentially.

### Option 2: Jupyter Notebook

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Then open the notebook:

```bash
jupyter notebook
```

Run the cells from top to bottom.

---

##  Insights

The analysis provides an overview of:

* Category-wise sales performance
* Profitability
* Product pricing
* Customer information
* Inventory levels
* Reordering information
* Payment methods
* Delivery status
* Delivery duration

The project demonstrates how Python can be used to transform raw sales data into useful business insights.

---

##  Future Improvements

The project can be extended by adding:

* Monthly and yearly sales trends
* Region-wise sales analysis
* Customer segment analysis
* Top-performing products
* Profit by category
* Delivery status visualization
* Payment mode analysis
* Inventory and reorder analysis
* Correlation analysis
* Interactive dashboards using **Power BI** or **Plotly**

---

## VISUALS

<img width="691" height="560" alt="image" src="https://github.com/user-attachments/assets/f3233a0a-fae5-494c-a633-ed80de183e88" />
<img width="695" height="470" alt="image" src="https://github.com/user-attachments/assets/603801be-cb4b-4373-8fb5-d1df2fd9c9d8" />
<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/9aee596d-b9e1-45ef-a287-9bedfa402ffd" />
<img width="589" height="455" alt="image" src="https://github.com/user-attachments/assets/0782427e-12f7-435d-a99f-73a0edd931fb" />
<img width="589" height="416" alt="image" src="https://github.com/user-attachments/assets/7812eab6-ade6-4904-af66-af2c0ed72cb8" />
<img width="589" height="455" alt="image" src="https://github.com/user-attachments/assets/0934e82f-0db7-48c9-9127-85c72aefc1c0" />
<img width="589" height="455" alt="image" src="https://github.com/user-attachments/assets/973f48f4-4963-41e3-bef0-e6444ec5ecea" />
<img width="632" height="540" alt="image" src="https://github.com/user-attachments/assets/9e19c124-e6d1-4e14-b88d-eb508c36fbcf" />



# Data Visualization

This project uses data visualization to convert the raw sales data into easy-to-understand graphs. Each graph focuses on a different aspect of the business, such as sales performance, profitability, and relationships between numerical variables.

---

## 1. Sales by Category

**Graph Type:** Bar Chart

This graph compares the **total sales amount generated by each product category**.

* It shows which product categories generate the most sales.
* It allows easy comparison between different categories.
* **Office Supplies** has the highest total sales.
* **Furniture** has the lowest total sales among the four categories.

### Purpose

This graph helps identify the **best-performing product categories in terms of sales**.

---

## 2. Profit by Category

**Graph Type:** Bar Plot

This graph compares the **profit generated by different product categories**.

* It shows how profitable each product category is.
* It helps compare **profitability rather than just sales**.
* A category having high sales does not necessarily mean it generates the highest profit.
* The graph helps identify categories that contribute more to the company's overall profit.

### Purpose

This graph helps understand **which product categories are more profitable for the business**.

---

## 3. Correlation Heatmap

**Graph Type:** Correlation Heatmap

The correlation heatmap shows the relationships between numerical variables such as:

* Quantity
* Unit Price
* Discount
* Sales Amount
* Cost Price
* Profit
* Stock Left
* Reorder Quantity
* Sales
* Delivery Days

The heatmap shows whether two variables have a **positive, negative, or weak relationship**.

Some important relationships found in the dataset are:

* **Sales Amount and Cost Price** have a very strong positive relationship.
* **Sales Amount and Profit** have a strong positive relationship.
* **Stock Left and Reorder Quantity** have a negative relationship.
* **Delivery Days and Sales** have almost no relationship.

### Purpose

This graph helps identify **patterns and relationships between different numerical variables** and can reveal which factors are closely associated with sales, profit, and inventory.

---

## Overall Explanation

| Visualization           | What it explains                                  |
| ----------------------- | ------------------------------------------------- |
| **Sales by Category**   | Which categories generate the most sales          |
| **Profit by Category**  | Which categories generate more profit             |
| **Correlation Heatmap** | How numerical variables are related to each other |

Together, these visualizations provide a clearer understanding of the dataset by showing **sales performance, profitability, and relationships between important business variables**.






## Author

NAVANEETHAN S

BCA Student
