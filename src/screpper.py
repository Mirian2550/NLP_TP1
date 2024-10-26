import requests
from bs4 import BeautifulSoup
import csv
import ssl
import concurrent.futures
import time

ssl._create_default_https_context = ssl._create_unverified_context

class ScrapperBooks:
    def __init__(self, url):
        self.url = url

    def get_books(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        div = soup.find_all('div', class_='page_content')[0]
        ol = div.find('ol')
        return ['https://www.gutenberg.org' + li.find('a')['href'] for li in ol.find_all('li')]

    def get_book_details(self, book_url):
        print(book_url)
        response = requests.get(book_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='bibrec')
        details = {
            tr.th.get_text(strip=True): tr.td.get_text(strip=True)
            for tr in table.find_all('tr')
            if tr.th and tr.td and tr.th.get_text(strip=True) in {'Author', 'Title', 'Summary'}
        }
        details['Link'] = book_url
        return details

    def save_to_csv(self, data, filename='books.csv'):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Summary', 'Link'])
            writer.writeheader()
            writer.writerows(data)

    def run(self):
        start_time = time.time()
        books = self.get_books()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            books_details = list(executor.map(self.get_book_details, books))
        self.save_to_csv(books_details)
        print(f"{len(books_details)} libros guardados en 'books.csv'.")
        elapsed_time = time.time() - start_time
        print(f"Tiempo total: {elapsed_time:.2f} segundos")

scraper = ScrapperBooks("https://www.gutenberg.org/browse/scores/top1000.php#books-last1")
scraper.run()
