def add(num_one, num_two):
    return num_one + num_two
    
def divide(num_one, num_two):
    if num_two == 0:
        raise ValueError("Division by zero is not allowed.")
    return num_one/num_two