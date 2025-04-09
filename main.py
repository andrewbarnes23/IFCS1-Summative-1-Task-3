def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return str("FizzBuzz")
    elif num % 5 == 0:
        return str("Buzz")
    elif num % 3 == 0:
        return str("Fizz")
    else:
        return num