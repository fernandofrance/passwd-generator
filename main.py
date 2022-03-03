import random, string

size = int(input("Password's length: ")) 
chars = string.ascii_letters + string.digits + '!@#$%&*()-+.=,/\|;:^~[]{}?'
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))