def square_root_bisection(number,tolerance=0.1,max_iteration=50):
    if number<0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number==1 or number==0:
        print(f"The square root of {number} is {number}")
        return number
    else:
        low=0
        high=number
        for _ in range(max_iteration):
            mid=(low+high)/2
            if high-low<=tolerance:
                print(f"The sqare root of {number} is approximately {mid}")
                return mid
            elif mid**2>number:
                high=mid
            else:
                low=mid


# print(square_root_bisection(9))
print(square_root_bisection(0.001, 1e-7, 50) )
        
