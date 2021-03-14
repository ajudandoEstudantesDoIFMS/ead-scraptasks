import scrapy
import time

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://ead.ifms.edu.br/login'] #https://ead.ifms.edu.br/

    
    def parse(self, response):
        print("=======================\n=======================\n=======================\n=======================\n=======================")
        user = "0000000"
        password = "000000"
        print(self.entrar(user,password,response))
        print(response)


    def entrar(self,user,password,response):
            scrapy.FormRequest.from_response("https://ead.ifms.edu.br/login/index.php", formdata={
            'logintoken': response.xpath('//input[@name="logintoken"]/@value').extract()[0],
            'username':user,
            'password':password
            }, callback=self.null())
    
    def null(self):
        print("login realizado...")
        time.sleep(5)
        pass

    def prin(self,response):
        print(response)

    def next(self,response):
        yield scrapy.Request(
            response.urljoin("https://ead.ifms.edu.br/my/"),
            callback=self.prin(response)
        )
        
