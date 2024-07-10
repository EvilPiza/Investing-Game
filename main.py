import random
import time

print("Welcome to My Generic Investing Game!")
print(" ")
time.sleep(.3)
print("Type 'h' or 'help' to see the controls.")
print(" ")
time.sleep(.3)
print("The difference between Large, Medium, and Small is risk.")
time.sleep(.4)
print("Large can gain the most but can lose the most.")
time.sleep(.4)
print("Small is the safest but makes less from gains.")
time.sleep(.4)
print("Medium is right in the middle.")
time.sleep(.5)
print(" ")
print(" ")

inp = ""
l_shares = 0
m_shares = 0
s_shares = 0
l_rate = 50
m_rate = 25
s_rate = 10
starting_money = 5000


def start_game():
    global inp
    global l_shares, m_shares, s_shares, l_rate, m_rate, s_rate, starting_money

    inp = str(input("Action: "))
    inp = inp.lower()

    if inp == "help" or inp == "h":
        print("h is for help")
        print("p or portfolio to see your networth and your portfolio")
        print("buy, purchase, or b to purchase shares")
        print("s or sell to sell shares")
        print("l or large to select large when handling shares")
        print("m or medium to select medium shares when handling shares")
        print("s or small to select small shares when handling shares")
        print("When in the action menu, 'm' or 'money' to check how much money you have")
        start_game()

    if inp == "portfolio" or inp == "p":
        print(" ")
        print("Large Shares: " + str(l_shares) + "x Worth $" + str(l_shares * l_rate))
        print("Medium Shares: " + str(m_shares) + "x Worth $" + str(m_shares * m_rate))
        print("Small Shares: " + str(s_shares) + "x Worth $" + str(s_shares * s_rate))
        print("Your total net worth is $" + str((l_shares * l_rate) + (m_shares * m_rate) + (s_shares * s_rate)))
        print(" ")
        start_game()

    if inp == "buy" or inp == "purchase" or inp == "b":

        print(" ")
        print("Large Shares cost $" + str(l_rate))
        print("Medium Shares cost $" + str(m_rate))
        print("Small Shares cost $" + str(s_rate))
        print(" ")
        inp = str(input("Which type of share would you like to purchase? "))

        if inp == "small" or inp == "s":
            inp = int(input("How many would you like to purchase? "))

            if inp * s_rate <= starting_money:
                print("Purchase Successful")
                starting_money = starting_money - (inp * s_rate)
                s_shares = s_shares + inp
                print("You now have " + str(s_shares) + " Small Shares")
                start_game()

            elif inp * s_rate > starting_money:
                print("Purchase Failed")
                start_game()

        elif inp == "medium" or inp == "m":
            inp = int(input("How many would you like to purchase? "))

            if inp * m_rate <= starting_money:
                print("Purchase Successful")
                starting_money = starting_money - (inp * m_rate)
                m_shares = m_shares + inp
                print("You now have " + str(m_shares) + " Medium Shares")
                start_game()

            elif inp * m_rate > starting_money:
                print("Purchase Failed")
                start_game()

        elif inp == "large" or inp == "l":
            inp = int(input("How many would you like to purchase? "))

            if inp * l_rate <= starting_money:
                print("Purchase Successful")
                starting_money = starting_money - (inp * l_rate)
                l_shares = l_shares + inp
                print("You now have " + str(l_shares) + " Large Shares")
                start_game()

        else:
            print("Unknown command, try again")
            start_game()

    if inp == "money" or inp == "m":
        print(" ")
        print("You have $" + str(int(starting_money)))
        print(" ")
        start_game()

    if inp == "change" or inp == "rate" or inp == "cr" or inp == "c" or inp == "r":
        rate_change()

    if inp == "sell" or inp == "s":

        inp = str(input("Which type of share would you like to sell? "))

        if inp == "small" or inp == "s":

            print("You have " + str(s_shares) + " Worth $" + str(int(s_shares * s_rate)) + " Or $" + str(
                int(s_rate)) + " Per Share")

            inp = int(input("How many would you like to sell? "))

            if inp <= s_shares:

                print("Success!")
                s_shares = s_shares - inp
                starting_money = starting_money + (inp * s_rate)
                print("You Sold " + str(inp) + " Shares, and got $" + str(inp * s_rate))
                start_game()

            elif inp > s_shares:

                print("Transaction Failed")
                start_game()

        else:

            print("Unknown command, try again")
            start_game()   

        if inp == "medium" or inp == "m":

            print("You have " + str(m_shares) + " Worth $" + str(int(m_shares * m_rate)) + " Or $" + str(
                int(m_rate)) + " Per Share")

            inp = int(input("How many would you like to sell? "))

            if inp <= m_shares:

                print("Success!")
                m_shares = m_shares - inp
                starting_money = starting_money + (inp * m_rate)
                print("You Sold " + str(inp) + " Shares, and got $" + str(inp * m_rate))
                start_game()

            elif inp > m_shares:

                print("Transaction Failed")
                start_game()

        else:

            print("Unknown command, try again")
            start_game()

        if inp == "large" or inp == "l":

            print("You have " + str(l_shares) + " Worth $" + str(int(l_shares * l_rate)) + " Or $" + str(
                int(l_rate)) + " Per Share")

            inp = int(input("How many would you like to sell? "))

            if inp <= l_shares:

                print("Success!")
                l_shares = l_shares - inp
                starting_money = starting_money + (inp * l_rate)
                print("You Sold " + str(inp) + " Shares, and got $" + str(inp * l_rate))
                start_game()

            elif inp > l_shares:

                print("Transaction Failed")
                start_game()
        else:

            print("Unknown command, try again")
            start_game()

    else:

        print("Unknown command, try again")
        start_game()


def rate_change():
    print(" ")

    global l_rate, m_rate, s_rate

    l_rate = random.randint(57, 150)

    m_rate = random.randint(80, 125)

    s_rate = random.randint(92, 110)


    if l_rate > 100:
        print("Large Shares went up by " + str(l_rate - 100) + "%")

    if m_rate > 100:
        print("Medium Shares went up by " + str(m_rate - 100) + "%")

    if s_rate > 100:

        print("Small Shares went up by " + str(s_rate - 100) + "%")

    elif l_rate == 100:

        print("Large Shares didn't change")

    elif m_rate == 100:

        print("Medium Shares didn't change")

    elif s_rate == 100:

        print("Small Shares didn't change")

    if l_rate < 100:
        print("Large Shares went down by " + str(100 - l_rate) + "%")

    if m_rate < 100:
        print("Medium Shares went down by " + str(100 - m_rate) + "%")

    if s_rate < 100:
        print("Small Shares went down by " + str(100 - s_rate) + "%")

    print(" ")

    start_game()


if __name__ == '__main__':
    start_game()


# well, its official. I'm a noob at python.
