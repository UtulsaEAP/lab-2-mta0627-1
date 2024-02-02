
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    
    caffeine_level_after_6_hrs = caffeine_mg / 2
    caffeine_level_after_12_hrs = caffeine_mg / 4
    caffeine_level_after_24_hrs = caffeine_mg / 16

    print(f'After 6 hours: {caffeine_level_after_6_hrs:.2f} mg')
    print(f'After 12 hours: {caffeine_level_after_12_hrs:.2f} mg')
    print(f'After 24 hours: {caffeine_level_after_24_hrs:.2f} mg')

if __name__ == "__main__":
    caffeine()