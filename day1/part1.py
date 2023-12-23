import os
import sys

def GetCalibration(input):
    calibration = 0
    for line in input:
        first = 0
        last = None
        for char in line:
            if char.isdigit():
                if not last:
                    last = int(char)
                else:
                    if not first:
                        first = int(last) *10 
                    last = int(char)
        if not first:
            first = 10 * last 
        calibration += first + last

    return calibration

def ReadInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return myfile.readlines()
    
if __name__== '__main__':
    data = ReadInput('input.txt')
    calibration = GetCalibration(data)
    print(calibration)