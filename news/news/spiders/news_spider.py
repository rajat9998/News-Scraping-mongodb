import scrapy
import validators

class NewsSpider(scrapy.Spider):

    name = "news"

    start_urls = ['https://news.ycombinator.com/']

    allNews = []

    def parse(self, response):

        votes = [int(vote.split(' ')[0]) for vote in response.css('.score::text').extract()]        

        for post, vote in zip(response.css('.itemlist .athing'), votes):

            self.allNews.append({
                'title': post.css('.title a::text').get(),
                'url': post.css('.title a::attr(href)').get(),
                'votes': vote
            })        

        next_page = response.css('.title a::attr(href)')[-1].get()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
        
        yield scrapy.Request(url=response.url, callback=self.next_requests)
        

    def next_requests(self, response):        

        next_urls = [item['url'] for item in self.allNews]        

        for url in next_urls:
            if validators.url(url):                
                yield scrapy.Request(url=url, callback=self.parseNext)

    def parseNext(self, response):

        try:
            url = response.url
            for item in self.allNews:
                if url in item['url']:

                    yield {                        
                        'url': item['url'],
                        'blog_heading': response.css('title::text').get(),                        
                        'title': item['title'],
                        'desc': response.css('body p::text').get(),
                        'img_url':  response.css('body img::attr(src)').get(),
                        'votes': item['votes']                        
                    }
            
        except Exception as e:
            print(e)


