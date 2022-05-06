# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:59:03 2022

@author: Waleed Esmat
"""

import json
import secrets
import hashlib
import sys
import argparse

def duplicate(usernames,username):
    for i in usernames:
        if i == username:
            print("username already exists \n")
            return False
    return True


      



parser=argparse.ArgumentParser(description='Take text file path')
parser.add_argument('-inputs', nargs='+', help='<Required> Set flag', required=True)
path=parser.parse_args()
username=path.inputs[0]
password=path.inputs[1]
print(username+" " + password)
# flag3=True
# while True:
#     while(flag3):
#         print("what do you want to do? \n")
#         choice=input("A.Login  B.Add new user  C.Delete user D.First time use E.exit\n")
#         if(choice.lower()!='a' and choice.lower()!='b' and choice.lower()!='c' and choice.lower()!='d' and choice.lower()!='e'  ):
#             print("Please choose a correct choice \n")
#         else:
#             flag3=False
#    flag3=True
choice = 'b'
first_time=True
db_3=db_2=db_1={}
usernames=[]
if choice.lower() == 'd' : ##first time
    with open ('database.json','w') as f:
        flag = True
        flag_2=True
        while flag :
            username=input("please enter ur username \n")
            replica = duplicate(usernames,username)
            usernames.append(username)
            if  replica==True:
                password=input("please enter ur password \n")
                salt = secrets.token_hex(8)
                password_hash=hashlib.sha1((password+salt).encode()).hexdigest()
                if first_time == True:
                    db_3={"salt":salt,"password hash":password_hash}
                    db_2={username:db_3}
                    first_time=False
                else:
                    db_3={"salt":salt,"password hash":password_hash}
                    db_2[username]=db_3
                while flag_2: 
                    decision= input("want to enter another username and password ? \n yes or no ? \n")
                    if decision.lower()!= "yes" and decision.lower()!="no":
                        print("please enter yes or no !! \n")
                    elif decision.lower() == "no":
                         flag=False
                         db_1={"securesystem":db_2}
                         ob=json.dumps(db_1,indent=4)
                         f.write(ob)
                         break
                    else:
                         break
            else:
                while True:
                    wrong=input("want to enter another one or end?\n A.enter another username   B.end\n")
                    if(wrong.lower()=='b'):
                        flag=False
                        ob=json.dumps(db_1,indent=4)
                        f.write(ob)
                        break;
                    elif(wrong.lower()=='a'):
                        break;
                    elif(wrong.lower()!='a' and wrong.lower()!='b'):
                        print("enter a valid choice\n")
                    
                    
            
              
elif choice.lower() == 'c' : #Delete user
    flag=True
    while flag:
        username = input("enter username u want to delete \n")
        password = input("enter password\n")
        with open ('database.json','r') as f:
            try:
                file=json.load(f)
            except:
                print("JSON FILE IS EMPTY")
                break
            db=file.get("securesystem")
            while True:
                
                credentials=db.get(username)
                #print(credentials)
                
                if len(db) == 0:
                    print("json file is empty !! no usernames to delete \n")
                elif credentials==None:
                    print("Username not found, please enter a valid one \n")
                    username=input()
                else:
                    break
            salt=credentials.get('salt')
            password_hash_original=credentials.get('password hash')
            password_hash=hashlib.sha1((password+salt).encode()).hexdigest()
            flag2=True
            while flag2:
                if (password_hash_original==password_hash):
                    db.pop(username)
                    flag2=False
                else:
                    print("wrong password \n enter password again")
                    password=input()
                    password_hash=hashlib.sha1((password+salt).encode()).hexdigest()
        with open ('database.json','w') as f:
            db={'securesystem':db}
            ob=json.dumps(db,indent=4)
            f.write(ob)
        
        while True:
            decision=input("want to delete another user?\n A.yes   B.no\n")
            if(decision.lower()=='b'):
                flag=False
                break
            elif(decision.lower()!='a' and decision.lower()!='b'):
                print("enter a valid choice")
            elif(decision.lower()=='a'):
                break
                
elif choice.lower() == 'b' : #add user
   with open ('database.json','r') as f:
       try:
           file=json.load(f)
       except:
           print("JSON FILE IS EMPTY")
           sys.exit("JSON File is empty, create file first")
   with open ('database.json','w') as f:
        flag = True
        flag_2=True
        db=file["securesystem"]
        usernames=[]
        for i in db:
            usernames.append(i)
        while flag :
            #username=input("please enter ur username \n")
            replica = duplicate(usernames,username)
            usernames.append(username)
            if  replica==True:
                #password=input("please enter ur password \n")
                salt = secrets.token_hex(8)
                password_hash=hashlib.sha1((password+salt).encode()).hexdigest()
                # if first_time == True:
                #     db_3={"salt":salt,"password hash":password_hash}
                #     db[username]=db_3
                #     first_time=False
                # else:
                db_3={"salt":salt,"password hash":password_hash}
                db[username]=db_3
                # while flag_2: 
                #     decision= input("want to enter another username and password ? \n yes or no ? \n")
                #     if decision.lower()!= "yes" and decision.lower()!="no":
                #         print("please enter yes or no !! \n")
                #     elif decision.lower() == "no":
                flag=False
                db_1={"securesystem":db}
                ob=json.dumps(db_1,indent=4)
                f.write(ob)
                break
                #     else:
                #          break
            else:
                #print("username already used")
                break
                # while True:
                #     wrong=input("want to enter another one or end?\n A.enter another username   B.end\n")
                #     if(wrong.lower()=='b'):
                #         flag=False
                #         db_1={"securesystem":db}
                #         ob=json.dumps(db_1,indent=4)
                #         f.write(ob)
                #         break;
                #     elif(wrong.lower()=='a'):
                #         break;
                #     elif(wrong.lower()!='a' and wrong.lower()!='b'):
                #         print("enter a valid choice\n")
                    
elif choice.lower() == 'a':
    flag = True
    with open ('database.json','r') as f:
        try:
            file=json.load(f)
        except:
            print("JSON FILE IS EMPTY, CREATE ONE FIRST")
            flag = False
    
    db=file["securesystem"]
    usernames=[]
    while flag :
             
             while True:
                 username=input("please enter ur username \n")
                 try:
                     credentials=db[username]
                     break
                 except:
                     print("username not found!!")
             while True:
                 
                 password=input("please enter ur password \n")
                 salt=credentials['salt']
                 correct_password=credentials['password hash']
                 password_hash=hashlib.sha1((password+salt).encode()).hexdigest()
                 if correct_password == password_hash :
                     print("you have logged in successfully! \n")
                     flag=False
                     break
                 else:
                     print("wrong password !!")
elif choice.lower()=='e':
      print("Have a nice day.. bye!")
      sys.exit(0)
     
