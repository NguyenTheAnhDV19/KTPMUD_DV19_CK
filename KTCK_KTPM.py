lst = [1,2,3,4] 
def sum() :
    k = 0 
    for i in lst :
        for j in range(2,i) :
            if i % j == 0 :
                k= k +1 
    return k

print("Tong so so nguyen to :",sum())



