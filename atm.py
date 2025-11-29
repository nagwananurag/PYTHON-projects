c=1


while True:
    
    pin=1786
    Amount=45456
    print("Welcome\nAttempt",c)
    pn=int(input("Enter Your PIN:"))
    if pin==pn:
        print(f'Your current Amount is:{Amount}')
        
        draw=int(input("Enter Amount To Withdraw:"))
        
        f=Amount-draw
        print(f'Withdraw Amount :{draw}\n Your Current Amount is:{f}')
        
    else:
        c+=1
        print("You Entered Wrong PIN")
        
        if c>3:
          print("Your account is blocked for 24 hours")
          
          break
      
