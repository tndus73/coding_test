product_name, product_code = input().split()
product_code = int(product_code)

class product():
    def __init__(self, name, code):
        self.name = name
        self.code = code

P = product('codetree', '50')
print(f'product {P.code} is {P.name}')
P = product(product_name, product_code)
print(f'product {P.code} is {P.name}')

# Please write your code here.