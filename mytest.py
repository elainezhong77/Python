f = open("input.txt", "r")
fout = open("output.txt", "w")


for str in f:
  tokens = str.split()
  fout.write(tokens[2] + "\n")


'''
s = f.read()
print(s)
'''

f.close()
fout.close()

