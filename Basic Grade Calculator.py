def main():
    global b, c, p, d
    print("Please type your Quiz score: ")
    a = input()
    while a.isnumeric() == False or int(a) >= 101:
        print("You made a mistake! Please try again.")
        a = input()

    if a.isnumeric() == True or int(a) <= 101:
        print("Please type your Lab Activities score: ")

        b = input()
    while b.isnumeric() == False or int(b) >= 101:
        print("You made a mistake! Please try again.")
        b = input()
    if b.isnumeric() == True or int(b) <= 101:
        print("Please type your Assignment score: ")
        c = input()
    while c.isnumeric() == False or int(c) >= 101:
        print("You made a mistake! Please try again.")
        c = input()
    if c.isnumeric() == True or int(c) <= 101:
        print("Please type your Midterm score: ")
        d = input()
    while d.isnumeric() == False or int(d) >= 101:
        print("You made a mistake! Please try again.")
        d = input()
    if d.isnumeric() == True or int(d) <= 101:
        print("Please type your Final score: ")

        e = input()
        p = (int(a) * 10 / 100 + int(b) * 10 / 100 + int(c) * 20 / 100 + int(d) * 20 / 100 + int(e) * 40 / 100)

    if 90 <= p <= 100:
        print("Congratulations! You passed this lecture with AA." " " + "Your score is" " " + str(p))
        exit()
    elif 85 <= p <= 89:
        print("Congratulations! You passed this lecture with BA." " " + "Your score is" " " + str(p))
        exit()
    elif 80 <= p <= 84:
        print("Congratulations! You passed this lecture with BB." " " + "Your score is" " " + str(p))
        exit()
    elif 75 <= p <= 79:
        print("Congratulations! You passed this lecture with CB." " " + "Your score is" " " + str(p))
        exit()
    elif 70 <= p <= 74:
        print("Congratulations! You passed this lecture with CC." " " + "Your score is" " " + str(p))
        exit()
    elif 60 <= p <= 69:
        print("Congratulations! You passed this lecture with DC." " " + "Your score is" " " + str(p))
        exit()
    elif 50 <= p <= 59:
        print("Congratulations! You passed this lecture with DD." " " + "Your score is" " " + str(p))
        exit()
    elif 50 >= p >= 0:
        print("Sorry to say this but you failed this lecture with FF." " " + "Your score is" " " + str(p))
        exit()
    elif p <= 0:
        print("Please type a relevant number!")
        p = input()
    elif p >= 101:
        print("Please type a relevant number!")
        p = input()


main()
