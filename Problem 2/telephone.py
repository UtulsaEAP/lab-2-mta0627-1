def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    
    area_code = phone_number // 10**7
    prefix = phone_number // 10**4 % 10**3
    line_number = phone_number % 10**4

    print(f'({area_code}) {prefix}-{line_number}')
    
if __name__ == "__main__":
    telephone()