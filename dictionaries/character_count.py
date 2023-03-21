message =  'My name is Carlos Sainz and I am race car Driver for Scuderia Ferrari'
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1
    
print(count)