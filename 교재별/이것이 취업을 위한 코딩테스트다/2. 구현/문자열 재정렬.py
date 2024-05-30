S = input()
array = map(str, S)

alphabet = []
number = []

for a in array:
    if a.isalpha():
        alphabet.append(a)
    else:
        number.append(int(a))

alphabet.sort()

alphabet = ''.join(alphabet)

print(alphabet + str(sum(number)))
