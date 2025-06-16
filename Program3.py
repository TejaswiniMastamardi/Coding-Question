def Print_series(a):
    if a%2 == 0:
        a = a-1
    for i in range(a):
        print(2*i +1)



num=int(input("Enter a number : "))
Print_series(num)
    