instring = input("請輸入字串:")

#找字首、字尾、及中間
mid = (len(instring)-1)//2
start = 0
last = len(instring)-1
flag = 0

#判斷前後文字
while(start <= mid):
    if(instring[start]==instring[last]):
        start += 1
        last -=1
    else:
        flag = 1
        break;
if flag == 0:
    print("此為回文字串")
else:
    print("此不為回文字串")