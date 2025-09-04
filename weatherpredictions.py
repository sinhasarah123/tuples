weather=(1,0,0,1,0,0,0,0)
sunny=1
rainy=0
for i in range(0,7):
    if weather[i]==sunny:
        print("Day",i+1,": Sunny")
    else:
        print("Day",i+1,": Rainy")