payrate = float(input("Enter hourly pay rate: "))
hours = float(input("Enter non-overtime hours: "))
overtime = float(input("Enter overtime hours: "))
WeeklyPay = ((overtime * 1.5) + hours) * payrate
print("Total pay for the week is ", str(WeeklyPay))
