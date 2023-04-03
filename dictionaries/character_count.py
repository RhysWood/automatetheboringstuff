import pprint

message =  'My name is Carlos Sainz and I am race car Driver for Scuderia Ferrari'
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1
    
pprint.pprint(count)
#{' ': 13,
# 'A': 9,
#'C': 4,
# 'D': 3,
# 'E': 5,
# 'F': 2,
# 'I': 6,
# 'L': 1,
# 'M': 3,
# 'N': 3,
# 'O': 2,
# 'R': 10,
# 'S': 4,
# 'U': 1,
# 'V': 1,
# 'Y': 1,
# 'Z': 1 }