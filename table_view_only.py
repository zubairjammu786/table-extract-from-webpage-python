import requests
from bs4 import BeautifulSoup

def extract_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    return tables

def print_table(table):
    max_col_widths = [0] * len(table.find_all('tr')[0].find_all(['th', 'td']))
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        for i, data in enumerate(row_data):
            max_col_widths[i] = max(max_col_widths[i], len(data))
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=True).ljust(max_col_widths[i]) for i, cell in enumerate(row.find_all(['th', 'td']))]
        print("| " + " | ".join(row_data) + " |")
        if row == table.find_all('tr')[0]:
            print("|" + "|".join(["-" * (max_col_widths[i] + 2) for i in range(len(row_data))]) + "|")

def main():
    url = input("Enter the URL of the webpage: ")
    tables = extract_tables(url)
    if tables:
        for i, table in enumerate(tables):
            print(f"Table {i+1}:")
            print_table(table)
            print()
    else:
        print("No tables found on the webpage.")

if __name__ == "__main__":
    main()
