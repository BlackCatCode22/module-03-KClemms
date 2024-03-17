num = 0
tot = 0.0
maxNum = 0
minNum = 0


while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
      
    minNum = min(minNum,fval)  
    maxNum = max(maxNum,fval)
    num = num + 1
    tot = tot + fval

print(tot, num, maxNum, minNum)