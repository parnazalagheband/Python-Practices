import random
boys=["ali","reza","yasin","benyamin","mehrdad","sajjad","aidin","shahin"]
girls=["sara","zari","neda","homa","eli","goli","mary","mina"]

marriage=[]

random.shuffle(girls)

for i in range(len(girls)):
    marriage.append((boys[i],girls[i]))

print(marriage)    