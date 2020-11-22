sum = 0.0
count = 0
data = input("Enter a number, or hit enter to stop entering: ")
while data != "":
    number = float(data)
    sum += number
    count += 1
    avg = sum / count
    data = input("Enter a number, or hit enter to stop entering: ")
print("The sum is", sum)
print("The average is", avg)
