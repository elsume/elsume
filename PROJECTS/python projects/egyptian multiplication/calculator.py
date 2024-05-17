import math # program will use abs() to evaluate if output is a negative or positive number later on

choice = input('This program finds the product of two integers with the "Ancient Egyptian" multiplication alogrithm.\nWould you like to run it? (yes/no): ')
while choice == 'yes':
    # collect user input
    while True:
        try:
            first_num = int(input('Please enter the first value of this equation: '))
            break
        except ValueError:
                print('Error! That is not a valid input!')
                print()

    while True:
        try:
            second_num = int(input('Please enter the second value of this equation: '))
            break
        except ValueError:
                print('Error! That is not a valid input!')
                print()
    print()


    # output if multiplication equals to zero
    
    if first_num == 0 or second_num == 0:
        print(f'''        A         B   Comment\n-------------------------------------------------------------------------------\n{second_num:9.0f} |{first_num:7.0f} |  Since the input(s) = 0, the calculation will stop here.\n-------------------------------------------------------------------------------''')
        print('The product of these integers will be equal to 0.')
        print()
        choice = input('Would you like to calculate a product again? (yes/no): ')
    else:


            # create lists with absolute values of inputs
        listB = []
        listA = []
        A = abs(first_num)
        B = abs(second_num)

        while B >= 1:
            listB.append(B)
            B = B // 2

        for val in listB:
            listA.append(A)
            A = A * 2


        # prints table
        print(f'        A         B   Comment\n---------------------------------------------------------------------------')
        x = 0
        for j in listA:
            print(f'{listA[x]:9.0f} |{listB[x]:7.0f} |', end="")
            if listB[x] % 2 != 0:
                print(f'  Since {listB[x]} is odd, we will add {listA[x]} to the product.')
            else:
                print(f'  Since {listB[x]} is even, we will ignore the {listA[x]}.')
            if listB[x] != 1:
                print('----------+--------+-------------------------------------------------------')           
            else:
                print('---------------------------------------------------------------------------')
            x += 1        


        # prints final product of the inputs
        print()
        sums = []
        print('Add all A values that have an odd B value to find the product:')

        i = 0
        while i < len(listA):
            if listB[i] % 2 != 0:
                if listA[i] < 0:
                    sums.append(abs(listA[i]))
                else:
                    sums.append(listA[i])
            i += 1

        counter = 1
        length = len(sums)
        for product in sums:
            print(f'{product}', end='')
            if counter < length:
                print(' + ', end='')
                counter += 1
            
            # check if product needs to be negative or positive
            else:    
                print()
                if (first_num < 0 and second_num > 0) or (first_num > 0 and second_num < 0):
                    print(f'= {(sum(sums)) * -1}')
                else:
                    print(f'= {sum(sums)}')
        # ask user if they want to run the program again
        print()
        choice = input('Would you like to calculate a product again? (yes/no): ')
print('Exiting the program - goodbye!')     