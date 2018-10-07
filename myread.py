f = open("input.txt", "r")
fout = open("output.txt", "w")

str = f.readline() 
count = 1
while str:
  if count % 2 == 1:
    fout.write(str)
  str = f.readline()
  count += 1


'''
s = f.read()
print(s)
'''

f.close()
fout.close()

