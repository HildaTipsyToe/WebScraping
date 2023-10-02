from bs4 import BeautifulSoup
import requests
import re
headers = {
        'authority': "",
        'cache-control': "max-age=0",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'sec-fetch-site': "none",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9"
    }
payload = ""
querystring = {"shape": "((wt_{F`m{e@njvAqoaXjzjFhecJ{ebIfi}L))"}
class DinosuarExtraction:
    def webSearch(self, url, HtmlTag, className='', fullFormat=False, splitter='\n|\t'):

        page = requests.request("GET", url, headers=headers, data=payload, params=querystring)
        soup = BeautifulSoup(page.text, features="html.parser")

        if className != '':
            WebPage = soup.find_all(HtmlTag, class_=className)
        else:
            WebPage = soup.find_all(HtmlTag)
        if fullFormat == False:
            return WebPage
        else:
            return self.PageTextToList(DinosuarExtraction, WebPage, splitter)


    def PageTextToList(self, data, splitter):
        list = []

        for line in data:

            tempList = re.split(splitter, line.text)


            for x in range(len(re.split(splitter, line.text))):
                if tempList[x] != "":
                    '''Hvis nogle af ordene bliver splittet, fordi de har \n eller \t f.eks men de skal rigtig være samlet'''
                    if tempList[x].endswith(","):
                        test = tempList[x]
                        '''looper igennem alle ordene efter det givet value for at finde dem der mangler'''
                        for index in range(len(tempList) - x):
                            if x + index < len(tempList):
                                if tempList[x + index] != "" and tempList[x] != tempList[x + index]:
                                    test += " " + tempList[x + index]
                                    '''erstatter orderet der bliver smidt i 
                                    med en tom string, så den bliver sprunget over'''
                                    tempList[x + index] = ""
                            else:
                                pass
                        list.append(test)
                    else:
                        list.append(tempList[x])
        return list


    def webSearchForImages(self, url, HtmlTag, className='', fullFormat=False, splitter='\n|\t'):

        page = requests.get(url)
        soup = BeautifulSoup(page.text, features="html.parser")

        if className != '':
            WebPage = soup.find_all(HtmlTag, class_=className)
        else:
            WebPage = soup.find_all(HtmlTag)
        if fullFormat == False:
            for item in WebPage:
                return item['src']