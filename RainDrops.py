def getinput():
    return int(input("Enter a number: "))


def calculations():
    usernum = getinput()
    if usernum % 3 == 0:
        if usernum % 3 == 0 and usernum % 5 == 0:
           print("Result: " + str(usernum) + " PlingPlang")

        elif usernum % 3 == 0 and usernum % 5 == 0 and usernum % 7 == 0:
           print("Result: " + str(usernum) + " PlingPlangPong")

        elif usernum % 3 == 0:
            print("Result: " + str(usernum) + " Pling")

    elif usernum % 5 == 0:
        print("Result: " + str(usernum) + " Plang")

    elif usernum % 7 == 0:
        print("Result: " + str(usernum) + " Plong")

    else:
        print("Result: " + str(usernum))






if __name__ == "__main__":
    calculations()


