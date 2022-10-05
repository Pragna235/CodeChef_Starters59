# cook your dish here
for i in range(int(input())):
    n=int(input()) #4
    binary=input()#0001
    binary=list(binary)
    #print("Given binary = ",binary)
    #t=['2','3','4']
    #t=' '.join(str(i) for i in t)
    #print(t)
    t=[]
    for k in range(0,len(binary)): # k=1,2,3,4
        if((k%2)==0):
            alice=binary[0]
            #print('alice = ',alice)
            if(alice=='0'):
                t.insert(0,'0')
                #print('t = ',t)
            else:
                t.append('1')
                #print('t = ',t)
            
            binary=binary[1:]
            #print('sliced alice binary = ',binary)
        else:
            bob=binary.pop()
            #print('bob = ',bob)
            #print('slice bob binary = ',binary)
            if(bob=='0'):
                t.append('0')
                #print('t = ',t)
            else:
                t.insert(0,'1')
                #print('t = ',t)
    print(''.join(t))
            
            
            
            
    
    