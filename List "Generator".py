num_int = 0
num = 0
Repeater = 'Y'
MainList = [0]
resp = True

while Repeater == 'Y' :
    while resp == True :
        num_int = 0
        while num_int <= 0 :
            num = input('Enter a number: ')
            try :
                num_int = int(num)
            except :
                num_int = -1
            print('Please do not enter a letter')
            continue
        break


    print(num_int)    

    RespondListRegulator = 1
    while RespondListRegulator > 0 :
        RespondList = input('Do you want to add it to the list? (Y or N): ')
        if RespondList == 'Y':
            break
        elif RespondList == 'N' :
            break
        else :
            print('Please type Y or N only')
            RespondListRegulator = RespondListRegulator + 1
        continue
        

        
        
    if RespondList == 'Y' :
        RespondList = True
    elif RespondList == 'N' :
        RespondList = False
        
    if RespondList == True :
        MaintList = MainList.append(num_int)
        
    print(MainList)
    print('Thank You!')
    RepeaterRegulator = 1
    while RepeaterRegulator > 0 :
        Repeater = input('Do you still want to continue? (Y or N) :')
        if Repeater == 'Y':
            break
        elif Repeater == 'N' :
            break
        else :
            print('Please type Y or N only')
            RepeaterRegulator = RepeaterRegulator + 1
            continue
    continue
    
print('Thank you! Come again!')
