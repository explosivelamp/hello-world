def main():
    x = input("Enter a number or press Enter to quit ")
    while x != "":
        x = float(x)
        print(newton(x))
        x = input("Enter a number or press Enter to quit ")
        
def newton(n):
    """Gives the square root of N using Newton's method"""
    
    tol = 0.000000001
    guess = 1.0

    while True:
        guess = (guess + n / guess) / 2
        diff = abs(n - guess ** 2)
        if diff <= tol:
            break
    return guess

if __name__ == "__main__":
    main()
