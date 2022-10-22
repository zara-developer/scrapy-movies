
import scrapy


import requests
from bs4 import BeautifulSoup
from ..items import MoviesItem
import json
import time

class ManzoomSpider(scrapy.Spider):
    name='Manzoom'

    def start_requests(self):
        resp=requests.get('https://www.manzoom.ir/foreign/imdbtop250/')
        content=resp.text
        s=BeautifulSoup(content,"html.parser")
        # print(s)
        urls=[]
        items=s.find_all('a',attrs={"class":"m-r-2"})
        with open('movies_250_url.txt', 'w') as f:

            for item in items:
                url=item['href']
                urls.append(url)
                f.write("%s\n" % url)

        urls=open('movies_250_url.txt').read().splitlines()
        print(len(urls))
        for url in urls[:20]:
            # time.sleep(0.1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movie=MoviesItem()

        Title=response.xpath('//*[@id="main-page-part"]/div[1]/div[2]/div[2]/div[1]/h1/text()').get()#.split('(')[0]
        Abstract=response.xpath('///*[@id="main-page-part"]/div[1]/div[2]/div[4]/text()').get()
        Director=response.xpath('//*[@id="main-page-part"]/div[1]/div[2]/div[5]/div[1]/span[2]/a/text()').get()
        Type=response.xpath('//*[@id="main-page-part"]/div[1]/div[2]/div[2]/div[4]/div[3]/span/text()').get()
        Rate=response.xpath('//*[@id="main-page-part"]/div[1]/div[2]/div[2]/div[3]/div[1]/text()').get()
        Poster_URL=response.xpath('//*[@id="main-page-part"]/div[1]/div[1]/img/@src').get()
        Year=response.url.split('-')[-1]
        Rate_count=response.xpath('//*[@id="main-page-part"]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/span/text()').get()
        
        movie['Title']=Title
        movie['Abstract']=Abstract
        movie['Director']=Director
        movie['Type']=Type
        movie['Rate']=Rate
        movie['Poster_URL']=Poster_URL
        movie['Year']=Year
        movie['Rate_count']=Rate_count

        yield movie
        # yield {
        #     'Title':Title,
        #     'Abstract':Abstract,
        #     'Director':Director,
        #     'Type':Type,
        #     'Rate':Rate,
        #     'Year':Year,
        #     'Rate_count':Rate_count,
        #     'Poster_URL':Poster_URL,
        # }
