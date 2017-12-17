
Qute = "Sabra ka fal mitha hota hai \n"

"""Write into file if not availabel create New one"""

FileOprationCreateAdd = open("Qute.txt","w")

FileOprationCreateAdd.write(Qute)
FileOprationCreateAdd.close()

"""This is to append inforamtion"""

Qute1= "Also things happens for good \n"

FileOprationAppend = open("Qute.txt","a")

FileOprationAppend.write(Qute1)

FileOprationAppend.close()


"""THis is to read files data"""

# read as List

FileOperationRead = open("Qute.txt","r").readlines()

print(FileOperationRead)



# read as Line

FileOperationRead = open("Qute.txt","r").read()

print(FileOperationRead)