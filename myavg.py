my_list = [1, 13, 26]

f = open("input.txt", "r")

sum = 0
count = 0
for str in f:
  tokens = str.split()
  for num in tokens:
    sum += int(num)
    count += 1
print sum

avg = sum / float(count)
print avg

f.close()