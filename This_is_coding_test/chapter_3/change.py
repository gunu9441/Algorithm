money_list = [500, 100, 50, 10]
prize = 1260
count = 0

for money in money_list:
    count += prize // money
    prize %= money

print("Total coin: {}\n".format(count))
