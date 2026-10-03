def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer value."
    if n<=0:
        return "Argument must be an integer greater than 0."
    list_of_numbers=[]
    for i in range(n):
        list_of_numbers.append(str(n-i))
    return (" ".join(list_of_numbers[::-1]))

