import requests
from bs4 import BeautifulSoup
import csv

# mengirimkan request ke halaman web
url = 'https://bisa.ai/course/all_course/1'
response = requests.get(url)

# melakukan parsing html menggunakan BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# mencari semua elemen dengan tag div dan class row mb-4
titles = soup.find_all('div', class_='row mb-4')

# membuka file CSV dan menuliskan header
with open('titles.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])

    # mencetak judul free course yang ditemukan ke dalam file CSV
    for title in titles:
        if title.find('h3', class_='nsans-700 text-hitam-custom text-shadow-2 text-center pb-3'):
            writer.writerow([title.text.strip()])
