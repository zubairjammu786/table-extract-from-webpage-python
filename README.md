# table-extract-from-webpage-python
A python script that can export table  from a webpage and save it into csv file.

## Features
1. Extract tables from webpages
2. Make csv file for each table
3. Can extract multiple tables from one webpage
4. Seperate each table's csv file download
5. Can extract thousands rows of table in couple of seconds

# Table Extractor from Webpage using Python

This Python script extracts tables from a given webpage URL and exports them to CSV files. It utilizes the `requests` library to fetch the HTML content of the webpage and `BeautifulSoup` for parsing the HTML to extract tables.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/zubairjammu786/table-extract-from-webpage-python.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd table-extract-from-webpage-python
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the script:
    ```bash
    python extract_tables.py
    ```
    
Follow the prompt and enter the URL of the webpage containing tables.
5. The script will extract tables from the webpage and export them to separate CSV files in the same directory.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

Install the dependencies using pip:
```bash
pip install requests beautifulsoup4```

## Error Handling
- if your table is not importing it might not have <table></table> tag

## Example
Suppose you have a webpage with tables at the URL http://example.com/tables. You can use this script to extract and export those tables by running the script and providing the URL as input.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
