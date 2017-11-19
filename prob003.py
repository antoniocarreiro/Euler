import math

primeFactor = 600851475143
counter = 3
sqrtOf = math.sqrt(primeFactor)
highestValue = 0

def CheckPrime(numCheck):
    i = 2
    while i < numCheck:
        if numCheck % i == 0:
            return 0
        i += 1
    return 1

while counter < sqrtOf:
    if (primeFactor % counter == 0):
        if CheckPrime(counter):
            highestValue = counter
    counter += 2
    
print "The highest prime factor of %d is %d" % (primeFactor, highestValue)
