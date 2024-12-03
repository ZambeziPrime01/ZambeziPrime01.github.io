#define again() function to ask user if they want to user the calculator again
def again() :
#take input from user 
 calc_again = input('''Do you want to calculate again? Please type Y for YES and N for no.''')
#if user types Y, run the calculate() function
if calc_again == 'Y':
    calculate()
#if user types N, say good-bye to the user and end the program
elif calc_again == 'N':
    print('See you later.')
#if user types another key, run the function again
else:
    again()