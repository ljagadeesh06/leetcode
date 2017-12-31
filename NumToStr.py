def convert(num):
    print(num)
    if num <= 0:
        return
    rem = num % 1000
    print(rem)
    convert(int(num/1000))


convert(2787)