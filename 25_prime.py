def prime_number(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
    if flag == False:
        print("Not a prime")
    else:
        print("Prime number")


n = int(input("Check this number: "))
prime_number(number=n)
