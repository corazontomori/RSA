def angoka():

    print ('暗号化したい文字を入力')
    M = int(input())
    M_E = M ** 5
    C = M_E % 26
    print (C) 

def fukugo():

    print ('暗号化したい文字を入力')
    C = int(input())
    C_D = C ** 5
    M = C_D % 26
    print (M)    
         
print ('暗号化(a) or 複合(f)')
aorf = input()

if aorf == 'a':
    angoka()
elif aorf == 'f' :
    fukugo()
else : 
    print ('再入力してください')

