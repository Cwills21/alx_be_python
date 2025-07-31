def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        Answer = num/den
        print(f'{num} divided by  {num} is equal to {Answer}')
        return f'Result: {Answer}'
    
    except ZeroDivisionError:
        print('sorry cannot divide by zero')
    except ValueError:
        print('sorry cannnot divide by a non mumber')

