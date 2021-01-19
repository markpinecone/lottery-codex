import random as rd

random = rd.randint(1,48)
odd=even=high_n=low_n=0
rdlist = []
condition = False
count = 0

def loop(rdlist):
    global random,odd,even,low_n,high_n 
    for _ in range(6):
        while random not in rdlist:
            rdlist.append(random)
            
            if random % 2 == 1:
                odd += 1
            if random % 2 == 0:
                even += 1
            if random <= 24:
                low_n += 1
            if random >= 25:
                high_n += 1  
            
            
        while random in rdlist:
            random = rd.randint(1,48)
    #print(rdlist)
            
    
    

def validation():
    global condition, odd, even, high_n, low_n
    if odd == even == high_n == low_n == 3:
        condition = True
        rdlist.sort()
        print(rdlist)

        
    else:
        condition = False
        rdlist.clear()
        loop(rdlist)
        
def reset():
    global condition, rdlist, odd, even, high_n, low_n
    odd=even=high_n=low_n=0
    condition = False
    rdlist = []


  
    

 
while condition != True:
    reset()
    loop(rdlist)
    validation()
    #print(odd, even, low_n, high_n)
    
