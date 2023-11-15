"""demonstrating functions"""
def my_max(number: int, number2: int) -> int:
    """Returns the maximum value"""
    if number >= number2:
        return number
    else: #number < number 2
        return number2
    
    
    
    

max_num: int = my_max(1,10)

other_max: int = my_max(10,3)
print(other_max)