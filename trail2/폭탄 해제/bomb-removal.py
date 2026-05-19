unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class pop:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

popT = pop(unlock_code, wire_color, seconds)

print(f'code : {popT.unlock_code}')
print(f'color : {popT.wire_color}')
print(f'second : {popT.seconds}')
