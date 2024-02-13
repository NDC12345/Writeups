string = '''./flag.txt'''
strings = ""
for i in string:
      h =  "chr(" + str(ord(i)) + ")" + "+"
      strings += h
print(strings)

