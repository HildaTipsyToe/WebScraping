import json
import os
import string
import time

from MethodExtractFromDino import DinosuarExtraction
import concurrent.futures
from threading import Thread

DinosuarNames = []



scrap = DinosuarExtraction
class DinosaurExtration:
    def __init__(self):
        self.i = 0
        self.Failed = 0
        self.running = 0

    def run(self):
        #It works right now, if I remove the Threading. but implementation of threading would be nice :)
        for letter in string.ascii_lowercase[:27].split(" ")[0]:
            names = self.getDinosaursFromAToB((f'https://www.nhm.ac.uk/discover/dino-directory/name/{letter}/gallery.html'))
            while (letter == "k" and len(names) == 0):
                names = self.getDinosaursFromAToB((f'https://www.nhm.ac.uk/discover/dino-directory/name/{letter}/gallery.html'))
            for name in names:
                DinosuarNames.append(name.lower())
        print(DinosuarNames)
        print(len(DinosuarNames))


        '''with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(self.getDinosaursFromAToB, string.ascii_lowercase[:27].split(" ")[0])
        print(len(DinosuarNames))'''
        #with concurrent.futures.ThreadPoolExecutor() as executor:
        #    executor.map(self.dinosss, DinosuarNames)

        #    for name in DinosuarNames:
        #            Thread(target=self.dinosss, args=(name,), daemon=True).start()

        #while(self.i + self.Failed != len(DinosuarNames)):
        #    print("Done")

    def dinosss(self, name):
        self.running += 1
        url = (f'https://www.nhm.ac.uk/discover/dino-directory/{name}.html')
        if self.ImportToJsonFile(self.getInfo(url), self.getName(url), self.getImage(url)) == True:
            self.i += 1
            self.running -= 1
            return print(self.i, " out of ", len(DinosuarNames))
        else:
            self.running -= 1
            return print('Failed to get the info from: %s' % name)


    def getDinosaursFromAToB(self, Url):
        DinosList = []
        print(Url)
        for item in scrap.webSearch(scrap, Url, 'li', 'dinosaurfilter--dinosaur', True):
            DinosList.append(item.replace("-", ""))
        print(len(DinosList))
        return DinosList

    def getInfo(self, url):
        Dinolist = scrap.webSearch(scrap, url, 'dl', '', True)
        return Dinolist
    def getName(self, url):
        Dinolist = scrap.webSearch(scrap, url, 'h1', '', True)
        return Dinolist[0]
    def getImage(self, url):
        img = scrap.webSearchForImages(scrap, url, 'img', 'dinosaur--image', False)
        return img

    def ImportToJsonFile(self, Dinolist, name, img):
        Dictionary = {'name': name, 'image': img}
        if os.path.exists("DinoFolder/%s.JSON" % name):
            os.remove("DinoFolder/%s.JSON" % name)
        with open("DinoFolder/%s.JSON" % name, "a+") as JsonFile:
            for i, item in enumerate(Dinolist):
                if i % 2 == 0:
                    Dictionary[Dinolist[i]] = Dinolist[i+1]
            try:
                JsonFile.write(json.dumps(Dictionary))
                return True
            except TypeError:
                print("unable to dump shit in")
                print(TypeError)


DinosaurExtration().run();
