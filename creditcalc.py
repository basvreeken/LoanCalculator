import math

# Prompt user for principal and type of calculation
principal = int(input('Enter the load principal: '))
calc_type = input('What do you want to calculate?\ntype "m" - for the '
                  'monthly payments,\ntype "p" for the monthly payment: ')

# Calculate the number of monthly payments
if calc_type == 'm':
    monthly_payment = int(input('Enter the monthly payment: '))
    months = math.ceil(principal / monthly_payment)
    print(f'It will take {months} month to repay the loan' if months == 1
          else f'It will take {months} months to repay the loan')

# Calculate the amount of monthly payments
if calc_type == 'p':
    months = int(input('Enter the number of months: '))
    monthly_payment = math.ceil(principal / months)
    last_payment = principal - ((months - 1) * monthly_payment)
    print(f'Your monthly payment = {monthly_payment} and the last payment = '
          f'{last_payment}')


