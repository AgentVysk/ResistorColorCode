# bk br rd og yw gn bl vt gy wt
# 0  1  2  3  4  5  6  7  8  9
import pyttsx3
engine = pyttsx3.init()
print("<<< bk br rd og yw gn bl vt gy wt >>>")

def color2numberer(input):
    if input == "bk":
        return 0
    if input == "br":
        return 1
    if input == "rd":
        return 2
    if input == "og":
        return 3 
    if input == "yw":
        return 4
    if input == "gn":
        return 5
    if input == "bl":
        return 6
    if input == "vt":
        return 7
    if input == "gy":
        return 8
    if input == "wt":
        return 9

def Calculator(nlist, tenpower, tot):
    if tot == 2:
        return ((nlist[0]*10)+(nlist[1]))*(10**tenpower)
    
    if tot == 3:
        return ((nlist[0]*100)+(nlist[1]*10)+(nlist[2]))*(10**tenpower)

    if tot == 4:
        return ((nlist[0]*1000)+(nlist[1]*100)+(nlist[2]*10)+(nlist[3]))*(10**tenpower)

cCode = []

num = int(input("how many color lines excluding the tolerances: "))

for i in range(0,num):
    line = input("Enter the colour of line ("+str(i+1)+"): ")
    cCode.append(line)

val = []

for elements in cCode:
    value = color2numberer(elements)
    val.append(value)

# print(val)

tenPower = val[num-1]
numlist = []
for i in range(0, num-1):
    numlist.append(val[i])

tot = len(numlist)

bigVal = Calculator(numlist, tenPower, tot)
# print(bigVal)

print("..................................................")
print()
if len(str(bigVal)) <= 3:
    finalVal = bigVal
    print(finalVal, "ohms")
    finalspeak = str(finalVal)+"ohms"
if len(str(bigVal)) > 3 and len(str(bigVal)) <= 6:
    finalVal = bigVal/1000
    print(finalVal, "K ohms")
    finalspeak = str(finalVal)+ "kilo ohms"
if len(str(bigVal)) > 6:
    finalVal = bigVal/1000000
    print(finalVal, "M ohms")
    finalspeak = str(finalVal)+ "mega ohms"
print()
print("..................................................")

engine.say(finalspeak)
engine.runAndWait()

input("Press Enter to exit...")