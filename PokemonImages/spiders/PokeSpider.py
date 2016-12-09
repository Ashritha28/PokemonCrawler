import scrapy
import urllib.parse
import re
from scrapy.spiders import Spider
from urllib.parse import urljoin
from PokemonImages.items import PokemonimagesItem
from scrapy.http import Request
from scrapy.selector import Selector

class MySpider(Spider):
    name="PokeSpider"
    allowed_domains=["pokemondb.net"]
    start_urls=["http://pokemondb.net/pokedex/national"]

    #crawledLinks = []

    def parse(self,response):
        title = response.xpath('//span/a/@href').extract()[-1]
        links = response.xpath('//span/a/@href').extract()
        #print (links)

    	#We store already crawled links in this list
        crawledLinks = []

    	#Pattern to check the proper link, we want only pokemon images
        linkPattern = re.compile("^\/pokedex\/+")

        for link in links :
    	    if linkPattern.match(link) and not ("http://pokemondb.net"+link) in crawledLinks:
                #print (link)
                #print ("http://pokemondb.net"+link)
                link = "http://pokemondb.net"+link
                #hxs = Selector(text="http://pokemondb.net"+link)
                #print (str(hxs))
    		    #sublink=str(link.xpath('//@src'))
                #sublink = str((hxs.xpath('//@src')))
                #print (sublink)
    		    #if (sublink.endswith('.jpg')):
                #if (sublink.endswith('.jpg')):
                crawledLinks.append(link)
    	        #crawledLinks.append(sublink)
                yield Request(link, self.parse)

        #hxs = Selector(crawledLinks)
        sublinks = response.xpath('//@src').extract()
        #print (sublinks)
        #print ("Hi")
        for url in sublinks :
            if (url.endswith('.jpg')):
                #print (i)
                item = PokemonimagesItem()
                item['poke_title'] = title
                item['image_urls'] = [url]
                yield item


