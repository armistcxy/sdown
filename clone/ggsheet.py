import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Student:
    def __init__(self, name, id, link):
        self.name = name
        self.id = id
        self.link = link

#info contain student_name - student_id - correspond github link
def get_all_info():
    #oauth2
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
    client = gspread.authorize(credentials)


    #how to get credential: https://medium.com/@a.marenkov/how-to-get-credentials-for-google-sheets-456b7e88c430
    #Note: you need to go into .json file and paste the client email into account you can share from spread sheet
    #----- 
    sheet_name = "djq"
    spread_sheet = client.open(sheet_name)
    worksheet = spread_sheet.get_worksheet(0)

    name_list = worksheet.col_values(2)
    msv_list = worksheet.col_values(3)
    link_list = worksheet.col_values(11)


    student_list = []
    for name, msv, link in zip(name_list, msv_list, link_list):
        if name == "": continue
        if link[len(link)-9:] == 'tree/main': #this type of link cannot be used to download
            link = link[:len(link)-9]
        name = name.replace(' ','_')
        student_list.append(Student(name, msv, link))

    #use this to extract link https://stackoverflow.com/questions/35230764/how-to-extract-url-from-link-in-google-sheets-using-a-formula

    return student_list
