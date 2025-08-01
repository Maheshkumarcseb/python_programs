letter = "hey my name is {} and i am from {}"
country="india"
name = "aman"
print(letter.format(name,country))
price = 100
print(f"hey my name is {{name}} and i am from {country}")
print(f"price is {price:.2f} rupees")

print(f"{2*40}")
print(type(f"{2*40}")) 

print(" GETTING STARTED WITH DOCSTRING")

def square(num):
    # print("hi")   // this will not allow to print docstring
    """
    This function returns the square of a number.
    
    Parameters:
    num (int or float): The number to be squared.
    
    Returns:
    int or float: The square of the input number.
    """
    return num * num
print(square(5))
print(square.__doc__)



# import this ---> the zen of pytho, by tim peters