
def main():
    #This will open the file
    myfile = open ('numbers.txt', 'r')
    #the for and in displays it.

    for line in myfile:
        #The '' will stop the spacing
        print(str(line))

    myfile.close()

main()