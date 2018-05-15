import random

'''
Playing with random built in function a bit
'''


# Pseudorandom numbers each time the program is run
for x in range(10):
    print(random.random())

print('-'*40)

# Since we use the same seed, these 10 numbers will always be the same when the program is run
'''
random.seed(0)
for x in range(10):
    print(random.random())

'''

miss = 0
hit = 0
for x in range(1000000000):
    y = random.random()
    if y < 0.5:
        hit += 1
    else:
        miss += 1

print("Hit: {}\n"
      "Miss: {}".format(hit, miss))

