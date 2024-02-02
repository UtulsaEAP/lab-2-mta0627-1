
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    
    change_in_price = current_price - last_month_price
    estimated_monthly_mortgage = (current_price * 0.051) / 12

    print(f'This house is ${current_price:.0f}. The change is ${change_in_price:.0f} since last month.')
    print(f'The estimated monthly mortgage is ${estimated_monthly_mortgage:.2f}.')

if __name__ == "__main__":
    real_estate()