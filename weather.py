rainy = input("how is the weather? is it raining? y/n: ").lower()
cold = input("is it cold outside ? y/n : ").lower()
if (rainy == 'y' and cold == 'y' ):
    print("you'd better STUDY. ")
elif (rainy == 'y' and cold != 'y'):
    print("carry an umbrella with you. ")
elif(rainy != 'y' and cold =='y' ):
    print("you'd better wear a jacket.")
elif(rainy !='y' and cold !='y'):
    print("")
