import argparse
import math

valid_choices = ['annuity', 'diff']
error_message = 'Incorrect parameters'

# Setup the argument parser to accept user input from the command line
parser = argparse.ArgumentParser(description='This program helps you with '
                                             'loan calculations.')
parser.add_argument('-t', '--type', choices=valid_choices,
                    help='Choose between annuity or differentiated payments.')
parser.add_argument('--principal', help='The loan principal.')
parser.add_argument('--periods', help='The number of periods to pay.')
parser.add_argument('--interest', help='The interest rate for the loan.')
parser.add_argument('--payment', help='The amount to pay per period.')

args = parser.parse_args()

if args.type == 'annuity':
    # Calculate the number of monthly payments
    if args.periods is None:
        if args.principal is None or args.payment is None or args.interest is \
                None:
            print(error_message)
        else:
            principal = float(args.principal)
            monthly_payment = float(args.payment)
            loan_interest = float(args.interest)
            nominal_interest_rate = loan_interest / (12 * 100)
            months = math.ceil(math.log(monthly_payment /
                                        (monthly_payment -
                                         nominal_interest_rate * principal),
                                        1 + nominal_interest_rate))

            years = math.floor(months / 12)
            rest_months = months % 12

            # Only months
            if years < 1:
                print(f'It will take {rest_months} month to repay the loan' if
                      rest_months == 1
                      else f'It will take {rest_months} months to repay the '
                           f'loan')

                # Only years
            elif months % 12 == 0:
                print(
                    f'It will take {years} year to repay the loan'
                    if years == 1
                    else f'It will take {years} years to repay the loan')

            # 1 years and months
            elif 12 < months < 24:
                print(
                    f'It will take {years} year and {rest_months} month to '
                    f'repay '
                    f'the loan' if rest_months == 1 else
                    f'It will take {years} years and {rest_months} '
                    f'months to repay the loan')
            else:
                print(
                    f'It will take {years} years and {rest_months} month to '
                    f'repay the loan' if rest_months == 1 else
                    f'It will take {years} years and {rest_months} months to '
                    f'repay the loan')
            print('Overpayment = ' + str(round(monthly_payment * months -
                                               principal)))

    # Calculate the annuity monthly payment amount
    if args.payment is None:
        if args.principal is None or args.periods is None or args.interest is \
                None:
            print(error_message)
        else:
            principal = float(args.principal)
            periods = float(args.periods)
            loan_interest = float(args.interest)
            nominal_interest_rate = loan_interest / (12 * 100)
            factor = (nominal_interest_rate * math.pow(
                (1 + nominal_interest_rate),
                periods)) / (math.pow((1 + nominal_interest_rate), periods)
                             - 1)
            ordinary_annuity = math.ceil(principal * factor)
            print(f'Your monthly payment = {ordinary_annuity}!')
            print('Overpayment = ' + str(round(ordinary_annuity * periods -
                                               principal)))

    # Calculate the loan principal
    if args.principal is None:
        if args.payment is None or args.periods is None or args.interest is \
                None:
            print(error_message)
        else:
            annuity_payment = float(args.payment)
            periods = float(args.periods)
            loan_interest = float(args.interest)
            nominal_interest_rate = loan_interest / (12 * 100)
            factor = (nominal_interest_rate * math.pow(
                (1 + nominal_interest_rate),
                periods)) / (math.pow((1 + nominal_interest_rate), periods)
                             - 1)

            loan_principal = int(annuity_payment / factor)
            print(f'Your loan principal = {loan_principal}!')
            print('Overpayment = ' + str(round(annuity_payment * periods -
                                               loan_principal)))
elif args.type == 'diff':
    # Calculate the monthly differentiated payment
    if args.principal is None or args.periods is None or args.interest is \
            None:
        print(error_message)
    else:
        P = float(args.principal)  # the loan principal
        n = float(args.periods)  # number of payments
        i = float(args.interest) / (12 * 100)  # nominal interest rate
        total_payment = 0
        m = 1  # current repayment month
        while m < n + 1:
            Dm = int(math.ceil(P / n + i * (P - (P * (m - 1) / n))))  # mth
            # differentiated payment
            print(f'Month {m}: payment is {Dm}')
            total_payment += Dm
            m += 1
        print('Overpayment = ' + str(round(total_payment - P)))

else:
    print(error_message)
