import math

# display the menu of options
menu = """investment - to calculate the amount of intrest you'll earn on an investment
bond        -to calculate the amount you'll have to pay on a home loan."""
print(menu)

# ask the user to choose either 'investment' or 'bond' from the menu
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()

# investment option with simple and compound interest
if choice == "investment":
    deposit = float(input("Enter the amount you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))
    interest = input("Enter the type of interest (simple or compound): ").lower().strip()
    
    # calculate simple or compound interest
    if interest == "simple":
        total_amount = deposit * (1 + rate * years)
        print(f"The total amount after {years} years is: {total_amount:.2f}")

    elif interest == "compound":
        total_amount = deposit * math.pow((1 + rate), years)
        print(f"The total amount after {years} years is: {total_amount:.2f}")

    else:
        print("Invalid interest type selected.")

# bond option to calculate monthly repayments
elif choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100 / 12
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    repayment = (annual_rate * present_value) / (1 - math.pow((1 + annual_rate), -months))
    print(f"The monthly repayment amount is: {repayment:.2f}")
    
else:
    print("Invalid option selected. Please choose either 'investment' or 'bond'.")
    








