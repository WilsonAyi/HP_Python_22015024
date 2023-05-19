i = 0  # variable i
while i < 50:  # while i less than 50
    i += 1  # increment i
    if i % 3 == 0:  # if i when divided by 3 has zero remainder print "Boy"
        print("Boy")
    elif i % 5 == 0:  # else if i when divided by 5 has zero remainder print "Girl"
        print("girl")
    elif i % 3 == 0 & i % 5 == 0:  # else if i when divided by both 3 and 5 has a remainder zero print "couple"
        print("couple")
    else:
        print(i)  # print the incremented i
