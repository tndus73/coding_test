product_name, product_code = input().split()
product_code = int(product_code)

class product():
    def __init__(self, name, code):
        self.name = name
        self.code = code

P1 = product('codetree', '50')
P2 = product(product_name, product_code)
print(f'product {P1.code} is {P1.name}')
print(f'product {P2.code} is {P2.name}')

# Please write your code here.