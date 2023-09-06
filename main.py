import json
import os
from bs4 import BeautifulSoup
import requests
from Method import WebScrapping


class DinosaurExtration:

    def run(self):

        url = 'https://www.nhm.ac.uk/discover/dino-directory/tyrannosaurus.html'
        DinoDictionary = {}
        scrap = WebScrapping
        list = scrap.webSearch(scrap, url, 'dl', 'dinosaur--name-description', True)

        self.ImportToJsonFile(list)


    def ImportToJsonFile(self, list):
        Dictionary = {}
        if os.path.exists("Dino.JSON"):
            os.remove("Dino.JSON")
        with open("Dino.JSON", "a+") as JsonFile:
            for i, item in enumerate(list):
                if True == True:
                    print(item)
                    Dictionary[item] =


        print(Dictionary)


DinosaurExtration().run();
'''
if os.path.exists("Dino.JSON"):
    os.remove("Dino.JSON")
JsonFile = open("Dino.JSON", "a+")
'''

''' i = 0
    u = 1
    for x in range(len(item)):
        DinoDictionary[item[i]] = item[u]
        if u == len(newerList) - 1:
            break
        i += 2
        u += 2

JsonFile.write(json.dumps(DinoDictionary))

for item in DinoDictionary:
    print(item + " " + DinoDictionary[item])
    print("")'''


#<div class ="dinosaur--container" >