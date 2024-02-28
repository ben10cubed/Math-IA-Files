import math
import os

# a = 1.1015;
# b = -0.0394;
# c = -0.1059;
# d = 1.0627;
# u = (1.16323 * sin(0.40547 * (c * x + d * y) + 2.14085) + 0.55023)-(-0.0956 * (c*x + d*y)-0.1387);
# v = (1.1374957 * sin(0.222722 * (a * x + b * y) + 6.60815) + 0.368331);

# def magnitudeX(x,y):
#     c = -0.1059
#     d = 1.0627
#     return (1.16323 * math.sin(0.40547 * (c * x + d * y) + 2.14085) + 0.55023)-(-0.0931 * (c*x + d*y)-0.1265)/10 + 4.225606385

# def magnitudeY(x,y):
#     a = 1.1015
#     b = -0.0394
#     return (1.1374957 * math.sin(0.222722 * (a * x + b * y) + 6.60815) + 0.368331)/10 + 4.259606869

def magnitudeX(x,y):
    num1 = 8.57277822217765E-11*pow(y,12)+ 1.22964317509335E-11*pow(y,(11))-3.1667097651394E-08*pow(y,10) - 6.78104898620738E-09*pow(y,9)
    num2 = 4.28191984236372E-06*pow(y,8) +1.47104788236869E-06*pow(y,7) -0.000266432419165233*pow(y,6) -0.000156588462134784*pow(y,5)
    num3 = 0.0082857941613217*pow(y,4) + 0.00881914596473338*pow(y,3) -0.153422597606132*pow(y,2) -0.11325832901437*y + 1.77315789473652
    return (num1 + num2 + num3)/10 + 4.225606385

def magnitudeY(x,y):
    num1 = 8.94503461399417*pow(10,-12)*pow(x,10) + 6.46819054271168*pow(10,-11)*pow(x, 9) - 7.88368957509758*pow(10, -9)*pow(x,8) - 4.73489528259461*pow(10,-8)*pow(x,7)
    num2 = 2.33880223338077*pow(10,-6)*pow(x,6) + 0.0000129401005498166*pow(x,5) - 0.000231123250510157*pow(x,4) - 0.00231804648813399*pow(x,3)
    num3 = -1 * 0.00199999943818308*pow(x,2) + 0.233982539432648*(x) + 0.732241972868306
    return (num1 + num2 + num3)/10 + 4.259606869

def NOmagnitudeX(x,y):
    return 4.225606385

def NOmagnitudeY(x,y):
    return 4.259606869


print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cnt = 1
changeCnt=1
datacount=0

interval = [0.1, 0.5, 1.5]

for dt in interval:
    startY = -8
    startX = -18
    fileName1 = "data" + str(cnt) + ".txt"
    cnt += 1
    fileName2 = "data" + str(cnt) + ".txt"
    cnt += 1
    f1 = open(fileName1, "w")
    f2 = open(fileName2, "w")
    f1.write(str(-18))
    f1.write('\n')
    f2.write(str(-8))
    f2.write('\n')
    datacount = 0
    time = 0
    #print("x-coord:", startX, "y-coord:", startY)

    #print(dt)
    while (startX <= 0.85215 or startY <= 11.00384) and (startX >= -18 and startY >= -14):
    #while time < 5.5:
        time = time + dt
        #print(magnitudeX(startX, startY), magnitudeY(startX, startY))
        #print("x-coord:", startX, "y-coord:", startY)

        magX = magnitudeX(startX,startY)
        magY = magnitudeY(startX,startY)
        if abs(magX) <= 1e-5 and abs(magY) <= 1e-5:
            break
        if datacount >= 100000:
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
    #print("x-coord:", startX, "y-coord:", startY)

    f1.close()
    f2.close()
    if datacount == 0:
        os.remove(fileName1)
        os.remove(fileName2)
    dt = dt * 10



startY = -8
startX = -18
fileName1 = "data" + str(7) + ".txt"
fileName2 = "data" + str(8) + ".txt"
f1 = open(fileName1, "w")
f2 = open(fileName2, "w")
f1.write(str(-18))
f1.write('\n')
f2.write(str(-8))
f2.write('\n')
datacount = 0
time = 0
dt=0.1
while (startX <= 0.85215 or startY <= 11.00384) and (startX >= -18 and startY >= -14):
    time = time + dt
    #print(magnitudeX(startX, startY), magnitudeY(startX, startY))
    magX = NOmagnitudeX(startX,startY)
    magY = NOmagnitudeY(startX,startY)
    if abs(magX) <= 1e-5 and abs(magY) <= 1e-5:
        break
    if datacount >= 100000:
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