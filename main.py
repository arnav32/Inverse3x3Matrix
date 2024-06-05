# Script to inverse any given 3x3 matrix.
# Coded and tested start-to-finish in 15 minutes (excluding time taken to do algebra)

print("Enter the numbers in each row, separated by spaces (e.g. 7 2 14).\n")
row1 = [float(x) for x in input("Enter first row:  ").split(" ")]
row2 = [float(x) for x in input("Enter second row: ").split(" ")]
row3 = [float(x) for x in input("Enter third row:  ").split(" ")]

# row1 = [1, 4, 2]
# row2 = [9, 5, 4]
# row3 = [6, 2, 7]

a, b, c = row1
d, e, f = row2
g, h, i = row3

det = (a * (e*i - f*h)) - (b * (d*i - f*g)) + (c * (d*h - e*g))
CT = [[e*i - f*h, c*h - b*i, b*f - c*e],
     [f*g - d*i, a*i - c*g, c*d - a*f],
     [d*h - e*g, b*g - a*h, a*e - b*d]]

inverse = [[round((item/det), 3) for item in row]
           for row in CT]

print()
for row in inverse:
    print(row)