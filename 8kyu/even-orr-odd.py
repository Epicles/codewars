# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


# My solutions
def even_or_odd(number):
    answ = "Even" if number % 2 == 0 else 'Odd'
    return answ