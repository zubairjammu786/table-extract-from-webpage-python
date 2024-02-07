import requests
from bs4 import BeautifulSoup
import csv
import random

def extract_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    return tables

randdigit = random.randint(100,999)

def export_tables(tables):
    for i, table in enumerate(tables):
        filename = f"table_{i+1}{randdigit}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in table.find_all('tr'):
                writer.writerow([cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])])
        print(f"Table {i+1} exported to {filename}")

def main():
    url = input("Enter the URL of the webpage: ")
    tables = extract_tables(url)
    if tables:
        export_tables(tables)
    else:
        print("No tables found on the webpage.")

if __name__ == "__main__":
    main()
