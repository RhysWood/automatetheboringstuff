#concat strings with +
print('Hello' + 'World')
#HelloWorld

#but this is tricky with long concatonations
name = 'Rhys'
place = 'Nanaimo'
time = '3pm'
food = 'pizza'
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')
#Hello Rhys, you are invited to a party at Nanaimo at 3pm. Please bring pizza.

#string interpolation! 
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)) #inversion specifiers
