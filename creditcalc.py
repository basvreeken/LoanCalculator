import math

# Prompt user for type of calculation
calc_type = input('What do you want to calculate?\ntype "n" - for the '
                  'monthly payments,\ntype "a" for annuity monthly payment '
                  'amount,\ntype "p" for loan principal: ')

# Calculate the number of monthly payments
if calc_type == 'n':
    principal = int(input('Enter the loan principal: '))
    monthly_payment = int(input('Enter the monthly payment: '))
    loan_interest = float(input('Enter the loan interest: '))
    nominal_interest_rate = loan_interest / (12 * 100)
    months = math.ceil(math.log(monthly_payment / (monthly_payment -
                                                   nominal_interest_rate *
                                                   principal),
                                1 + nominal_interest_rate))

    years = math.floor(months / 12)
    rest_months = months % 12

    # Only months
    if years < 1:
        print(f'It will take {rest_months} month to repay the loan' if
              rest_months == 1
              else f'It will take {rest_months} months to repay the loan')

    # Only years
    elif months % 12 == 0:
        print(f'It will take {years} year to repay the loan' if years == 1
              else f'It will take {years} years to repay the loan')

    # 1 years and months
    elif 12 < months < 24:
        print(f'It will take {years} year and {rest_months} month to repay '
              f'the loan' if rest_months == 1 else f'It will take {years} '
                                                   f'years and {rest_months} '
                                                   f'months to repay the loan')
    else:
        print(f'It will take {years} years and {rest_months} month to repay '
              f'the loan' if rest_months == 1 else f'It will take {years} '
                                                   f'years and {rest_months} '
                                                   f'months to repay the loan')

# Calculate the annuity monthly payment amount
if calc_type == 'a':
    principal = int(input('Enter the loan principal: '))
    periods = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))
    nominal_interest_rate = loan_interest / (12 * 100)
    factor = (nominal_interest_rate * math.pow((1 + nominal_interest_rate),
                                               periods)) / \
             (math.pow((1 + nominal_interest_rate), periods) - 1)
    ordinary_annuity = math.ceil(principal * factor)
    print(f'Your monthly payment = {ordinary_annuity}!')

# Calculate the amount of monthly payments
if calc_type == 'p':
    annuity_payment = float(input('Enter the annuity payment'))
    periods = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))
    nominal_interest_rate = loan_interest / (12 * 100)
    factor = (nominal_interest_rate * math.pow((1 + nominal_interest_rate),
                                               periods)) / \
             (math.pow((1 + nominal_interest_rate), periods) - 1)

    loan_principal = int(annuity_payment / factor)
    print(f'Your loan principal = {loan_principal}!')
