def main():
    x = input("Enter a number or press Enter to quit ")
    guess =(input("Enter an estimate of the square root "))
    while x != "":
        x = float(x)
        
        print(newton(x, guess))
        x = input("Enter a number or press Enter to quit ")
        guess = (input("Enter an estimate of the square root "))
        
def newton(n, guess):
    """Gives the square root of N using Newton's method"""
#if no input is given for guess, a guess of 1 is assumed#
    if guess == "":
        guess = 1.0
       
    tol = 0.0001
    guess = float(guess)
    
    while True:
        guess = (guess + n / guess) / 2
        diff = abs(n - guess ** 2)
        if diff <= tol:
            break
        newton(n, guess)
    return guess

if __name__ == "__main__":
    main()
