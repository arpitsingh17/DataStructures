import random
originalstring = 'app'

def generator(originalstring):
    
    string = 'abcdefghijklmnopqrstuvwxyz '
    desired = ''
    for i in range(len(originalstring)):
        desired = desired + (string[random.randrange(27)])
    
    return(desired)

def score(originalstring,desired):
    numscore = 0
    for i in range(len(originalstring)):
        if desired[i] == originalstring[i]:
            numscore += 1
    return (float (numscore / len(originalstring)))

def main():
    count = 0
    while(score(originalstring,generator(originalstring))< 1):
        count += 1
    
        print(generator(originalstring))
        print(float (score(originalstring,generator(originalstring))))
    print(count)



main()
