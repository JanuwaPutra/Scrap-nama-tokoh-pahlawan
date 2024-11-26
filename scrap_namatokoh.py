import requests
from bs4 import BeautifulSoup
import csv

nama_tokoh = input("Masukkan nama tokoh pahlawan Indonesia: ")
url = "https://id.wikipedia.org/wiki/" + nama_tokoh.replace(" ", "_")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print (soup)
paragraphs = soup.find_all('p')
#print (paragraphs)
informasi = "nama tidak ada."


for paragraph in paragraphs:
    text = paragraph.get_text() 
    if nama_tokoh.lower() in text.lower(): 
        informasi = text.strip()
        break 

if informasi != "nama tidak ada.":
    with open('tokoh_pahlawan.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writerow(['Nama Tokoh', 'Penjelasan Singkat'])
        writer.writerow([nama_tokoh, informasi])  
        print(f"DATA MASUK CSV.")
else:
    print(informasi)
