file = open('test01.in', 'r')
table = dict()
cars = dict()

for row in file:
    row = row.strip().split()
    # this add salesman in a "table" dictionary
    if row[0] not in table:
        table[row[0]] = 0
    # this add price in a "table" dictionary as values to the salesman
    if row[-1] not in table:
        table[row[0]] += int(row[-1])
    # this add name of car in a "cars" dictionary
    if row[1] not in cars:
        cars[row[1]] = 1
    else:
        cars[row[1]] += 1

sorted_table = sorted(zip(table.keys(), table.values()), key=lambda t:t[1], reverse=True)
name, sumPrice = sorted_table[0]
print(name, sumPrice)
name, sumPrice = sorted_table[1]
print(name, sumPrice)
name, sumPrice = sorted_table[2]
print(name, sumPrice)

switch = 0
for key, value in cars.items():
    print(key, value)
    switch += 1
    if switch == 3:
        break
file.close()



