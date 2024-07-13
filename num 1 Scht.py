def skobochki(stroki):
    proverka = []
    for char in stroki:
        if char in matches.values():
            proverka.append(char)
        elif char in matches:
            if not proverka or proverka.pop() != matches[char]:
                return False
    return len(proverka) == 0


slovarik = []
matches = {')': '(', '}': '{', '>': '<', ']': '['}
try:
    with open('input.txt', 'r') as file:
        for lines in file:
            chist = lines.strip()
            slovarik.append(chist)
except FileNotFoundError:
    print("файл не найден")
print(slovarik)
truee = []
falsee = []
for stroki in slovarik:
    if skobochki(stroki):
        truee.append(stroki)
    else:
        falsee.append(stroki)
print("True", truee)
print("False", falsee)
with open('output.txt', 'w') as file:
    for i in truee:
        file.write(f"{i} True\n")
    for i in falsee:
        file.write(f"{i} False\n")