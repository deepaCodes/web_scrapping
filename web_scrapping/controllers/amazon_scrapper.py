from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from web_scrapping.spiders.amazon_bestseller import AmazonBestsellerSpider

"""
    Running spiders: script for running spiders
"""


def run():
    settings = get_project_settings()
    # settings.set('FEED_FORMAT', 'json')
    # settings.set('FEED_URI', 'result.json')

    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

    runner = CrawlerRunner(settings)
    runner.crawl(AmazonBestsellerSpider)

    _deferred = runner.join()
    _deferred.addBoth(lambda _: reactor.stop())

    reactor.run()  # the script will block here until all crawling jobs are finished


if __name__ == '__main__':
    run()
