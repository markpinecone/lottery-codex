import random as rd


def loop():
    random = rd.randint(1,48)
    odd=even=high_n=low_n=0
    rdlist = []
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
                
          
            if odd == even == high_n == low_n == 3:
                rdlist.sort()
                return rdlist 
            else:
                break
a = loop()

while True:
    a = loop()
    if a != None:
        print(a)
        break
    