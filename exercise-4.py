# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('=====================================================================')
print('Enter the lengths of a triangle in the three prompts!')
print('=====================================================================')

a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))

if a == b and b ==c:
    print('=====================================================================')
    print(f"A tringle with sides of {a}, {b}, and {c} is an equalateral triangle")
elif a != b and b != c and a != c:
    print('=====================================================================')
    print(f"A triangle with sidea of {a}, {b}, and {c} is an scalene triangle")
    print('=====================================================================')

else:
    print('=====================================================================')
    print(f"A triangle with sides of {a}, {b}, and {c} is an isosceles triangle")
    print('=====================================================================')
