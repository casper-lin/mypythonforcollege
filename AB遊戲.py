
import random
answer = random.sample(range(10),4)
a=b=n=0
while a!=4:
    a=b=n=0
    user=list(input("猜數字:"))
    for i in user:
        if int(user[n]) == answer[n]:
            a +=1
        else:
            if int(i) in answer:
                b +=1
        n+=1
    print(user,":",a,"A",b,"B")
    output = ','.join(user).replace(',','')
    print(f'{output}:{a}A{b}B')

    an = input("看答案?(y/n):")
    if((an == "y")or(an == "Y")):
        print(answer)
        break
if(a==4):
    print("成功!")