import math

def pizza(d, price):
    r = d / 100 / 2
    area = math.pi * r ** 2
    unit_price = price / area

    return unit_price

def cheap_pizza(p1, p2):

    if p1 < p2:
        return 1, p2 - p1
    else:
        return 2, p1 - p2

d1, price1 = input("\nEnter diameter/cm for pizza 1: "), input("\nEnter price: ")
d2, price2 = input("\nEnter diameter/cm for pizza 2: "), input("\nEnter price: ")

pizza1 = pizza(int(d1), int(price1))
pizza2 = pizza(int(d2), int(price2))

res = cheap_pizza(pizza1, pizza2)

print(f"\nThe cheapest pizza is: pizza number {res[0]} with pirse difference {res[1]:.2f}€")