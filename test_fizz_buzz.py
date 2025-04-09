from main import fizz_buzz

def test_fizz():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(9) == "Fizz"

def test_buzz():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(20) == "Buzz"

def test_fizzbuzz():
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"

def test_othernumbers():
    assert fizz_buzz(4) == 4
    assert fizz_buzz(8) == 8
    assert fizz_buzz(11) == 11

def test_notequals():
    assert fizz_buzz(1) != "Fizz"
    assert fizz_buzz(2) != "Buzz"
    assert fizz_buzz(7) != "FizzBuzz"