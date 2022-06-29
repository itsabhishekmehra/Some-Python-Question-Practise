# 1. Check a number prime or not
i = 0
while(i<10):
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    else:
        print(i)
    i+=1

# # Find a prime number (1-10)
# for i in range(1,11):
# 	    if i>1:
# 	        for j in range(2,i):
# 	            if i%j==0:
# 	                break
# 	        else:
# 	            print (i)
    
    