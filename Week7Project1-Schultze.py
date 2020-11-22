fileName = input("Enter the file name: ")
#Mean#
f = open(fileName, 'r')
mean = []
for line in f:
    avg = line.split()
    for MeanNum in avg:
        mean.append(float(MeanNum))
total = sum(avg)
print(total)

#Median#
f = open(fileName, 'r')
median = []
for line in f:
    stuff = line.split()
    for MedNum in stuff:
        median.append(float(MedNum))

median.sort()
midpoint = len(median) // 2
print("Median: ", end=" ")
if len(median) % 2 == 1:
    print(median[midpoint])
else:
    print((median[midpoint] + median[midpoint - 1]) / 2)

#Mode#
f = open(fileName, 'r')
Mode = []
for line in f:
    NumInLine = line.split()
    for Num in NumInLine:
        Mode.append(Num.upper())

ModeList = {}
for Num in Mode:
    ocurr = ModeList.get(Num, None)
    if ocurr == None:
        ModeList[Num] = 1
    else:
        ModeList[Num] = ocurr + 1

theMaximum = max(ModeList.values())
for key in ModeList:
    if ModeList[key] == theMaximum:
        print("Mode: ", key)
        break
