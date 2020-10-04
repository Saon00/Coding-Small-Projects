# Saon Srabon
# 08:20 PM
# 28 July 2020
# Dhaka,Bangladesh
# Python3
# Watch this video to use this program nicely: https://www.linkedin.com/posts/saon-sikder_pythonprogramming-activity-6693743246700634112-Qf-7


def womens_dress():
    print("""                   Women's Collections
1. Salwar Kameez  1600 Taka     2. Saree  4500 Taka
3. One Piece  1000 Taka         4. Four Piece  25000 Taka
5. Gown  6000 Taka              6. Lehenga  15000 Taka
7. Tops  850 Taka               8. Skirt  500 Taka
9. Kurta  850 Taka              10. Jeans Pant  900 Taka
11. T-Shirt  450 Taka           12. Ladies Shirt  1400 Taka
    """)


def womens_dress_price(taka):
    dic = {'1': '1600', '2': '4500', '3': '1000', '4': '2500', '5': '6000', '6': '15000',
           '7': '850', '8': '500', '9': '850', '10': '900', '11': '450', '12': '1400'}
    return dic[f'{taka}']


def mens_dress():
    print("""                    Men's Collections
1. Punjabi  1600 Taka           2. Pajama  600 Taka
3. Dhoti Pajama  500 Taka       4. Lungi  400 Taka
5. Half Pant  300 Taka          6. Kurta  1500 Taka
7. Blazer  9000 Taka            8. Jeans Pant  2100 Taka
9. Jacket  1800 Taka            10. Trousers  500 Taka  
11. T-Shirt  350 Taka           12. Shirt  1350 Taka
    """)


def mens_dress_price(taka):
    dic = {'1': '1600', '2': '600', '3': '500', '4': '400', '5': '300', '6': '1500',
           '7': '9000', '8': '2100', '9': '1800', '10': '500', '11': '350', '12': '1350'}
    return dic[f'{taka}']


items_price = []
qua = []
print("Welcome to Eid Bazar\nWhich Section you want to Visit")
morf = input('>> Male or Female ').lower()  # morf = male or female

# activities for male
if morf == 'male':
    print('\nChoose Your Items by Serial Number')
    mens_dress()
    while True:
        yorn = input("Proceed to buy Y / N : ").lower()
        if yorn == 'n':
            break
        elif yorn == 'y':
            product, quantity = map(int, input('Type Product Serial and Quantity: ').split())
            qua.append(quantity)
            price = mens_dress_price(product)
            sub_price = int(price) * quantity
            items_price.append(sub_price)

# activities for female
elif morf == 'female':
    print('\nChoose Your Items by Serial Number')
    womens_dress()
    while True:
        yorn = input("Proceed to buy Y / N : ").lower()
        if yorn == 'n':
            break
        elif yorn == 'y':
            product, quantity = map(int, input('Type Product Serial and Quantity: ').split())
            qua.append(quantity)
            price = womens_dress_price(product)
            sub_price = int(price) * quantity
            items_price.append(sub_price)

else:
    print("Invalid Keyword. Start again")
    
 
sum_item_price = sum(items_price)
print("\nYour Total Cost is:", sum_item_price, 'Taka')  # Taka is Bangladeshi Currency
print("\n--------- This part is Only for Authority -------------")

discount = input("How much Discount you want to Provide: ")
# initial_vat = input("Govt. Vat: ")   # use this if you want to change VAT every-time
vat = sum_item_price * 0.05  # VAT 5%
discount_price = int(sum_item_price) * float(discount)
after_discount_price = int(sum_item_price) - float(discount_price)
subtotal = (float(after_discount_price) + float(vat))

# print("Total products:",sum(qua))
customer_name = input("Customer Name: ")
print(f'''
--------------------------------------------------
Subtotal Without VAT:               {sum_item_price} Taka
{float(discount) * 100}% Discount on Product(s):       {discount_price} Taka
---------------------------------------------------
Total:                              {sum_item_price - discount_price} Taka
5% VAT on {sum(qua)} Product(s):             {vat} Taka
---------------------------------------------------
CASH:                               {subtotal} Taka
''')
print(f"Thanks For Shopping {customer_name}. Will Buy Again.\nHappy EID MUBARAK....")
