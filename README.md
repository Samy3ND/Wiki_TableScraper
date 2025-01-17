# Wikipedia Table Scraper

This project is a Streamlit-based web application designed to scrape tables from any Wikipedia page and display the data in an interactive format. With this tool, users can quickly extract and view tabular data from Wikipedia.

## Features
- Scrapes all tables from a specified Wikipedia URL.
- Displays the scraped tables in a clean, interactive format.
- Automatically handles tables with missing or inconsistent headers.
- Provides feedback on the number of tables found on the page.

## Prerequisites
Ensure you have the following installed on your system:

- Python 3.7 or later
- pip (Python package manager)

## Installation
1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application using the following command:
   ```bash
   streamlit run app.py
   ```

2. Open the provided local URL in your web browser (usually `http://localhost:8501`).

3. Enter a valid Wikipedia URL (must start with `https://en.wikipedia.org`) in the input field.

4. Click the `SCRAPE` button to extract and display tables.

## How It Works
1. The app takes a Wikipedia URL input from the user.
2. It validates the URL to ensure it begins with `https://en.wikipedia.org`.
3. Makes a request to fetch the HTML content of the page using the `requests` library.
4. Parses the HTML using `BeautifulSoup` to find tables with the `wikitable` class.
5. Extracts data from each table and converts it into a Pandas DataFrame for display.
6. Displays the data table-by-table with headers and contents.

## Error Handling
- Provides warnings if the entered URL is invalid or does not lead to a Wikipedia page.
- Displays an error if no tables are found on the page.
- Catches network errors or issues with table processing and provides relevant feedback.

## Example
Enter a URL like:
```
https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)
```
Click `SCRAPE` to see the tabular data extracted from the page.

## Dependencies
- [Streamlit](https://streamlit.io/) - For building the interactive web application.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - For parsing HTML and extracting data.
- [Pandas](https://pandas.pydata.org/) - For handling and displaying tabular data.
- [Requests](https://docs.python-requests.org/) - For making HTTP requests.

## Limitations
- Only works with tables that have the `wikitable` class on Wikipedia pages.
- Assumes all rows in a table have consistent cell counts.

---

Enjoy scraping and exploring Wikipedia tables effortlessly!
