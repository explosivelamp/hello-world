def main():
    x = input("Enter a number or press Enter to quit ")
    guess = float(input("Enter an estimate of the square root "))
    while x != "":
        x = float(x)
        guess = float(guess)
        print(newton(x, guess))
        x = input("Enter a number or press Enter to quit ")
        guess = (input("Enter an estimate of the square root "))
        
def newton(n, guess):
    """Gives the square root of N using Newton's method"""
    
    tol = 0.0001

    while True:
        guess = (guess + n / guess) / 2
        diff = abs(n - guess ** 2)
        if diff <= tol:
            break
        newton(n, guess)
    return guess

if __name__ == "__main__":
    main()
