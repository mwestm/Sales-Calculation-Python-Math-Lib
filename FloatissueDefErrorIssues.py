# 
#python saved for the sum function
import math

#NUM_DAYS is used as a constant, 7 assuming open all days of week
NUM_DAYS = 7
#start main
def main():
    write_to_file()
    read_to_file()
#launch 1st
def write_to_file ():
    # Create a list to hold daily sales
    dsales = [0] * NUM_DAYS
try:
    fname = open('daysales.txt', 'w') 
        # Get each days sales
    for index in range(NUM_DAYS):
        print('Enter the sales for Day ',index + 1, sep='')
        dsales = float((input()))       
except IOerror:
    print('Error occured with input.')
except ValueError:
    print('Non-numeric characters found.')
    fname.write(dsales + '\n')
fname.close()
          
    
#launch 2nd    
def read_to_file (): #read file, make them floats, calc using sum/map
    try:
        fname = open('daysales.txt', 'r')
        for line in fname:
            amount = float(line)
            totalPrice = sum(map(float, fname)) + amount
            print(totalPrice)
        fname.close()
    except IOerror:
        print('Error occured while reading.')
    except ValueError:
        print('Non-numeric characters found.')

# Call the main function and its over so end program
main()
