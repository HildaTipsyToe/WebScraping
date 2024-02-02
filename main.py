import json
import os
from MethodExtractFromDino import DinosuarExtraction
import concurrent.futures

scrap = DinosuarExtraction
class DinosaurExtration:
    def __init__(self):
        self.i = 0
        self.Failed = 0
        self.DinosuarNames = []
        self.failDinosuars = []
        self.CompletedDinosaurs = []
        self.dinos = []

    def run(self):
        self.Dinosaurscrapping()
        if os.path.exists("DinoFolder/Everything.JSON"):
            os.remove("DinoFolder/Everything.JSON")
        with open("DinoFolder/Everything.JSON", "w+") as JsonFile:
            for line in self.dinos:
                JsonFile.write(line + ",")


    def Dinosaurscrapping(self):
        names = self.getDinosaursFromAToB('https://www.nhm.ac.uk/discover/dino-directory/name/name-az-all.html')
        for name in names:
            self.DinosuarNames.append(name.lower())
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.getDinosaursInfomation, self.DinosuarNames)

        self.checkDownloads()
    def getDinosaursInfomation(self, name):
        url = (f'https://www.nhm.ac.uk/discover/dino-directory/{name}.html')
        if self.ImportToJsonFile(self.getInfo(url), name, self.getImage(url)):
            self.i += 1
            return print(self.i, " out of ", len(self.DinosuarNames))
        else:
            return print('---- Failed to get the info from: %s ----' % name)
        
    def getInfo(self, url):
        Dinolist = scrap.webSearch(scrap, url, 'dl', '', True)
        # self.dinos.append(Dinolist)
        return Dinolist
    
    def getImage(self, url):
        img = scrap.webSearchForImages(scrap, url, 'img', 'dinosaur--image', False)
        return img

    
    def getDinosaursFromAToB(self, Url):
        DinosList = []
        for item in scrap.webSearch(scrap, Url, 'li', 'dinosaurfilter--dinosaur', True):
            DinosList.append(item.replace("-", ""))
        return DinosList

    def ImportToJsonFile(self, Dinolist, name, img):
        Dictionary = {'name': name, 'image': img}
        if os.path.exists("DinoFolder/%s.JSON" % name):
            os.remove("DinoFolder/%s.JSON" % name)
        with open("DinoFolder/%s.JSON" % name, "w+") as JsonFile:
            for i, item in enumerate(Dinolist):
                if i % 2 == 0:
                    Dictionary[Dinolist[i]] = Dinolist[i+1]
            file = json.dumps(Dictionary)
            #JsonFile.write(file)
            self.dinos.append(file)

            if os.path.exists(f"DinoFolder/{name}.JSON"):
                return True

    def checkDownloads(self):
        for index, name in enumerate(self.DinosuarNames):
            if os.path.exists(f'DinoFolder/{name}.JSON'):
                print(f"{index + 1} out of {len(self.DinosuarNames)}, with the name of {name}")
                self.CompletedDinosaurs.append(name)
            else:
                self.failDinosuars.append(name)
        print("These dinosaurs failed!!")
        print(self.failDinosuars)






DinosaurExtration().run();
