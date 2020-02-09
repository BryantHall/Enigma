#Attempt to decrpyt the cipher using frequency based probability

import csv

#List of character frequency
alphabetTable =  [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
conversionTable = [' ','e','t','a','o','n','r','i','s','h','d','l','f','c','m','u','g','y','p','w','b','v','k','x','j','q','z']
#punctuationTable = [',',':','(',')',';','.','?','!']
charSum = [0] * 27
oldSum = [0] * 27

#read in .csv file
with open('dataF.csv') as csvfile:
    fileData = csv.reader(csvfile,delimiter=',')

    #sum number of characters
    for column in fileData:
        for i in range(0,len(alphabetTable)):
            if column[1] == alphabetTable[i]:
                charSum[i] = charSum[i] + 1

#save old fequency table and newly sorted frequency table
for i in range(0,len(charSum)):
    oldSum[i] = charSum[i]
charSum.sort(reverse = True)

#debug
print(charSum)

#This will be the decrypting cipher
key = [] 
for i in range(0,len(alphabetTable)):
    for j in range(0,len(conversionTable)):
        #every a goes to t
        #if(j > 0 and j < (len(conversionTable) - 1) and charSum[j] == charSum[j-1]):
            #key.append(conversionTable[j + 1])
         #   charSum[j-1] = -1
         #   break
        if(oldSum[i] == charSum[j]):
            key.append(conversionTable[j])
            charSum[j] = -1
            break

#write out file
with open('dataF.csv') as csvfile:
    fileData = csv.reader(csvfile,delimiter=',')

    #open output file
    output = open("converted.txt", "w")

    for column in fileData:
        for i in range(0,len(alphabetTable)):
            if(column[1] == alphabetTable[i]):
                cipherChar = key[i]
                output.write(cipherChar)
                break
    output.close()

#write to csv file
#with open('converted.csv', 'w',newline='') as file:
#    writer = csv.writer(file)
#    for i in range(0,360):
#        for j in range(0,len(alphabetTable)):
#            if(oldSum[] == charSum[]):
##                column[0] = conversionTable[]
#                writer.writerow(column[0])
##                break
##

#debug
print(key)
print(oldSum)
print(charSum)
#['t', 'j', 'y', 'm', 's', 'i', 'p', 'w', 'n', 'd', 'k', 'v', 'l', 'u', 'e', 'h', 'b', 'z', 'r', 'o', 'f', 'a', 'x', 'g', 'q', 'c'] 