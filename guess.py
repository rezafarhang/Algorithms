low = 1
high = 1000
turns = 10

while turns > 0:
    guess = int((high - low)/ 2 + low)
    print(guess)
    guess_ans = input()
    if guess_ans == "lower":
        high = guess - 1
        if low > high:
            low, high = high, low
        turns -= 1
    elif guess_ans == "higher":
        low = guess + 1
        if low > high:
            low, high = high, low
        turns -= 1
    else:
        turns = 0