def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if str is None or len(str.strip()) == 0:
        return 0
    str = str.strip()
    num = 0
    sign = 1
    start = 0
    if str[0] == '+':
        sign = 1
        start = 1
    if str[0] == '-':
        sign = -1
        start = 1
    for item in str[start:]:
        if item.isdigit():
            num *= 10
            num += int(item)
        else:
            break
    if sign == 1:
        return min(num, 2 ** 31 - 1)
    else:
        return max(num * sign, 2 ** 31 * sign + 1)


print(2 ** 31 - 1)
print(myAtoi("-214748364as;as"))

