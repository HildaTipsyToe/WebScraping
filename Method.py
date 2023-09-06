import json
import os
from bs4 import BeautifulSoup
import requests

class WebScrapping:
    def webSearch(self, url, HtmlTag, className='', fullFormat=False, splitter='\n'):

        page = requests.get(url)
        soup = BeautifulSoup(page.text, features="html.parser")

        if className != '':
            WebPage = soup.find_all(HtmlTag, class_=className)
        else:
            WebPage = soup.find_all(HtmlTag)

        if fullFormat == False:
            return WebPage
        else:
            return self.PageTextToList(WebScrapping, WebPage, splitter)


    def PageTextToList(self, data, splitter):
        for line in data:
            text = line.text.split(splitter)
            if text[0] == '':
                text.pop(0)
            if text[len(text) - 1] == '':
                text.pop(len(text) - 1)

        return text
