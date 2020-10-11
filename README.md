# webscraper
 simple script that scrapes top 1 million websites

![Screenshot_3](/assets/Screenshot_3_1bddlytot.png)

Introduction
============

TODO

Usage
============

Docker
======

#### Build
```bash
docker build -t webscraper .
#Linux/mac
docker run -it --rm -v ./output:/app/output webscraper:latest
#powershell (Windows)
docker run -it --rm -v ${PWD}/output:/app/output webscraper:latest
```
Future Feature
========
- [Scrapy | A Fast and Powerful Scraping and Web Crawling Framework](https://scrapy.org/)

# sources
- [How to Download a List of All Registered Domain Names | Hacker News](https://news.ycombinator.com/item?id=10367342)
    - http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

Author
======

- wisehackermonkey <oranbusiness@gmail.com>

