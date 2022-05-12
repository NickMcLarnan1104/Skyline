# FUNCTIONS FILE FOR TOTAL PURCHASES/FEET-TO-INCHES 
import random
import turtle
#==========================================================================

# Function to check float data type and negative values.
def checkFloatDataType():
    while True:
        
        # Try this prompt
        try:
            floatDataType = float(input())
            
        # If you get a ValueError exception this will print:
        except ValueError:
            print('ERROR: Entered the wrong data type. Re-enter a positive number for this item.')
            continue
        
        # else, If you get value <= 0 you will get another error.
        else:
            if floatDataType <= 0:
                print('ERROR: Cannot enter a negative value, please enter a positive number.')
                continue
            break
    return floatDataType

    # End checkFloatDataType function

#==========================================================================
    
# Function to add 5 values
def add_five_values(item1, item2, item3, item4, item5):
    # Result adds up all the items and saves it in variable
    result = item1 + item2 + item3 + item4 + item5
    # Return result value
    return result

    # End add_five_values function

#==========================================================================

# Function to calculate total sales tax
def calc_sales_tax(tax, subTotal):
    # Multiply parameters and assign to variable
    salesTax = tax * subTotal
    # Return variable value
    return salesTax

    # End calc_sales_tax function]
    
#==========================================================================

# Function to calculate total sales
def calc_total_sales(subTotal, totalSalesTax):
    # Adds sales tax to subtotal and stores in variable
    sales = totalSalesTax + subTotal
    # Returns variable value
    return sales

    # End calc_total_sales function

#==========================================================================

# Function to print output statement
def print_output(item1, item2, item3, item4, item5, subTotal, totalSalesTax, totalSales, outFile):
    # Lots of parameters/arguments so it will display every variable/value within this function
    outFile.write("=================================================\n")
    outFile.write("TOTAL PURCHASE RECEIPT / INFORMATION\n")
    outFile.write("=================================================\n")
    outFile.write(f"PRICE FOR ITEM # 01:               ${item1:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 02:               ${item2:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 03:               ${item3:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 04:               ${item4:,.2f}\n")
    outFile.write(f"PRICE FOR ITEM # 05:               ${item5:,.2f}\n")
    outFile.write("=================================================\n")
    outFile.write(f"SUB TOTAL     =    ${subTotal:,.2f}\n")
    outFile.write(f"SALES TAX     =    ${totalSalesTax:,.2f}\n")
    outFile.write(f"TOTAL SALES   =    ${totalSales:,.2f}\n")
    outFile.write("=================================================\n")

    # End print_output function

#==========================================================================

# Function to convert feet to inches
def ft_to_inch(feet):
    inches = feet * 12
    return inches

#    End function

#==========================================================================

def find_max_func(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        print('Error deciding larger integer.')
        
    # End function

#==========================================================================

def display_results_max_num(num1, num2, findMax, outFile):
    outFile.write('~' * 50 + '\n')

    outFile.write(f'{"MAXIMUM OF TWO VALUES":^50s}\n')

    outFile.write('~' * 50 + '\n')

    outFile.write(format(f'{"The maximum of "}{int(num1)}{" and "}{int(num2)}{" is "}{int(findMax)}.', "^50s") + '\n')

    outFile.write('~' * 50 + '\n')

    # End function

#==========================================================================

def display_results_feet_inches(ft, inc, file):

    # Display lines
    file.write("~" * 50 + "\n")

    # Centers this text within 50 characters
    file.write(f'{"CONVERTING FEET TO INCHES":^50s}' + "\n")

    file.write("~" * 50 + "\n")

    # Centers this text within 50 characters
    file.write(format(f'{ft:,.2f}{" feet = "}{inc:,.2f}{" inches."}', "^50s") + "\n")

    # Display lines
    file.write("~" * 50 + "\n")

    # End function

#==========================================================================

def draw_Stars():
    # Set range size
    RAND_RANGE = 14
    turtle.penup()
    
    # Use for loop to randomly generate numbers(for the coordinates)
    for coord in range(RAND_RANGE):
        rand_num1 = random.randint(-500, 500)
        rand_num2 = random.randint(100, 350)
        turtle.goto(rand_num1, rand_num2)
        turtle.dot('yellow')

    # End function

#==========================================================================

def setup_Screen():
    # Set turtle speed to 0, color to black, and screen size to 1000px by 800px
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.setup(1000, 800)

    # End function

#==========================================================================

def draw_Building():
    # set pen color to grey
    turtle.pencolor('grey')
    turtle.penup()
    turtle.goto(-500, -400)
    turtle.setheading(90)
    turtle.fillcolor('grey')
    turtle.begin_fill()
    turtle.pendown()

    # set-up
    turtle.forward(100)
    turtle.setheading(0)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    
    # first building
    turtle.forward(100) 
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    
    # second building
    turtle.forward(350)
    turtle.right(90)
    turtle.forward(200) 
    turtle.right(90)
    turtle.forward(350)

    # third building
    turtle.left(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)

    # fourth building
    turtle.left(180)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(150)

    # fifth building
    turtle.left(180)
    turtle.forward(300)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(300)

    # sixth building
    turtle.left(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(145)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()

    # End function

#==========================================================================


def draw_Window():
    # window 1
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-380, -200)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

     # window 2
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-380, -250)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

     # window 3
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-380, -300)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    

    # window 4
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-180, 0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 5
    turtle.penup()
    turtle.goto(-260, 0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 6
    turtle.penup()
    turtle.goto(-70, -150)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 7
    turtle.penup()
    turtle.goto(-70, -200)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 8
    turtle.penup()
    turtle.goto(-70, -250)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 9
    turtle.penup()
    turtle.goto(50, -200)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 10
    turtle.penup()
    turtle.goto(110, -200)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 11
    turtle.penup()
    turtle.goto(170, -200)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 12
    turtle.penup()
    turtle.goto(270, 0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # window 13
    turtle.penup()
    turtle.goto(330, 0)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.begin_fill()
    # For loop to draw windows
    for x in range(4):
        turtle.forward(35)
        turtle.right(90)
    turtle.end_fill()

    # End function

#==========================================================================

# END PROGRAM
