# Explore US Bikeshare Data
## Project Overview
This project uses Python to analyze data from bikeshare systems in three major U.S. cities: Chicago, New York City, and Washington. The goal is to provide insights into the usage patterns of these systems, using descriptive statistics and user interaction through a terminal-based interface.

## Purpose
The purpose of this project is to:
- Import bikeshare data for analysis.
- Compute descriptive statistics such as popular travel times, trip durations, and user demographics.
- Create an interactive terminal experience where users can filter data by city, month, and day of the week to gain insights about bikeshare usage.
## Requirements
To run and complete this project, you will need the following software:
- Python 3: Used for scripting and data manipulation.
- Pandas: A Python library for data analysis and manipulation.
You can install the required libraries using pip:
`pip install pandas`
## Files Used
The following files are used in this project:
- bikeshare_2.py: The Python script used to perform the analysis and handle user input.
- chicago.csv: Data source for the bikeshare system in Chicago.
- new_york_city.csv: Data source for the bikeshare system in New York City.
- washington.csv: Data source for the bikeshare system in Washington, D.C.
## How it works
- The program prompts the user to select a city (Chicago, New York City, or Washington).
- The user can then filter the data by month (January to June or all months) and by day of the week (or all days).
- The program computes and displays statistics for the selected filters, including the most popular travel times, trip durations, and user types.
## User Inputs
The program accepts the following inputs from the user:
- City: Choose between "chicago", "new york city", or "washington".
- Month: Choose between "january", "february", "march", "april", "may", "june", or "all".
- Day: Choose between "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", or "all".
## Project Setup
To run the project, follow these steps:
- clone the repository using `$ git clone https://github.com/E4GLz/pdsnd_github.git`
- navigate to the project directory where you cloned the repository
- run the bikeshare_2.py script
## Results
The program outputs various insights, such as:
- Most common month for bikeshare usage
- Most common day of the week for trips
- Most common start and end stations
- Total and average trip durations
- Breakdown of user types (e.g., subscribers vs. customers)
## Known Issues and Limitations
While this project provides valuable insights into bikeshare usage, there are a few known issues and limitations:
- Missing Data: The data for washington is missing gender and birth year column.
- Limited Time Frame: The analysis only covers the first six months. A full-year dataset would provide a brgoader view.
- Interface Limitation: The command-line interface may be difficult for non-technical users.
- Static Data: The project uses fixed datasets, not reflecting real-time bikeshare database.
## Credits
Special thanks to the following resources for aiding the completion of this project:
- [Python Official Documentation:](https://docs.python.org/3/contents.html) A valuable resource for Python programming.
- [Pandas User Guide:](https://pandas.pydata.org/docs/user_guide/index.html#user-guide) Essential for working with data frames.
- [W3Schools Python Tutorial:](https://www.w3schools.com)  Useful for quick reference and troubleshooting.
- [Udacity](https://www.udacity.com) for providing the data and project outline.