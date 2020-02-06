# -*- coding: utf-8 -*-
import scrapy


class AmazonBestsellerSpider(scrapy.Spider):
    name = 'amazon_bestseller'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics']

    def parse(self, response):
        self.logger.info('%s spider parsing  on %s', self.name, response.url)
        ordered_list_items = response.xpath('//ol[@id="zg-ordered-list"]//li')
        for item in ordered_list_items:
            yield self._parse_item(item)

        for href in response.css('ul.a-pagination li.a-last ::attr(href)').getall():
            self.logger.info('following to next page: %s', href)
            yield response.follow(href, self.parse)

    def _parse_item(self, item):
        item_data = {
            'ranking': item.css('span.a-list-item span.zg-badge-text ::text').get(),
            'item_name': item.xpath('.//span/div/span/a/div/text()').get(),
            'star_rating': item.css('div.a-icon-row i.a-icon-star ::text').get(),
            'review_count': item.css('div.a-icon-row a.a-size-small ::text').get(),
            'price': item.css('div.a-row span.a-color-price ::text').get()
        }
        item_data['item_name'] = str(item_data['item_name']).strip()
        return item_data
