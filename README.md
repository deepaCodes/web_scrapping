# Web Scrapping/Crawler

Scrapping web content using python scrapy. In this project I scrapped amazon bestseller items by categories.

I have another project which scrapes data from SEC EDGAR and downloads filing forms. Checkout at https://github.com/deepaCodes/sec_edgar

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
run python script ./web_scrapping/web_scrapping/controllers/amazon_scrapper.py

csv will be generated under ./web_scrapping/output folder of your current directory. See below for the program console output
```

## Author

* **Deepa Aswathaiah**



## Program out

```
csv out file generated under ./web_scrapping/output/

INFO: Overridden settings: {'BOT_NAME': 'web_scrapping', 'FEED_FORMAT': 'csv', 'FEED_URI': 'output/%(name)s_%(time)s.csv', 'NEWSPIDER_MODULE': 'web_scrapping.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['web_scrapping.spiders']}
2020-02-06 06:53:20 [scrapy.extensions.telnet] INFO: Telnet Password: cc6e42400eda91ab
2020-02-06 06:53:20 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-02-06 06:53:20 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-02-06 06:53:20 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-02-06 06:53:20 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-02-06 06:53:20 [scrapy.core.engine] INFO: Spider opened
2020-02-06 06:53:20 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-02-06 06:53:20 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-02-06 06:53:21 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.com/robots.txt> (referer: None)
2020-02-06 06:53:21 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/> (referer: None)
2020-02-06 06:53:21 [amazon_bestseller] INFO: amazon_bestseller spider parsing  on https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#1', 'item_name': '\n            Fire TV Stick streaming media player with Alexa built in, includes Alexa Voice Remote, HD, easy set-up, released 2019\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '126,741', 'price': '$39.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#2', 'item_name': '\n            Fire TV Stick 4K streaming device with Alexa built in, Ultra HD, Dolby Vision, includes the Alexa Voice Remote\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '147,710', 'price': '$49.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#3', 'item_name': '\n            Echo Dot (3rd Gen) - Smart speaker with Alexa - Charcoal\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '296,917', 'price': '$29.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#4', 'item_name': '\n            Roku Express HD Streaming Media Player 2019\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '6,263', 'price': '$29.00'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#5', 'item_name': '\n            Echo Auto - Add Alexa to your car\n        ', 'star_rating': '3.6 out of 5 stars', 'review_count': '33,199', 'price': '$29.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#6', 'item_name': '\n            Echo Dot (3rd Gen) - Smart speaker with Alexa - Sandstone\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '296,917', 'price': '$29.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#7', 'item_name': '\n            Echo Dot (3rd Gen) - Smart speaker with Alexa - Plum\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '296,917', 'price': '$29.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#8', 'item_name': '\n            Roku Streaming Stick+ | HD/4K/HDR Streaming Device with Long-range Wireless and Voice Remote with TV Controls (updated for 2019)\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '10,385', 'price': '$46.59'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#9', 'item_name': '\n            Echo Show 5 – Compact smart display with Alexa - Charcoal\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '74,384', 'price': '$64.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#10', 'item_name': '\n            Fujifilm Instax Mini Instant Film, 10 Sheets×5 Pack(Total 50 Shoots)\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '1,623', 'price': '$32.14'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#11', 'item_name': '\n            Echo Dot (3rd Gen) - Smart speaker with Alexa - Heather Gray\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '296,917', 'price': '$29.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#12', 'item_name': '\n            Kindle Paperwhite – Now Waterproof with 2x the Storage – Includes Special Offers\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '27,961', 'price': '$94.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#13', 'item_name': '\n            Wyze Cam 1080p HD Indoor Wireless Smart Home Camera with Night Vision, 2-Way Audio, Works with Alexa & the Google Assistant, One Pack, White - WYZEC2\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '23,215', 'price': '$25.98'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#14', 'item_name': '\n            Introducing Echo Show 8 - HD 8" smart display with Alexa - Charcoal\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '17,177', 'price': '$89.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#15', 'item_name': '\n            Amazon Smart Plug, works with Alexa – A Certified for Humans Device\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '60,234', 'price': '$24.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#16', 'item_name': '\n            Ring Rechargeable Battery Pack\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '5,411', 'price': '$29.00'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#17', 'item_name': '\n            Wyze Cam Pan 1080p Pan/Tilt/Zoom Wi-Fi Indoor Smart Home Camera with Night Vision, 2-Way Audio, Works with Alexa & the Google Assistant, White - WYZECP1\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '11,781', 'price': '$37.98'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#18', 'item_name': '\n            Fujifilm INSTAX Mini Instant Film 2 Pack = 20 Sheets (White) for Fujifilm Mini 8 & Mini 9 Cameras\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '2,132', 'price': '$14.51'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#19', 'item_name': '\n            All-new Kindle - Now with a Built-in Front Light - Black - Includes Special Offers\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '8,072', 'price': '$64.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#20', 'item_name': '\n            8" Selfie Ring Light with Tripod Stand & Cell Phone Holder for Live Stream/Makeup, UBeesize Mini Led Camera Ringlight for YouTube Video/Photography Compatible with iPhone Xs Max XR Android (Upgraded)\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '4,788', 'price': '$29.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#21', 'item_name': '\n            amFilm Tempered Glass Screen Protector for Nintendo Switch 2017 (2-Pack)\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '21,631', 'price': '$7.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#22', 'item_name': '\n            NETGEAR Nighthawk Smart WiFi Router (R6700) - AC1750 Wireless Speed (up to 1750 Mbps) | Up to 1500 sq ft Coverage & 25 Devices | 4 x 1G Ethernet and 1 x 3.0 USB ports | Armor Security\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '37,940', 'price': '$72.63'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#23', 'item_name': '\n            TP-Link AC1750 Smart WiFi Router - Dual Band Gigabit Wireless Internet Router for Home, Works with Alexa, VPN Server, Parental Control&QoS (Archer A7)\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '6,015', 'price': '$51.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#24', 'item_name': '\n            DUDE Wipes Flushable Wet Wipes Dispenser (3 Packs 48 Wipes), Unscented Wet Wipes with Vitamin-E & Aloe for at-Home Use, Septic and Sewer Safe\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '3,087', 'price': '$8.94'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#25', 'item_name': '\n            Wyze Cam 1080p HD Indoor Wireless Smart Home Camera with Night Vision, 2-Way Audio, Works with Alexa & the Google Assistant (Pack of 2), White - WYZEC2X2\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '4,878', 'price': '$47.41'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#26', 'item_name': '\n            Power Strip with USB, Anker 3-Outlet & 3 PowerIQ USB Power Strip Surge Protector, PowerPort Strip 3 with 5 Foot Long Extension Cord, Flat Plug, Safety Shutter, for Home, Office (300 J)\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '400', 'price': '$22.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#27', 'item_name': '\n            Roku Ultra | Streaming Media Player 4K/HD/HDR with Premium JBL Headphones 2019\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '3,004', 'price': '$74.75'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#28', 'item_name': '\n            Fire 7 Tablet (7" display, 16 GB) - Black\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '42,426', 'price': '$49.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#29', 'item_name': '\n            All-new Echo Dot (3rd Gen) - Smart speaker with clock and Alexa - Sandstone\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '296,917', 'price': '$39.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#30', 'item_name': '\n            Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin Zero Frame Monitor (HDMI & VGA port)\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '3,732', 'price': '$89.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#31', 'item_name': '\n            AmazonBasics Small Digital Alarm Clock with Nightlight and Battery Backup, LED Display\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '895', 'price': '$9.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#32', 'item_name': '\n            All-new Echo (3rd Gen)- Smart speaker with Alexa- Charcoal\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '17,796', 'price': '$74.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#33', 'item_name': '\n            Introducing Ring Indoor Cam, Compact Plug-In HD security camera with two-way talk, White, Works with Alexa\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '3,375', 'price': '$59.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#34', 'item_name': '\n            RUNMUS Stereo Gaming Headset for PS4, Xbox One, Nintendo Switch, PC, PS3, Mac, Laptop, Over Ear Headphones PS4 Headset Xbox One Headset with Surround Sound, LED Light & Noise Canceling Microphone\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '10,352', 'price': '$26.85'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#35', 'item_name': '\n            Nintendo Switch with Neon Blue and Neon Red Joy‑Con - HAC-001(-01)\n        ', 'star_rating': '4.8 out of 5 stars', 'review_count': '6,160', 'price': '$299.00'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#36', 'item_name': '\n            HP 23.8-inch FHD IPS Monitor with Tilt/Height Adjustment (VH240a, Black)\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '3,013', 'price': '$104.62'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#37', 'item_name': '\n            Cool Sticker 100pcs Random Music Film Vinyl Skateboard Guitar Travel Case Sticker Door Laptop Luggage Car Bike Bicycle Stickers (100pcs)\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '2,712', 'price': '$6.69'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#38', 'item_name': '\n            Acer Aspire 5 Slim Laptop, 15.6 inches Full HD IPS Display, AMD Ryzen 3 3200U, Vega 3 Graphics, 4GB DDR4, 128GB SSD, Backlit Keyboard, Windows 10 in S Mode, A515-43-R19L\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '2,996', 'price': '$313.68'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#39', 'item_name': '\n            All-new Fire TV Cube, hands-free with Alexa built in, 4K Ultra HD, streaming media player, released 2019\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '5,454', 'price': '$119.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#40', 'item_name': '\n            Roku Premiere | HD/4K/HDR Streaming Media Player, Simple Remote and Premium HDMI Cable\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '8,218', 'price': '$38.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#41', 'item_name': '\n            Scotch-Brite Non-Scratch Scrub Sponges, Cleans Fast without Scratching, Stands Up to Stuck-on Grime, 9 Scrub Sponges\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '4,621', 'price': '$7.82'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#42', 'item_name': '\n            Polaroid 2x3ʺ Premium ZINK Zero Photo Paper 50-Pack - Compatible with Polaroid Snap / SnapTouch Instant Print Digital Cameras & Polaroid ZIP Mobile Photo Printer\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '3,808', 'price': '$13.46'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#43', 'item_name': '\n            3M Particulate Respirator 8210, N95, Smoke, Dust, Grinding, Sanding, Sawing, Sweeping, 20/Pack\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '115', 'price': None}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#44', 'item_name': '\n            Introducing Echo Flex - Plug-in mini smart speaker with Alexa\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '4,455', 'price': '$19.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#45', 'item_name': '\n            Cord Cover Raceway Kit, 157" Cable Cover Channel, Paintable Cord Concealer System Cable Hider, Cord Wires, Hiding Wall Mount TV Powers Cords in Home Office, 10X L15.7in X W0.95in X 0.55in\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '823', 'price': '$15.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#46', 'item_name': '\n            GE 6 Outlet Surge Protector, 10 Ft Extension Cord, Power Strip, 800 Joules, Flat Plug, Twist-to-Close Safety Covers, White, 14092\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '3,009', 'price': '$12.02'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#47', 'item_name': '\n            Introducing Echo Show 8 - HD 8" smart display with Alexa - Sandstone\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '17,177', 'price': '$89.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#48', 'item_name': '\n            Fire HD 8 Tablet (8" HD Display, 16 GB) - Black\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '45,583', 'price': '$79.99'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#49', 'item_name': '\n            3M Organic Vapor/Acid Gas Cartridge/Filter 60923, P100 Respiratory Protection (Pack of 2)\n        ', 'star_rating': '4.8 out of 5 stars', 'review_count': '371', 'price': '$21.62'}
2020-02-06 06:53:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/>
{'ranking': '#50', 'item_name': '\n            Ring Video Doorbell 2 with HD Video, Motion Activated Alerts, Easy Installation\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '22,262', 'price': '$199.00'}
2020-02-06 06:53:21 [amazon_bestseller] INFO: following to next page: https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2
2020-02-06 06:53:21 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2> (referer: https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/)
2020-02-06 06:53:22 [amazon_bestseller] INFO: amazon_bestseller spider parsing  on https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#51', 'item_name': '\n            Echo Show 5 – Compact smart display with Alexa - Sandstone\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '74,384', 'price': '$64.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#52', 'item_name': '\n            Orzly Carry Case Compatible With Nintendo Switch - BLACK Protective Hard Portable Travel Carry Case Shell Pouch for Nintendo Switch Console & Accessories\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '5,724', 'price': '$13.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#53', 'item_name': '\n            USB Wall Charger, Surge Protector, POWRUI 6-Outlet Extender with 2 USB Charging Ports (2.4A Total) and Night Light, 3-Sided Power Strip with Adapter Spaced Outlets - White，ETL Listed\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '2,756', 'price': '$19.97'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#54', 'item_name': '\n            All-New Fire HD 10 Tablet (10.1" 1080p full HD display, 32 GB) – Black\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '21,729', 'price': '$149.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#55', 'item_name': '\n            Fire 7 Tablet (7" display, 16 GB) - Twilight Blue\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '42,426', 'price': '$49.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#56', 'item_name': '\n            AmazonBasics 9 Volt Everyday Alkaline Batteries - Pack of 4 (Appearance may vary)\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '11,296', 'price': '$7.48'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#57', 'item_name': '\n            Bond Touch - Bracelets That Bring Long-Distance Lovers Closer Than Ever\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '263', 'price': '$98.00'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#58', 'item_name': '\n            AKASO EK7000 4K WiFi Sports Action Camera Ultra HD Waterproof DV Camcorder 12MP 170 Degree Wide Angle\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '12,649', 'price': '$43.25'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#59', 'item_name': '\n            Ring Chime Pro, Indoor Chime and Wi-Fi Extender ONLY for Ring Network Devices\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '4,441', 'price': '$49.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#60', 'item_name': '\n            TCL 32S327 32-Inch 1080p Roku Smart LED TV (2018 Model)\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '7,583', 'price': '$149.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#61', 'item_name': '\n            Kindle Paperwhite – Now Waterproof with more than 2x the Storage – Includes Special Offers\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '27,961', 'price': '$119.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#62', 'item_name': '\n            Fujifilm INSTAX Mini Instant Film Twin Pack (White)\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '11,341', 'price': '$11.95'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#63', 'item_name': '\n            Blink XT2 Outdoor/Indoor Smart Security Camera with cloud storage included, 2-way audio, 2-year battery life – Add-on camera for existing Blink customers\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '14,943', 'price': '$89.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#64', 'item_name': '\n            Blink XT2 Outdoor/Indoor Smart Security Camera with cloud storage included, 2-way audio, 2-year battery life – 2 camera kit\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '14,943', 'price': '$179.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#65', 'item_name': '\n            TOSHIBA 50LF711U20 50-inch 4K Ultra HD Smart LED TV HDR - Fire TV Edition\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '15,640', 'price': '$269.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#66', 'item_name': '\n            Xbox One S 1TB All-Digital Edition Console (Disc-Free Gaming)\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '2,190', 'price': '$171.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#67', 'item_name': '\n            Power Strip, Bototek Surge Protector with 10 AC Outlets and 4 USB Charging Ports,1625W/13A, 2100 Joules, 6 Feet Long Extension Cord for Smartphone Tablets Home,Office, Hotel- Black\n        ', 'star_rating': '4.9 out of 5 stars', 'review_count': '2,535', 'price': '$25.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#68', 'item_name': '\n            Fire 7 Tablet (7" display, 16 GB) - Plum\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '42,426', 'price': '$49.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#69', 'item_name': '\n            TP-Link AC1200 Gigabit Smart WiFi Router - 5GHz Gigabit Dual Band MU-MIMO Wireless Internet Router, Long Range Coverage by 4 Antennas(Archer A6)\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '1,658', 'price': '$44.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#70', 'item_name': '\n            Certified Refurbished Fire TV Stick with Alexa Voice Remote, streaming media player\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '2,973', 'price': '$34.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#71', 'item_name': '\n            AmazonBasics 6-Outlet Surge Protector Power Strip 2-Pack, 2-Foot Long Cord, 200 Joule - White\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '8,036', 'price': '$11.49'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#72', 'item_name': '\n            Blink XT2 Outdoor/Indoor Smart Security Camera with cloud storage included, 2-way audio, 2-year battery life – 3 camera kit\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '14,943', 'price': '$249.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#73', 'item_name': '\n            NETGEAR Cable Modem CM500 - Compatible with all Cable Providers including Xfinity by Comcast, Spectrum, Cox | For Cable Plans Up to 300 Mbps | DOCSIS 3.0\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '9,350', 'price': '$59.17'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#74', 'item_name': '\n            Tile Slim (2020) - 1 Pack\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '2,377', 'price': '$29.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#75', 'item_name': '\n            Cable Clips - Cord Organizer - Cable Management - Wire Holder System - 6 Pack Adhesive Cord Hooks - Home, Office, Cubicle, Car, Nightstand, Desk Accessories - Gift Ideas Men, Women, Dad, Mom, Him, Her\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '3,933', 'price': '$6.97'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#76', 'item_name': '\n            Acer R240HY bidx 23.8-Inch IPS HDMI DVI VGA (1920 x 1080) Widescreen Monitor\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '3,385', 'price': '$99.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#77', 'item_name': '\n            Fire 7 Kids Edition Tablet, 7" Display, 16 GB, Blue Kid-Proof Case\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '32,134', 'price': '$99.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#78', 'item_name': '\n            All-new Echo (3rd Gen) - Smart speaker with Alexa - Twilight Blue\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '17,796', 'price': '$74.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#79', 'item_name': '\n            TCL 55S425 55 inch 4K Smart LED Roku TV (2019)\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '5,691', 'price': '$299.19'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#80', 'item_name': '\n            [3 Pack] Screen Protector Tempered Glass for Nintendo Switch, iVoler Transparent HD Clear Anti-Scratch Screen Protector Compatible Nintendo Switch\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '2,954', 'price': '$7.95'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#81', 'item_name': '\n            Dude Wipes Flushable Wet Wipes Dispenser, Mint Chill, 48 Count (Pack of 3) Scented Wet Wipes with Vitamin-E, Aloe, Eucalyptus & Tea Tree Oils for at-Home Use, Septic and Sewer Safe\n        ', 'star_rating': '4.6 out of 5 stars', 'review_count': '3,785', 'price': '$13.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#82', 'item_name': '\n            Toshiba 32LF221U19 32-inch 720p HD Smart LED TV - Fire TV Edition\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '15,640', 'price': '$129.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#83', 'item_name': '\n            Digital Alarm Clock, with Wooden Electronic LED Time Display, 3 Alarm Settings, Humidity & Temperature Detect, Wood Made Electric Clocks for Bedroom, Bedside, Black\n        ', 'star_rating': '4.8 out of 5 stars', 'review_count': '4,967', 'price': '$19.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#84', 'item_name': '\n            Kindle Paperwhite – Now Waterproof with 2x the Storage – Includes Special Offers + Kindle Unlimited (with auto-renewal)\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '27,961', 'price': '$94.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#85', 'item_name': '\n            Neewer 50-In-1 Action Camera Accessory Kit Compatible with GoPro Hero 8 Max 7 6 5 4 Black GoPro 2018 Session Fusion Silver White Insta360 DJI AKASO APEMAN Campark SJCAM Action Camera etc\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '4,387', 'price': '$21.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#86', 'item_name': '\n            Kindle Paperwhite – Now Waterproof with 2x the Storage\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '27,961', 'price': '$114.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#87', 'item_name': '\n            Microsoft Surface Dock (Pd9-00003)\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '1,684', 'price': '$128.98'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#88', 'item_name': '\n            Sceptre E248W-19203R 24" Ultra Thin 75Hz 1080p LED Monitor 2x HDMI VGA Build-in Speakers, Metallic Black 2018\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '2,773', 'price': '$89.97'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#89', 'item_name': '\n            Anker Power Strip with USB, 2 Outlet & 2 PowerIQ USB Ports (24W) Travel Power Strip, Powerport Strip 2 Mini with 5ft Long Cord, Safety Door, Flat Plug, for Hotels, Dorm Room, Cruise Ships, and Home\n        ', 'star_rating': '4.7 out of 5 stars', 'review_count': '534', 'price': '$15.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#90', 'item_name': '\n            BENGOO V-4 Gaming Headset for Xbox One, PS4, PC, Controller, Noise Cancelling Over Ear Headphones with Mic, LED Light Bass Surround Soft Memory Earmuffs for PS2 Mac Nintendo Switch Games\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '2,821', 'price': '$20.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#91', 'item_name': '\n            Sabrent 4-Port USB 2.0 Hub with Individual LED lit Power Switches (HB-UMLS)\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '17,476', 'price': '$7.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#92', 'item_name': '\n            RCA Digital Alarm Clock with Large 1.4" Display\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '6,455', 'price': '$8.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#93', 'item_name': '\n            Sony DVPSR210P DVD Player\n        ', 'star_rating': '4.2 out of 5 stars', 'review_count': '4,267', 'price': '$33.00'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#94', 'item_name': '\n            RAVPower FileHub, Travel Router AC750, Wireless SD Card Reader, Connect Portable SSD Hard Drive to iPhone iPad Tablet Smart Phone Laptop for Photo Backup, Data Transfer, Portable NAS, 6700mAh Battery\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '893', 'price': '$55.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#95', 'item_name': '\n            Echo Show (2nd Gen) – Premium sound and a vibrant 10.1” HD screen - Charcoal\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '14,519', 'price': '$179.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#96', 'item_name': '\n            Fire 7 Tablet (7" display, 16 GB) - Sage\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '42,426', 'price': '$49.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#97', 'item_name': '\n            Stickers for Water Bottles Big 30-Pack Cute,Waterproof,Aesthetic,Trendy Stickers for Teens,Girls Perfect for Waterbottle,Laptop,Phone,Travel\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '1,926', 'price': '$1.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#98', 'item_name': '\n            EVISTR 16GB Digital Voice Recorder Voice Activated Recorder with Playback - Upgraded Small Tape Recorder for Lectures, Meetings, Interviews, Mini Audio Recorder USB Charge, MP3\n        ', 'star_rating': '4.3 out of 5 stars', 'review_count': '1,330', 'price': '$36.99'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#99', 'item_name': '\n            Fujifilm instax Mini 9 Instant Camera (Ice Blue) with Film Twin Pack Bundle (2 Items)\n        ', 'star_rating': '4.4 out of 5 stars', 'review_count': '1,159', 'price': '$65.48'}
2020-02-06 06:53:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics?_encoding=UTF8&pg=2>
{'ranking': '#100', 'item_name': '\n            TCL 32S325 32 Inch 720p Roku Smart LED TV (2019)\n        ', 'star_rating': '4.5 out of 5 stars', 'review_count': '7,583', 'price': '$127.88'}
2020-02-06 06:53:22 [scrapy.core.engine] INFO: Closing spider (finished)
2020-02-06 06:53:22 [scrapy.extensions.feedexport] INFO: Stored csv feed (100 items) in: output/amazon_bestseller_2020-02-06T11-53-20.csv
2020-02-06 06:53:22 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 828,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 84189,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 3,
 'elapsed_time_seconds': 1.241991,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 2, 6, 11, 53, 22, 102269),
 'item_scraped_count': 100,
 'log_count/DEBUG': 103,
 'log_count/INFO': 14,
 'request_depth_max': 1,
 'response_received_count': 3,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 2, 6, 11, 53, 20, 860278)}
2020-02-06 06:53:22 [scrapy.core.engine] INFO: Spider closed (finished)

Process finished with exit code 0
    
```
