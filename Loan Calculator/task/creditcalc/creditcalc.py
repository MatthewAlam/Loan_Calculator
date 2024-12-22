import argparse
from math import ceil, log

# Terminal input parser
def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=float)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--type", type=str)

    return parser.parse_args()

# Annuity payment calculations
def annuity_payment(principal, interest, periods):
    annuity = ceil(principal * (interest * (1 + interest) ** periods / ((1 + interest) ** periods - 1)))
    print(f"Your annuity payment = {annuity}!")
    return overpayment(principal, periods * annuity)

# Differentiated payment calculations
def diff_payment(principal, interest, periods):
    total_payment = 0
    for month in range(1, int(periods) + 1):
        difference = ceil(principal / periods + interest * (principal - principal * (month - 1) / periods))
        print(f"Month {month}: payment is {difference}")
        total_payment += difference
    return overpayment(principal, total_payment)

# Number of Payment years and months conversion
def period_of_payments(time):
    years = ceil(time // 12)
    months = ceil(time % 12)
    if years == 0:
        return f"{months} months"
    elif months == 0:
        return f"{years} years"
    else:
        return f"{years} years and {months} months"

# Number of payment calculations
def number_of_payments(principal, payment, interest):
    return ceil(log(payment / (payment - interest * principal)) / log(1 + interest))

# Principal payment calculation
def principal_payment(interest, payment, periods):
    principal = int(payment / ((interest * (1 + interest) ** periods ) / ((1 + interest) ** periods - 1)))
    print(f"Your loan principal = {principal}!")
    return overpayment(principal, periods * payment)

# Nominal interest calculation
def nominal_interest(interest):
    return interest / 12 / 100

# Overpayment calculations
def overpayment(principal, total_payment):
    print(f"Overpayment = {total_payment - principal}")
    return

# Negative check
def is_positive(inputs):
    values = (num for num in inputs if isinstance(num, float))
    for num in values:
        if num < 0:
            return False
    return True

# Main function
def loan(args):
    arg_inputs = [args.payment, args.principal, args.periods, args.interest]
    if args.type in ["annuity", "diff"] and is_positive(arg_inputs) and arg_inputs.count(None) < 2:
            # Interest check error code
            if args.interest is None:
                print("Incorrect parameters")

            # Payment amount
            elif args.payment is None and args.type == "annuity":
                annuity_payment(args.principal, nominal_interest(args.interest), args.periods)
            elif args.payment is None and args.type == "diff":
                diff_payment(args.principal, nominal_interest(args.interest), args.periods)

            # Amount of payments
            elif args.periods is None and args.type == "annuity":
                total_time = number_of_payments(args.principal, args.payment, nominal_interest(args.interest))
                print(f"It will take {period_of_payments(total_time)} payments to repay this loan!")
                overpayment(args.principal, total_time * args.payment)

            # Principal interest
            elif args.principal is None and args.type == "annuity":
                principal_payment((nominal_interest(args.interest)), args.payment, args.periods)

            # Incorrect parameters error code
            else:
                print("Incorrect parameters")
    else:
        # Incorrect parameters error code
        print("Incorrect parameters")

loan(parse_arguments())