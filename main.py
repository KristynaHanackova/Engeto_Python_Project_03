"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Kristýna Hanáčková
email: hanackova.kr@gmail.com
"""

import requests

from bs4 import BeautifulSoup

import csv

from urllib.parse import urljoin

import sys

if len(sys.argv) != 3:
    print("Error: Enter 2 arguments: <link_to_municipality> <output_file_name.csv>")
    sys.exit(1)

base_url = sys.argv[1]
output_file = sys.argv[2]

if not base_url.startswith("https://www.volby.cz/pls/ps2017nss/ps32"):
    print("Error: First argument must be link to municipality from volby.cz")
    sys.exit(1)

def start_web_scraping(base_url, output_file):

    def get_soup(url) -> BeautifulSoup:
        '''
        Convert HTML document into structured format (soup)
        '''
        web_page = requests.get(url)
        web_page.raise_for_status() 
        soup = BeautifulSoup(web_page.text, features='html.parser')
        return soup

    soup = get_soup(base_url)

    codes = [td.text.strip() for td in soup.find_all('td', {'class': 'cislo'})]

    headers_list = ["t1sa1 t1sb1", "t2sa1 t2sb1", "t3sa1 t3sb1"]
    all_links = [
        urljoin(base_url, td.a['href'])
        for header in headers_list
        for td in soup.find_all('td', headers=header)
        if td.a
    ]
           
    party_names = []
    
    for link in all_links:
        municipality_soup = get_soup(link)
        for tr in municipality_soup.find_all('tr'):
            party = tr.find('td', headers='t1sa1 t1sb2') or tr.find('td', headers='t2sa1 t2sb2')
            if party:
                name = party.text.strip()
                if name not in party_names:
                    party_names.append(name)
                
    results = []

    for code, link in zip(codes, all_links):
        municipality_soup = get_soup(link)
        municipality_name = municipality_soup.find_all('h3')[2].text.strip().replace('Obec: ', '')
    
        votes_info = municipality_soup.find_all('td', class_='cislo') 
        voters = votes_info[3].text.strip()
        envelopes = votes_info[4].text.strip()
        valid_votes = votes_info[7].text.strip()
    
        row = {
            'Code' : code,
            'Location': municipality_name,
            'Registered': voters,
            'Envelopes': envelopes,
            'Valid': valid_votes
        }
        
        party_votes = {name: '0' for name in party_names}
        
        for tr in municipality_soup.find_all('tr'):
            party = tr.find('td', headers="t1sa1 t1sb2")
            votes = tr.find('td', headers="t1sa2 t1sb3")
            if party and votes:
                party_votes[party.text.strip()] = votes.text.strip()
        
        for tr in municipality_soup.find_all('tr'):
            party = tr.find('td', headers="t2sa1 t2sb2")
            votes = tr.find('td', headers="t2sa2 t2sb3")
            if party and votes:
                party_votes[party.text.strip()] = votes.text.strip()
            
        row.update(party_votes)
        results.append(row)        

    fieldnames = ['Code', 'Location', 'Registered', 'Envelopes', 'Valid'] + party_names

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
if __name__ == "__main__":
    start_web_scraping(base_url, output_file)