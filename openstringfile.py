# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
f = fh.read()
final = f.upper().rstrip()
print (final)
