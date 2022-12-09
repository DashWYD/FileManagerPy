import os 


option = input("Do you want to delete or create a file( (D) to delete and (C) to create \n")

if(option == "C"):
  fName = input("Please type the file name, Please include an extension \n")
  f = open(fName, "w")
  print("Successfully created!")

if(option == "D"):
  FNameD = input("Please input the file you want to delete, please include an extension \n")
  if(os.path.exists(FNameD)):
    os.remove(FNameD)
    print("Successfully removed!")
  else:
    print("Path not found, please enter a new path.")
