filename = 'article.txt'  

with open(filename, encoding='utf-8) as file:   #open the exist file 
          lines = file.read()                   
lines = lines.replace('\n', ' ')                   
newlines = lines.split('.')
newfile = open('newarticle.txt', 'w', encoding='utf-8')
for i in newlines:
          a = i + '\n'*2
          newfile.write(a)
newfile.close()
