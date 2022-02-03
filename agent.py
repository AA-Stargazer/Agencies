import scrapy
from scrapy_selenium import SeleniumRequest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from scrapy.shell import inspect_response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector


class AgentSpider(scrapy.Spider):
    name = 'agent'


    def start_requests(self):
        yield SeleniumRequest(url='https://airtable.com/shrGAmy0TzK9h73Us/tbl8gRla9VxzUnbwM',
        wait_time=10,
        screenshot=False,
        wait_until=EC.element_to_be_clickable((By.XPATH, '//div[@role="region"]')),
        callback=self.parse_result,
        )
        

    def parse_result(self, response):
        driver = response.meta['driver']
        driver.set_window_size(16000, 900)
        time.sleep(10)
        lenlen = len(driver.find_elements(By.XPATH, '//div[@class="galleryCardContainer z1"]'))
        print(f"\n\n\n{lenlen}\n\n\n")
        response0 = response.selector
        llist = []
        y = 800
        for a in range(200):
            llist2 = []
            cards = response0.xpath('//div[@class="galleryCardContainer z1"]')
            for card in cards:
                name = card.xpath('string(.//div[contains(@class, "flex")]/a)').get()
                roles = card.xpath('.//div[@class="px2 pt1 pb-half"]/div[@class="cellContainer relative"]/div/div/span/div/text()').getall()
                link = card.xpath('.//div[@class="px2 pt1 pb-half"]//div[@class="cellContainer relative"]/div[@class="cell read relative"]/div/div/text()').get()
                about = card.xpath('(.//div[@class="px2 pt1 pb-half"]//div[@class="cellContainer relative"]/div[@class="cell read relative"]/div[@class="flex-auto truncate"]/text())[1]').get()
                discord = card.xpath('(.//div[@class="px2 pt1 pb-half"]//div[@class="cellContainer relative"]/div[@class="cell read relative"]/div[@class="flex-auto truncate"]/text())[2]').get()
                ddict = {
                    'name': name,
                    'roles': roles,
                    'link': link,
                    'about': about,
                    'discord': discord
                }
                llist2.append(ddict)
            x = 0
            for i in llist2:
                if i in llist:
                    print('\n\n\nNOT YIELD DUPLICATE\n\n\n')
                else:
                    x += 1
                    llist.append(i)
                    yield i
            print(f'\n\n\n{x}\n\n\n')
            y += 800
            driver.find_element(By.XPATH, '//div[@id="viewContainer"]//div[@id="galleryView"]//div[@class="light-scrollbar animateCards"]').send_keys(Keys.PAGE_DOWN)

            time.sleep(5)
            response0 = Selector(text=driver.page_source)

        
        




        # inspect_response(response,self)
