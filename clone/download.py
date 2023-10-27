from ggsheet import Student, get_all_info
import os

#given Student field clone that repo
PREFIX_COMMAND = "git clone "
def clone_repo(student):
    directory = student.name + "-" + str(student.id)
    command = PREFIX_COMMAND + student.link + " " + directory
    os.system(command)

#get all repositories with specify identity
def get_all_repos():
    student_list = get_all_info()
    for student in student_list:
        clone_repo(student)
    
if __name__ == "__main__":
    get_all_repos()