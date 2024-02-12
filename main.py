import json
import os
from Webscrap import Webscrap
from MethodExtractFromDino import DinosuarExtraction
import concurrent.futures

listAttributes = [
    "name",
    "image",
    "Pronunciation",
    "Name meaning",
    "Type of dinosaur",
    "Diet",
    "When it lived",
    "Found in",
    "Taxonomy",
    "Type species"
    ]

scrap = DinosuarExtraction

class DinosaurExtration:
    def __init__(self):
        self.dinos = []
        self.dataHandling = Webscrap()
        self.Everything = []
        self.getDinoInfomation = False #True
        self.dataHandlingCheckmark = True
    def run(self):
        if self.getDinoInfomation:
            self.dinos = self.dataHandling.Dinosaurscrapping()
            with open("DinoFolder/Everything.JSON", "w+") as JsonFile:
                for lines in self.dinos:
                    JsonFile.write(lines + ",\n")

        if self.dataHandlingCheckmark:
            #self.DataHandling()
            self.checkKeys()

    def DataHandling(self):
        list = []
        with open("DinoFolder/Everything.JSON", "r") as JsonFile:
            files = json.load(JsonFile)
            for js in files:
                dict = js
                if dict.get("Length") and dict.get("When it lived"):
                    list.append(dict)

        with open("DinosaurData.JSON", "w+") as JsonFile:
            listDump = json.dumps(list)
            JsonFile.write(listDump)

    def checkKeys(self):
        keys = {}
        with open("DinosaurData.JSON", "r") as JsonFile:
            files = json.load(JsonFile)
            for js in files:
                for key in js.keys():
                    if keys.get(key):
                        keys[key] = keys[key] + 1
                    else:
                        keys[key] = 1
            print(keys)

DinosaurExtration().run()
