

def main():

    #The elements of the list
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
                      'Saturn', 'Uranus', 'Neptune',]
    list_size = len(planets)

    print('Number of Planets: ',list_size)

    #The for loop to give each planet their own line.
    for name in planets:
        print(name)

def playlist():
    print 'This is the chopped portion:'

    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
                      'Saturn', 'Uranus', 'Neptune',]
    list_size = len(planets)
    i = list_size - 2;
    while i > 0:
        print (planets [i])
        i = i - 1
               

main()
playlist()