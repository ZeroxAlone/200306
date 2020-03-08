# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:14:42 2020

@author: lisa_
"""


def GetInfo():
    while True:
        UserID = input("Enetr a user ID: ")
        if len(UserID)==5 and 65<=ord(UserID[0])<=90 and UserID[1:].isdigit():
            break
    PreferredName = input("Enter a preferred name: ")
    return UserID + "*" + PreferredName

def WriteInfo(ThisString):
    file1 = open("File1.txt","w")
    file2 = open("File2.txt","w")
    if 65<=ord(ThisString[0])<=77:
        file1.write(ThisString[:5])
    else:
        file2.write(ThisString[:5])
    file1.close()
    file2.close()
    return True
    
def TopLevel():
    C = "Y"
    while C=="Y":
        Temp = WriteInfo(GetInfo())
        if Temp == False:
            break
        C = input("Enter 'Y' to continue, 'N' to end program: ")

TopLevel()