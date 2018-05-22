chance = 3
chance = int(chance)
password = '1234'
while True:
    password = input('請輸入密碼:')
    if password == '1234':
    	print('登入成功')
    	break
    elif password != '1234' and chance == 3:
    	chance = chance - 1
    	print('密碼錯誤，還有兩次機會')
    elif password != '1234' and chance == 2:
    	chance = chance - 1
    	print('密碼錯誤，還有一次機會')
    elif password != '1234' and chance <= 1:
    	chance = chance - 1
    	print('密碼錯誤，登入失敗')
    	print('密碼鎖定跳出系統')
    	break
#password = 'a123456'
#i = 3
#while True:
    #pwd = input('請輸入密碼')
    #if pwd == password:
        #print('登入成功')
        #break
    #else:
        #i = i -1
        #print('密碼錯誤!還有', i ,'次機會')
        #if i == 0:
            #break

#password = 'a123456'
#i = 3
#while i > 0:
    #pwd = input('請輸入密碼')
    #if pwd == password:
        #print('登入成功')
        #break
    #else:
        #i = i -1
        #print('密碼錯誤!還有', i ,'次機會')
        