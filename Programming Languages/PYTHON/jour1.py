
message = 'Hello Wolrd'

print(message) 

print(len(message))

print(message[10])

print(message[0:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('Hello'))

print(message.count('l'))

print(message.find('World'))

print(message.count('Universe'))

new_message = message.replace('Wolrd', 'Universe')

greeting = 'Hello'
name = 'Michael'

message2 = greeting + ', ' + name + '. Welcome!'     
                                                      
message2 = '{}, {}, Welcome!'.format(greeting, name) #this is better 

message2 = f'{greeting}, {name}, Welcome!' #this is the best 
print(message2)

message2 = f'{greeting}, {name.upper()}, Welcome!' 
print(message2)

print(dir(name))

print(help(str))

print(help(str.lower))