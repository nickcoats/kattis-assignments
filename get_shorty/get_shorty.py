import sys

#
# Code Sample from Kattis Get Shorty Assignment
# URL: https://open.kattis.com/problems/getshorty
# Execute: pyhton get_shorty.py < get_shorty.in
#

tests = []
testSet = []

i = 0
valid = False
validData = False
for row in sys.stdin:

    row = row.replace('\r', '').replace('\n', '')
    row = row.split()

    if len(row) == 2 and int(row[0]) == 0 and row[0] == row[1]:
        tests.append(testSet)
        break

    if len(row) == 2:
        if (int(row[0]) >= 2 and int(row[0]) <= 10000) and (int(row[1]) >= 1 and int(row[1]) <= 15000):

            row[0] = int(row[0])
            row[1] = int(row[1])

            if i == 0:
                valid = True
                testSet.append(row)
                i += 1
                continue

            valid = True
            if validData == True:
                tests.append(testSet)

            testSet = []
            testSet.append(row)
        else:
            valid = False
            testSet = []

    if len(row) == 3 and valid == True:
        passed = False

        row[0] = int(row[0])
        row[1] = int(row[1])

        if float(row[2]) >= 0.00 and float(row[2]) <= 1.00:
            passed = True
            row[2] = float(row[2])

        if passed:
            validData = True
            testSet.append(row)
        else:
            validData = False



for test in tests:

    mikaelSize = 0.00
    startSize = 1.00
    stop = test[0][0] - 1

    for i in range(1,len(test)):
        startSize = startSize * test[i][2]

        if test[i][0] == stop or test[i][1] == stop:
            if startSize > mikaelSize:
                mikaelSize = startSize
                startSize = 1.00
                continue


    print '{0:.4f}'.format(mikaelSize)
