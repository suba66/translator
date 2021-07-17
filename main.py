import re
#input file
fin = open("t8.shakespeare.txt", "rt")
#output file to write the result to
fout = open("t8.shakespeare.translated.txt", "wt")
#lookup file
fcsvin = open("french_dictionary.csv", "rt")

for line in fcsvin:
 string1 = line
match  = re.findall(r'[^\s,]+', string1)
key1=''
val1=''
data = fin.read()
datatemp=''

for m in match:
 if(key1 != ''):
  val1 = m
  print ('key1'+key1)
  print (val1)
  fout.write(data.replace(key1, val1))
 else:
  key1 = m

#fout.write(data)		
fin.close()
fout.close()
