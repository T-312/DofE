import xlsxwriter
import os
import sys

os.chdir('/Users/Tim/Desktop/Text Files/')

workbook = xlsxwriter.Workbook('Test.xlsx')
worksheet = workbook.add_worksheet()
q = 1

worksheet.write(0, 0, 'Subject')
worksheet.write(0, 2, 'Date')
worksheet.write(0, 4, 'Name')

while True:
    #Inputs
    books = input("Enter book name: ")
    authors = input("Enter author names: ")
    pages = input("Enter number of pages: ")

    worksheet.write(q, 0, books)
    worksheet.write(q, 2, authors)
    worksheet.write(q, 4, pages)
    q+=1

    cvc = input("Would you like to continue (y/n): ")
    if cvc == "y":
        pass
    elif cvc == "n":
        workbook.close()
        exit()