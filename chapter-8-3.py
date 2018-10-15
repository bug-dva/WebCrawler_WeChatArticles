f = open('test.txt', 'w')
f.write('I am linpz!')
f.close()

f = open('test.txt', 'r')
content = f.read()
f.close()

print content


with open('test.txt', 'r') as f:
    print f.read()