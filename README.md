# Web Scrapping/Crawler

Scrapping web content using python scrapy. In this project I scrapped amazon bestseller items by categories.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.6.0 or higher, I have not tested in previous version of python
Dependency lib's are added into requirement.txt, run dependency.txt to install required python packages.



### Installing and running

A step by step series of examples that tell you how to get a development env running

Install dependency packages 

```
1. python: pip install scrapy 
   install this package with conda run one of the following:
    conda install -c conda-forge scrapy
2. Create python project uisng scrapy
    scrapy startproject web_scrapping
3. Create spiders
    scrapy genspider amazon_bestseller https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics

```
### Running

```
run python script web_scrapping/controllers/controller.py
csv will be generated under output folder of your current directory
```

## Author

* **Deepa Aswathaiah**

