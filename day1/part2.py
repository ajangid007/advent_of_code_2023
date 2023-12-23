import os
import sys
import re

numMap = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven':7,
    'eight':8,
    'nine': 9,
    'zero': 0
}

def GetCalibration(input):
    calibration = 0
    for line in input:
        found = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        if found:
            calibration = (int(found[0])*10 if found[0].isdigit() else numMap[found[0]] * 10) + (int(found[-1]) if found[-1].isdigit() else numMap[found[-1]])
    return calibration

def ReadInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return myfile.readlines()
    
if __name__== '__main__':
    data = ReadInput('input.txt')
    calibration = GetCalibration(data)
    print(calibration)