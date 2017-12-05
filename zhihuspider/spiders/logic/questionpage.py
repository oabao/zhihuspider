from scrapy.http import Request

from zhihuspider.spiders.commons import Commons
from zhihuspider.spiders.config import Config


class QuestionPageParser(object):
    def get_default_ques_page(self, id, url):
        return [Request(url, headers=Config.headers, meta={"id":id}, callback=self.parse_default_ques_page)]

    def parse_default_ques_page(self, response):
        description = response.xpath('//span[@class="RichText"]/text()').extract()
        if Config.debug:
            if len(description) > 0:
                print("parse_default_ques_page:",description[0])
        Commons.commit_item(datatype=Config.question_type, id=[response.meta["id"]], content=description)
