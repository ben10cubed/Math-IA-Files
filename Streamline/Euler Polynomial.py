import math
import os


def magnitudeX(x,y):
    num1 = 8.57277822217765E-11*pow(y,12)+ 1.22964317509335E-11*pow(y,(11))-3.1667097651394E-08*pow(y,10) - 6.78104898620738E-09*pow(y,9)
    num2 = 4.28191984236372E-06*pow(y,8) +1.47104788236869E-06*pow(y,7) -0.000266432419165233*pow(y,6) -0.000156588462134784*pow(y,5)
    num3 = 0.0082857941613217*pow(y,4) + 0.00881914596473338*pow(y,3) -0.153422597606132*pow(y,2) -0.11325832901437*y + 1.77315789473652
    return num1 + num2 + num3

def magnitudeY(x,y):
    num1 = 8.94503461399417*pow(10,-12)*pow(x,10) + 6.46819054271168*pow(10,-11)*pow(x, 9) - 7.88368957509758*pow(10, -9)*pow(x,8) - 4.73489528259461*pow(10,-8)*pow(x,7)
    num2 = 2.33880223338077*pow(10,-6)*pow(x,6) + 0.0000129401005498166*pow(x,5) - 0.000231123250510157*pow(x,4) - 0.00231804648813399*pow(x,3)
    num3 = -1 * 0.00199999943818308*pow(x,2) + 0.233982539432648*(x) + 0.732241972868306
    return num1 + num2 + num3

dt = 0.1

print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cnt = 1
for j in range (-12, 13):
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
        while (startX <= 18 and startY <= 12) and (startX >= -18 and startY >= -12):

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
