numbers = [str(i) for i in range(10)]
result = []
number_result = 0
given = input()

for i in given:
    if i in numbers:
        number_result += int(i)
    else:
        result.append(i)

result.sort()
if number_result != 0:
    result.append(str(number_result))

print("".join(result))

# Solution
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))
