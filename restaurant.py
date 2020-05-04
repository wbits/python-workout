menu = {
    'sandwich': 10,
    'tea': 7,
    'coffee': 8
}

total = 0
order = input('Please order: ').strip()

while True:
    if not order:
        break
    elif order in menu.keys():
        costs = menu.get(order)
        total += costs
        print(f'{order} costs {costs}, total is {total}')
        order = input('Please order: ').strip()
    else:
        print(f'Sorry, we are fresh out of {order} today')
        order = input('Please order: ').strip()

print(f'Your total is {total}')
