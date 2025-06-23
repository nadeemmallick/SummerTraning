def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    return round(amount, 2)

try:
    p = float(input("Enter principal amount ($): "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time (years): "))
    n = int(input("Enter number of times interest is compounded per year: "))

    total = calculate_compound_interest(p, r, t, n)
    print(f"Total amount after interest: ₹{total}")

except ValueError:
    print("Please enter valid numeric values.")