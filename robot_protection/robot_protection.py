import sys

#
# Code Sample from Kattis Robot Protection Assignment
# URL: https://open.kattis.com/problems/robotprotection
# Execute: pyhton robot_protection.py < robot_protection.in
#

tests = []
testSet = []

i = 0
validData = True
for row in sys.stdin:
    row = row.replace('\r', '').replace('\n', '')
    row = row.split()

    if len(row) == 1 and i > 0:
        if validData == True:
            tests.append(testSet)

        validData = True
        testSet = []

    if len(row) == 2:
        x = int(row[0])
        y = int(row[1])

        if abs(x) > 10000 or abs(y) > 10000:
            validData = False

        row[0] = x
        row[1] = y
        testSet.append(row)

    i = 1

for test in tests:
    n = len(test)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += test[i][0] * test[j][1]
        area -= test[j][0] * test[i][1]
    area = abs(area) / 2.0
    print area
