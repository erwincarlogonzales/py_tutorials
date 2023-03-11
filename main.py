# create a simple slot machine
# source: https://www.youtube.com/watch?v=th4OBktqK1I&t=2s

# import modules
import random



# create global constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # check every line in the lines list
    for line in range(lines):

        # check symbol in the first column of the current row
        symbol = columns[0][line]

        # loop through every column and check for that symbol
        for column in columns:

            # the symbol_to_check is at the current row that we are checking
            symbol_to_check = column[line]

            # check if the symbols are different then break out of the loop
            if symbol != symbol_to_check:
                break
            
        # if the user has all the same symbols then he wins
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines




# create a slot machine function
def get_slot_machine_spin(rows, cols, symbols):

    # create a list and return a random number
    all_symbols = []

    # use .items to return a key value pair
    for symbol, symbol_value in symbols.items():
        # use _ as an anonymous variable that way you don't have to care about the iteration value or i++
        for _ in range(symbol_value):
            # take a value from the symbol_value dictionary and add it to the all_symbols list
            all_symbols.append(symbol)

    # create an empty columns list to store the number of values in each row we have
    columns = []

    # for every col we need to generate a certain number of rows
    for _ in range(cols):

        column = []

        # create a copy of all_symbols bec we want to remove the symbols we took from the all_symbols list
        # the [:] avoids makeing changes to the all_symbols list
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            # remove the value we chose to avoid duplicates
            current_symbol.remove(value)

            # take the value and add it to the column list
            column.append(value)
        
        columns.append(column)
    
    return columns



# transpose the rows into columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end= "")
        
        print()



# create a function that takes an input for the starting amoun
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")

        # check if amount is a number
        if amount.isdigit():
            amount = int(amount)

            # is it > 0
            if amount > 0:
                break
         
            else:
                print("Please enter an amount greater than 0.")
        else:
            print("Please enter an amount")

    return amount


# create a bet function that takes an input for the starting amount
def get_number_of_lines():
    while True:
        lines = input("How many lines would you would like to bet on: (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)

            # is it > 0
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a value between 1 - 3.")
        else:
            print("Please enter an number")

    return lines


# create a function that takes the bet of the user
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)

            # is it > 0
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter an amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter an number")

    return amount

# create the game function
def spin(balance):
    lines = get_number_of_lines()

    # check if bet is !> balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to bet that amount. Your currnent balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines}. dollars. Your total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You have won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


# create a function that runs everytime a user wants to play again
def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")

main()
