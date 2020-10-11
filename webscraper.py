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

# Alexa top 1 million domain names (actually around 600k in reality)
DOMAIN_NAME_CSV_FILE = "top-1m-internet-domains.csv"
# number of domains to be read
END = 100

class webscraper:
    def __init__(self):
        self._url = 1

    def scrape_domain(self, domain_name):
        try:
            return requests.get(f"http://{domain_name}", timeout=3).text

        except requests.exceptions.TooManyRedirects as error:
            return "Error: TooManyRedirects"
        except requests.exceptions.ConnectionError as error:
            return "Error: ConnectionError"
        except requests.exceptions.ReadTimeout as error:
            return "Error: ReadTimeout"

    @property
    def url(self):
        """
        I am a getter.


        """

        return self._url

if __name__ == "__main__":
    print("webscriaping started")


    Webscraper = webscraper()
    # read domain names from csv file
    with open("./top-1m-internet-domains.csv","r") as website_csv:
        csvreader = csv.reader(website_csv, delimiter=",")
        with open(f"scraping_results_x{END}_{time.time()}.txt","w", encoding="utf8") as scraped_domains_file:
            start = time.time()
            for x, domain in enumerate(csvreader):
                if x < END:
                    web_domain_name = domain[1]
                    start_fetch_time = time.time()
                    text_result = Webscraper.scrape_domain(web_domain_name) 
                    end_fetch_time = time.time()

                    snipit = len(text_result) > 0 if text_result[0:40].strip() else ""
                    print(f"Website:{web_domain_name}")
                    print(f"Result:{snipit}.....")
                    print(f"Total Time: {end_fetch_time - start_fetch_time} seconds")

                    scraped_domains_file.write(f"\n{web_domain_name}, epoch:{time.time()}, loadtime: {end_fetch_time - start_fetch_time} seconds\n{text_result}\n``````````````\n")
            end = time.time()

            print(f"Time Elapsed: {end - start} seconds")