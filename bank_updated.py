class banking:
    w = list()

    def __init__(self):
        self.name = str()
        self.mobile = int()
        self.father = str()
        self.age = int()
        self.breakout = 0
        self.paisa = 0.0

    def DEPOSITE(self,pop,mobile):
        for i in banking.w:
            if (i.mobile == mobile):
                i.paisa+=pop
                self.paisa = i.paisa
                banking.w.append(self)
                return

    def addcous(self):
        banking.w.append(self)
        

    def CHECKING(self, name, mobile):
        for i in banking.w:
            if (i.name == name and i.mobile == mobile):
                self.breakout =i.breakout = 11
                self.name = i.name
                self.mobile = i.mobile
                self.father = i.father
                self.age = i.age
                self.paisa = i.paisa
                return
            
    
        
        

import time
import calendar
localtime = time.asctime( time.localtime(time.time()) )
cal = calendar.month(2019, 7)
print('                                                   Day Mnth Date TIME  YEAR')
print('                                                  ',localtime)
print(cal,end='')


print('\n','\n')

kok=('           WELCOME TO THE BANK OF INDIA....\n ')
for i in kok:
    print(i,end='')
    time.sleep(.1)
while (True):
    print(' -------------------------------------------------------------- ')
    print(' \n     Creat New Account : 1 \n     Deposite Money : 2 \n     Account Details : 3 \n     Exit : 0 \n')
    n = input('Enter your coice here :  ')
    if (n == '1'):
        cus = banking()
        v=1
        pp=0
        while(v==1):
            cus.name = input('ENTER YOUR NAME :')
            pp+=1
            for i in cus.name:
                if i.isalpha():
                    if i != cus.name[-1]:
                        continue
                    else:
                        r=1
                        c=0
                        while(r==1):
                            c+=1
                            try:
                                cus.mobile = int(input('ENTER YOUR MOBILE NUMBER :'))
                                cus.CHECKING(cus.name,cus.mobile)
                                if cus.breakout != 11:
                                    w=str(cus.mobile)
                                    if len(w) == 10:
                                        pass
                                    else:
                                        print('------------- Wrong Mobile Number -----------------')
                                        if c == 5:
                                            print('<<<<<<<<<<  ---- YOU TRY it many times \n                 SORRY B BYE... ---- >>>>>>>>')
                                            v=0
                                            break
                                        else:
                                            continue
                                else:
                                    print('      ID ALREADY EXISTS WITH THESE DETAILS    ')
                                    v=0
                                    break
                                    
                            except:
                                print('--------------- Wrong Mobile Number ------------')
                                if c == 5:
                                    print('              YOU TRY it many times \n                 SORRY B BYE...')
                                    v=0
                                    break
                                else:
                                    continue
                                    
                            else:
                                cus.father = input('FATHER NAME :')
                                try:
                                    cus.age = int(input('ENTER YOUR AGE :'))
                                    ee=str(cus.age)
                                    if len(ee)==2:
                                        pass
                                    else:
                                        AtrributeError
                                except:
                                    print('     INCORRECT AGE')
                                    import time
                                    ap='SORRY... You Have To Start With First Step'
                                    for k in ap:
                                        print(k,end='')
                                        time.sleep(.2)
                                    v=0
                                    break
                                else:
                                    cus.addcous()
                                    print(' --------------------------------------------------------------------')
                                    print('                    HEY !! YOU ARE A MEMBER OF THIS BANK ..~~ \n ')
                                    print('          YOUR ID IS :: ', cus.name)
                                    print('          YOUR PASSWORD IS ::', cus.mobile)
                                    v=0
                                    break
                                                  
                            
                                    

                else:
                    if pp==5:
                        print('YOU TRY it many times \n                 SORRY B BYE...')
                        v=0
                        break
                    else:
                        print('-------------- Wrong Name --------------------')
                        break
        
    if (n == '2'):
        print('                           WELCOME TO THE BANK OF INDIA')
        q = len(banking.w)
        cus = banking()
        cus.name = input('Enter your ID :')
        cus.mobile = int(input('Enter your password'))
        cus.CHECKING(cus.name, cus.mobile)
        if cus.breakout == 11:
            print('            ACCESS GRANTED ')
            import time
            y= '   HELLO  '+(cus.name.upper())
            for i in y:
                print(i,end='')
                time.sleep(.1)
            try:
                pop= float(input('\n ENTER AMOUNT TO DEPOSITE = '))
            except:
                print('  <<<<<   INVALID MONEY   >>>>>>>')
                print('~~~~~~~~    Sorry we are exit you ~~~~~~  TRY AGAIN LATER')
                v=0
                break
            else:
                cus.DEPOSITE(pop,cus.mobile)
            
                print('                            MONEY ADDED SUCCESSFULLY \n')
                print('\n                      YOUR CURRENT STATUS OF MONEY IS  ',cus.paisa)
            
        else:
            print('                            OOpss..  WRONG ID OR PASSWORD')
            


    if (n == '0'):
        import time
        khatam='   THANKS FOR YOUR VALUABLE TIME   \n      HAVE A STUNNING DAY ...  '
        for i in khatam:
            print(i,end='')
            time.sleep(.1)
        break


    if (n =='3'):
        print('                           WELCOME TO THE BANK OF INDIA')
        cus = banking()
        cus.name = input('Enter your ID :')
        cus.mobile = int(input('Enter your password'))
        cus.CHECKING(cus.name, cus.mobile)
        if cus.breakout == 11:
            print('            ACCESS GRANTED ')
            print('YOUR DETAILS ARE  \n')
            print(' NAME = ',cus.name)
            print(' MOBILE =' ,cus.mobile)
            print(' FATHER NAME =',cus.father)
            print(' AGE =',cus.age)
            print(' ACCOUNT BALANCE =',cus.paisa)
        else:
            print('                            OOpss..  WRONG ID OR PASSWORD')
        













