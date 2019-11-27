from csv_utils import sum_of_all_goods, most_expensive, cheapest, reducing_products_amount, csv_read

a = sum_of_all_goods('/home/valid/Projects/git/tms-21/cw10_task08/f.csv')
print(f'Sum of all goods is {a}')

a = most_expensive('/home/valid/Projects/git/tms-21/cw10_task08/f.csv')
print(f'Most expensive product is {a}')

a = cheapest('/home/valid/Projects/git/tms-21/cw10_task08/f.csv')
print(f'Cheapest product is {a}')

a = reducing_products_amount('/home/valid/Projects/git/tms-21/cw10_task08/f.csv', 1, 1)
csv_read('/home/valid/Projects/git/tms-21/cw10_task08/f.csv')