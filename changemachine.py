"""
Purpose of program is to take in a total cost of itmes, a total dollar amount given to
"""

#Reference dictionaries and lists
#Dictinoaries offers english to value translation.  Lists are ordered list of values.
#Coin versions are value * 100 to avoid rounding fuckery
coindict = {"quarters":25, "dimes":10,"nickels":5, "pennies":1}
coinlist = ["quarters","dimes","nickels","pennies"]
dollarlist = ["twenties","tens", "fives","ones"]
dollardict = {"twenties":20,"tens":10,"fives":5,"ones":1}


#old attempt at minimizing coins, using too many loops etc.
def oldminimizecoins(remainder):
    changetotal = remainder
    remainder = 100 * remainder
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while remainder > 0:
        if remainder > 100:
            break
        elif remainder > 25:
            quarters = int(remainder // 25)
            remainder = remainder % 25
            print(remainder)
        elif remainder > 10:
            dimes = int(remainder // 10)
            remainder = remainder % 10
            print(remainder)
        elif remainder > 5:
            nickels = int(remainder // 5)
            remainder = remainder % 5
            print(remainder)
        else:
            pennies = int(remainder // 1)
            remainder = 0
            print(remainder)
    return("Coins totaling:",changetotal, quarters, " quarters, ", dimes, " dimes," , nickels, " nickels, " , pennies, " pennies." )


#Minimizes coins, returns list of # of coins given in change if given an original valid number
#Can compute with values > $1.00 but not supposed to.
def minimizecoins(cents):
    if cents < 0:
        raise ValueError("Cents must be greater than zero")
    #if cents > 1.00:
        #cents = cents % 1.00
    remainder = cents * 100
    coins = []
    for coin in coinlist:
        coins.append(int(remainder// coindict[coin]))
        remainder = remainder % coindict[coin]
    return coins

#retrun two things
#(thing1, thing2) = minimizecoins(change)
#Minimizes Dollars, calls minimize coins function as well.
def minimizedollars(dollars):
    remainderd = dollars
    dollarcounts = []
    for bill in dollarlist:
        dollarcounts.append(int(remainderd//dollardict[bill]))
        remainderd = remainderd % dollardict[bill]
    return dollarcounts


def format_coins(cents, coins):
    statement1 = "Change is $ %s" % str(cents)
    coins1 = tuple(coins)
    statement2 = "Here is %s quarters, %s dimes, %s nickels and %s pennies " % coins1
    return(statement1, statement2)

def run_it():
    #INPUT SECTION.
    while True:
        try:
            total =float(input("Please enter Total: "))
            paid = float(input("How much will the customer pay?: "))
        except:
            print("Please try again, values not valid.")

        change = paid - total

        if change < 0:
            print("Not enough payment.")
        elif change == 0:
            print("Thank you this is exactly the right amount")
        else:
            print(minimizecoins(change))

"""
Input Rewrite
Run_it()

check for invalid input. Ensure numbers can be floats - can be function

add error testing to each specific function. ie negatives

function to actually make change
    within func, have test for if need dollars and cents or just cents

add function to make final statements. Consider adding functionality if change needed to bew more than $1


"""

if __name__ == __file__:
    run_it()

##TESTING OUT FUNCTIONS##


#print(minimizecoins(1.85))

#print(minimizedollars(1.65))

print(format_coins(200, [8, 2, 0, 2]))

