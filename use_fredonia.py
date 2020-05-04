from fredonia import calculate_tax

price = input('Enter price: ')
province = input('Enter province: ')
time = int(input('Enter hour or purchase: '))

print(f'Purchase costs {calculate_tax(price, province, time):.2f} including taxes')
