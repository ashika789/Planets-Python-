
def main():

    #The import random is the random number generator needed.
    import random
    #The myfile open command will open the txt document made with the numbers.
    myfile = open('numbers.txt', 'w')
    
    number = random.randint(4,11)
    
    i = 0;
    while i < number:
        num = random.randint(10, 20)
        myfile.write(str(num) + '\n')
        i = i + 1

    myfile.close()

main ()