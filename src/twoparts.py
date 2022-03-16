# Function to divide number to two parts
def twoParts(number) :
    possible_couples = []
    for i in range(1,number//2+1):
        for j in range(i,number):
            if i+j == number and i!=j:
                possible_couples.append([i,j])
    return possible_couples
