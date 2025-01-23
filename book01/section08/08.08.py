try:
    first_side = float(input('Enter the first side of the triangle: '))
    if first_side <= 0:
        print('The side of a triangle cannot be zero or a negative number.')
    else:
        second_side = float(input('Enter the second side of the triangle: '))
        if second_side <= 0:
            print(
                'The side of a triangle cannot be zero or a negative number.'
            )
        else:
            third_side = float(input('Enter the third side of the triangle: '))
            if third_side <= 0:
                print('The side of a triangle cannot'
                      'be zero or a negative number.')
            else:
                if (first_side + second_side <= third_side or
                   first_side + third_side <= second_side or
                   second_side + third_side <= first_side):
                    print('The entered sides do not form a valid triangle.')
                elif first_side == second_side == third_side:
                    print('The triangle is equilateral.')
                elif first_side != second_side != third_side:
                    print('The triangle is scalene.')
                else:
                    print('The triangle is isosceles.')
except ValueError:
    print('Please enter a valid number.')
