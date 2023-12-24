import os
import sys
import re
import collections
from typing import Dict

class Game:
    def __init__(self) -> None:
        self.gameinfo = {}

    def IDSum(self, rmax, gmax, bmax):
        sum = 0
        for key, values in self.gameinfo.items():
            sum += key
            for r,g,b in values:
                if not (r <=rmax and g<=gmax and b <=bmax):
                    sum -= key
                    break 
        return sum
    
    def PowCubes(self):
        sum = 0
        for values in self.gameinfo.values():
            rm,gm,bm=0,0,0
            for value in values:
                rm =value[0] if value[0]>rm else rm
                gm =value[1] if value[1]>gm else gm
                bm =value[2] if value[2]>bm else bm
            sum += rm*gm*bm
        return sum


        

    def ReadInput(self, inputfile):
        with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
            for line in myfile:
                id,games  = re.findall(r'Game\s*(\d+)\s*:(.*)', line)[0]
                self.gameinfo[int(id)] = []
                for game in games.split(";"):
                    red,blue,green=0,0,0
                    for result in re.findall(r'(\d+)\s*(red|green|blue)', game):
                        red = int(result[0]) if result[1] == 'red' else red
                        blue = int(result[0]) if result[1] == 'blue' else blue
                        green = int(result[0]) if result[1] == 'green' else green
                    self.gameinfo[int(id)].append((red,green, blue))
        return self



    
if __name__== '__main__':
    sum = Game().ReadInput('input.txt').PowCubes()
    print(sum)