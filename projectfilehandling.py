from pathlib import Path
import os

def createfile():
    try:
        name=input("Please tell your file name:-")
        path=Path(name)
        if not Path.exists():
            with open(Path,"w") as fs:
                data=input("What you want to write:-")
                fs.write(data)
            print("file created successfully")  
        else:
            print("Error file name already exists")
    except Exception as err:
        print(f"an error occured as {err}")

def readfile():
    try:
        name=input("Please tell your file name:-")
        path=Path(name)
        if ath.exists():
            with open(path,"r") as fs:
                content=fs.read()
                print(f"yuor file content is \n {content}")
        else:
            print("error no such file exist") 
    except Exception as err:
        print(f"an error occured as {err}")   

def updatefile():
    try:
        name=input("Please tell your file name:-")
        path=path(name)

        if path.exists():
            print("Operations")
            print("1.Renaming the file")
            print("2.Appending the content")
            print("3.Overwriting the file")

            choice=int(input("enter your option:-"))

            if choice==1:
                newname=input("tell your new file name:-")
                new_path=path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully ")
                else:
                    print("file already exists")
                
            elif choice == 2:
                with open(path,'a') as fs:
                    data = input("what do you want to append :- ")
                    fs.write(" \n"+data)
                print("successfully appended")
                
            elif choice == 3:
                with open(path , "w") as fs:
                    data = input("what do you want to overwrite :- ")
                    fs.write(" \n"+data)
                print("successfully overwrittten")

    except Exception as err:
       print(f"An error occured as {err}")




def deletefile():
    try:
        name = input("please tell your file name :- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("Error no such file exists")
    except Exception as err:
        print(f"An error occured as {err}")



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

a = int(input("\ntell your response :- "))


if a == 1:
    createfile()
if a == 2:
    readfile()
if a == 3:
    updatefile()
if a == 4:
    deletefile() 


