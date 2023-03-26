s = "()[]{}"
pair = {'(': ')', '[': ']', '{': '}'}
stack = []
for x in s:
    if x in '([{':
        stack.append(x)
    elif len(stack) == 0 or x != pair[stack.pop()]:
        print(False)
print(len(stack) == 0)


