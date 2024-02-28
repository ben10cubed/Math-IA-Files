#Two functions
#Our dydt and dxdt are just our vector magnitude functions


#To Do:
#Do some testing first as to how to get the data and write it into a txt file
#Each line will most likely have data regarding x,y coordinates
#These can be strung together to form streamline

# a = 1.1015;
# b = -0.0394;
# c = -0.1059;
# d = 1.0627;
# u = (1.16323 * sin(0.40547 * (c * x + d * y) + 2.14085) + 0.55023)-(-0.0956 * (c*x + d*y)-0.1387);
# v = (1.1374957 * sin(0.222722 * (a * x + b * y) + 6.60815) + 0.368331);

import math
import os

def magnitudeX(x,y):
    c = -0.1059
    d = 1.0627
    return (1.16323 * math.sin(0.40547 * (c * x + d * y) + 2.14085) + 0.55023)-(-0.0931 * (c*x + d*y)-0.1265)

def magnitudeY(x,y):
    a = 1.1015
    b = -0.0394
    return (1.1374957 * math.sin(0.222722 * (a * x + b * y) + 6.60815) + 0.368331)

dt = 0.1 #Seconds

print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cnt = 1
for j in range (-14, 15):
    for i in range(-18,19):
        startY = j
        startX = i
        fileName1 = "data" + str(cnt) + ".txt"
        cnt += 1
        fileName2 = "data" + str(cnt) + ".txt"
        cnt += 1
        f1 = open(fileName1, "w")
        f2 = open(fileName2, "w")
        datacount = 0
        while (startX <= 18 and startY <= 14) and (startX >= -18 and startY >= -14):

            #print(magnitudeX(startX, startY), magnitudeY(startX, startY))
            magX = magnitudeX(startX,startY)
            magY = magnitudeY(startX,startY)
            if abs(magX) <= 1e-5 and abs(magY) <= 1e-5:
                break
            if datacount >= 1000:
                break
            startX = startX + magX*dt
            startY = startY + magY*dt
            toWrite1 = str(startX)
            toWrite2 = str(startY)
            datacount += 1
            f1.write(toWrite1)
            f1.write('\n')
            f2.write(toWrite2)
            f2.write('\n')
        f1.close()
        f2.close()
        if datacount == 0:
            os.remove(fileName1)
            os.remove(fileName2)