unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class pop:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

popT = pop('branch', 'G', 34)

print(f'code : {unlock_code}')
print(f'color : {wire_color}')
print(f'second : {seconds}')
