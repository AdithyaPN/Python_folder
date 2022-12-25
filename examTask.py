score = 0
def total_score():
    score = score+1

def select_test():
    print('\nOnline Examination')
    print('1.Python')
    print('2.PHP')
    print('3.Flutter')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        print('Welcome to python examination')
        python_test()

    elif choice ==2:
        print('Welcome to php examination')
        #php_test()

    elif choice ==3:
        print('Welcome to Flutter examination')
        #flutter_test()

    else: 
        print('Invalid choice!!!')
        select_test()


#fuction for python test
def python_test():

    def python_first_qst():
        print('\n1: Who first developed python?')
        print('a.Guido Van Russom')
        print('b.Dennis Ritchie')
        print('c.James Gosling')
        answer1 = input('Enter your answer: ')

        if answer1 == 'a':
            print('Correct')
            # total_score()
            python_second_qst()

        elif answer1 == 'b':
            print('Wrong answer')
            total_score()
            python_second_qst()

        elif answer1 == 'c':
            print('Wrong answer')
            # total_score()
            python_second_qst()

        else:
            print('\nInvalid option')
            python_first_qst()
    python_first_qst()

    def python_second_qst():
        print('\n1: Which is not an oops below?')
        print('a.Java')
        print('b.Python')
        print('c.C')
        answer1 = input('Enter your answer: ')

        if answer1 == 'a':
            print('Wrong answer')
            # total_score()
            #python_third_qst()

        elif answer1 == 'b':
            print('Wrong answer')
            # total_score()
            #python_third_qst()

        elif answer1 == 'c':
            print('Corect')
            # total_score()
            #python_third_qst()

        else:
            print('\nInvalid option')
            python_second_qst()
    python_second_qst()
    #write more python questions
    #python test ends here

select_test()
