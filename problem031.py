# In England the currency is made up of pound and pence, and there
# are eight coins in general circulation:
# 
# 1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.
# It is possible to make 200p in the following way:
# 
# 1*100p + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
# How many different ways can 200p be made using any number of coins?

# started doing research, accidentally found generating function
# https://www.math.upenn.edu/~wilf/PIMS/PIMSLectures.pdf
# http://math.stackexchange.com/questions/176363/keep-getting-generating-function-wrong-making-change-for-a-dollar/176397#176397
c = [1]
c = c + [0 for x in range(0,200)]
for k in [1,2,5,10,20,50,100,200]:
    for i in range(0,201-k):
        c[i+k] += c[i]
        
print(c[200])