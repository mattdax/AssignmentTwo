


for i in range(0,len(accountsContent),1):
    if accountsContent[i]=='@':
        start=i
        print('start',start)
    elif accountsContent[i]=='$':
        end=i
        print('end',end)
        accountsUsername=accountsContent[start:end]

        print(accountsUsername)

        if accountsUsername==username:
            for i in range(end,len(accountsContent),1):
                if accountsContent[i]=='@':
                    realPassword = accountsContent[end:(i - 1)]
                    print(realPassword)
                    break



print('username:',username)
print('password entered:',password)
print('actual pass',realPassword)