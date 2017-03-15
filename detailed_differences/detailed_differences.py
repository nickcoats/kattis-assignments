import sys

#
# Code Sample from Kattis Detailed Differences Assignment
# URL: https://open.kattis.com/problems/detaileddifferences
# Execute: pyhton detailed_differences.py < detailed_differences.in
#

# Test cases counter and array to hold string data from input
testCases = 0
tests = []

# Parse strings from input
i = 0
for row in sys.stdin:
    if i == 0:
        testCases = int(row)
        i += 1
        continue

    # Sanitize strings and append to tests array
    tests.append(row.replace('\r', '').replace('\n', ''))


# Compare strings
for i in range(0,(testCases*2)-1,2):

    # Print comparison strings
    print tests[i]
    print tests[i+1]

    # Create lists from strings for comparison
    a = list(tests[i])
    b = list(tests[i+1])

    # Comparison results array
    comparison = []

    for k in range(0,len(a)):
        # If values are equal, append . to comparison array
        if a[k] == b[k]:
            comparison.append('.')
            continue

        # Values are different - append *
        comparison.append('*')

    # Print comparison result
    print ''.join(comparison) + '\n'
