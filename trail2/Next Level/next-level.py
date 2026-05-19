user2_id, user2_level = input().split()
user2_level = int(user2_level)

class idlevel:
    def __init__(self, id='codetree', level=10):
        self.id = id
        self.level = level

idl1 = idlevel()
idl2 = idlevel(user2_id, user2_level)

print(f'user {idl1.id} lv {idl1.level}')
print(f'user {idl2.id} lv {idl2.level}')
# Please write your code here.
