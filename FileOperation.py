
Quote = "Sabra ka fal mitha hota hai \n"

"""Write into file if not availabel create New one"""

FileOprationCreateAdd = open("Quote.txt","w")

FileOprationCreateAdd.write(Quote)
FileOprationCreateAdd.close()

"""This is to append inforamtion"""

Quote1= "Also things happens for good \n"

FileOprationAppend = open("Quote.txt","a")

FileOprationAppend.write(Quote1)

FileOprationAppend.close()


"""THis is to read files data"""

# read as List

FileOperationRead = open("Quote.txt","r").readlines()

print(FileOperationRead)



# read as Line

FileOperationRead = open("Quote.txt","r").read()

print(FileOperationRead)