import scrapy
import re

class Ebay1spiderSpider(scrapy.Spider):
    name = "ebay1spider"
    allowed_domains = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/sch/i.html?_nkw=laptop&_fcid=3"]

    page_count = 0
    max_pages = 2  # Stop after 2 pages
    
    custom_headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.ebay.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-EBAY-C-MARKETPLACE-ID': 'EBAY-GB',
        'sec-ch-ua': '"Google Chrome";v="124", "Chromium";v="124", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0'
    }

    def parse(self, response):
        self.page_count += 1
        if self.page_count > self.max_pages:
            return

        product_links = response.xpath('//a[@class="s-item__link"]/@href').getall()
        for link in product_links:
            yield response.follow(
                link,
                callback=self.parse_product,
                meta={'page_link': response.url},
                headers=self.custom_headers
            )

        next_page = response.xpath('//a[@aria-label="Go to next search page"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        item = {
            'Pagination_Link': response.meta['page_link'],
            'Product_link': response.url,
            'Product_title': response.xpath('//h1[@class="x-item-title__mainTitle"]/span/text()').get(),
            'Product_Price': response.xpath('//div[@class="x-price-primary"]/span/text()').get(),
            'Product_images': ', '.join(re.findall(r'"ZOOM_GUID","URL":"(.*?)"', response.text)[:10])
        }
        yield item
