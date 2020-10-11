# webscraper:  simple script that scrapes top 1 million websites
#
# This file is part of webscraper.
#
# MIT License
# Copyright (c) 2020 Oran C
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# @author = 'wisehackermonkey'
# @email = 'oranbusiness@gmail.com'


import requests
import csv
import time
import json 

END = 4
# Alexa top 1 million domain names (actually around 600k in reality)
DOMAIN_NAME_CSV_FILE = "./top-1m-internet-domains.csv"
SCRAPED_DOMAIN_NAME_FILE = f"scraping_results_x{END}_{time.time()}" + ".json"
# number of domains to be read


class webscraper:
    def __init__(self):
        self._websites_list = []
        self._scraping_results = []
        

    # reads and grabs the second column of the csv file
    # which hold list of internet domain names
    def read_csv(self, file_name):
        with open(file_name, "r") as website_csv:
            csvreader = csv.reader(website_csv, delimiter=",")
            for x, domain in enumerate(csvreader):
                # "12313, google.com" <- grab the domain name only = domain[1]
                self._websites_list.append(domain[1])

    # downloads the raw html from a givin domain name: "domain_name" = "example.com"
    def scrape_domain(self, domain_name):
        try:
            return requests.get(f"http://{domain_name}", timeout=3).text
        except requests.exceptions.TooManyRedirects as error:
            return "Error: TooManyRedirects"
        except requests.exceptions.ConnectionError as error:
            return "Error: ConnectionError"
        except requests.exceptions.ReadTimeout as error:
            return "Error: ReadTimeout"
    # scrapes all the domain names contained in self._websites_list
    # which comes from read_csv()
    def scrap_all(self):
        for x, web_domain_name in enumerate(self._websites_list):
            # number of domain names to scrap from .csv file
            if x < END:

                # record time it takes to grab page
                start_fetch_time = time.time()
                text_result = self.scrape_domain(web_domain_name)
                end_fetch_time = time.time()

                snipit = text_result[0:40].strip() if len(text_result) > 0 else ""
                print(f"Website:{web_domain_name}")
                print(f"Result:{snipit}.....")
                print(f"Total Time: {end_fetch_time - start_fetch_time} seconds")
                
                self._scraping_results.append({
                    "domain": web_domain_name,
                    "epoch":time.time(),
                    "loadtime": f"{end_fetch_time - start_fetch_time} seconds",
                    "result": text_result
                })
    def save_file(self,file_name):
        with open(file_name, "w", encoding="utf8") as scraped_domains_file:
            scraped_domains_file.write(json.dumps(self._scraping_results))
    @property
    def website_list(self):
        """
        Gets list of websites read from csv file
        """
        return self._websites_list

    @property
    def scraping_results(self):
        """
        Gets results of scraped  websites 
        """
        return self._scraping_results

if __name__ == "__main__":
    print("webscriaping started")

    Webscraper = webscraper()
    # read domain names from csv file
    Webscraper.read_csv(DOMAIN_NAME_CSV_FILE)
    
    # scrape all domain names contained in DOMAIN_NAME_CSV_FILE
    #v---- record how long the scraping operation takes
    start = time.time()
    Webscraper.scrap_all()
    end = time.time()
    
    Webscraper.save_file(SCRAPED_DOMAIN_NAME_FILE)

    print(f"Time Elapsed: {end - start} seconds")
