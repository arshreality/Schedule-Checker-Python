# first_sem[], second_sem[], third_sem[], fourth_sem[], fifth_sem[], sixth_sem[], seventh_sem[], eight_sem[]
def totalCreditHours(class_list):
    credit = 0
    for s in class_list:
        l = list(s)
        for i in range(len(l)):
            if l[i] == ' ':
                credit = credit + int(l[i+2])
    return credit

def classExists(Class, class_list):
    yeah = False
    for element in class_list:
        if Class.lower() == element.lower():
            yeah = True
            break
    return yeah

def Credit(Class):
    credit = 0
    for i in range(len(Class)):
        if l[i] == ' ':
            credit = int(l[i+2])
    return credit


class_list1 = []
class_list2 = []
class_list3 = []
class_list4 = []
class_list5 = []
class_list6 = []
class_list7 = []
class_list8 = []
choice = 0

free_electives_total = 11
guided_electives_total = 9
core_curriculum_total = 42
major_prepatory_courses_total = 20
major_core_courses_total = 42
total_credits_needed_to_graduate = 124

free_electives = 0
guided_electives = 0
core_curriculum = 0
major_prepatory_courses = 0
major_core_courses = 0


all_classes = ['AHST 1303',
'AHST 1304',
'AHST 2331',
'AMS 2300',
'AMS 2341',
'ARTS 1301',
'BIOL 1306',
'BIOL 1307',
'BIOL 1311',
'BIOL 1313',
'CHEM 1311',
'CHEM 1312',
'CS 1200',
'CS 1337',
'CS 2305',
'CS 2336',
'CS 3162',
'CS 3305',
'CS 3340',
'CS 3345',
'CS 3354',
'CS 3377',
'CS 4141',
'CS 4314',
'CS 4315',
'CS 4334',
'CS 4336',
'CS 4337',
'CS 4341',
'CS 4347',
'CS 4348',
'CS 4349',
'CS 4352',
'CS 4353',
'CS 4361',
'CS 4365',
'CS 4376',
'CS 4384',
'CS 4386',
'CS 4389',
'CS 4390',
'CS 4391',
'CS 4392',
'CS 4393',
'CS 4394',
'CS 4395',
'CS 4396',
'CS 4397',
'CS 4398',
'CS 4399',
'CS 4485',
'CS 4V95',
'CS 4V98',
'ECS 1100',
'ECS 3361',
'ECS 3390',
'EE 4325',
'FILM 2332',
'GEOL 1303',
'GEOL 1304',
'GOVT 2305',
'GOVT 2306',
'HIST 1301',
'HIST 1302',
'HIST 2301',
'HIST 2330',
'HIST 2332',
'HUMA 1301',
'LIT 2331',
'MATH 2413',
'MATH 2414',
'MATH 2417',
'MATH 2418',
'MATH 2419',
'MUSI 1306',
'PHIL 1301',
'PHIL 2316',
'PHIL 2317',
'PHYS 2125',
'PHYS 2126',
'PHYS 2325',
'PHYS 2326',
'RHET 1302',
'SE 4351',
'SE 4352',
'SE 4367',
'SE 4381',
'SE 4485',
'THEA 1310']

guided_electives = ["CS 4314",
                        "CS 4315",
                        "CS 4334",
                        "CS 4336",
                        "CS 4352",
                        "CS 4353",
                        "CS 4361",
                        "CS 4365",
                        "CS 4376",
                        "CS 4386",
                        "CS 4389",
                        "CS 4390",
                        "CS 4391",
                        "CS 4392",
                        "CS 4393",
                        "CS 4394",
                        "CS 4395",
                        "CS 4396",
                        "CS 4397",
                        "CS 4398",
                        "CS 4399",
                        "CS 4V95",
                        "CS 4V98",
                        "EE 4325",
                        "SE 4351",
                        "SE 4352",
                        "SE 4367",
                        "SE 4381",
                        "SE 4485"]

core_curriculum = ["RHET 1302",
                        "ECS 3390",
                        "ECS 3361",
                        "MATH 2413",
                        "MATH 2419",
                        "PHYS 2125",
                        "MATH 2417",
                        "PHYS 2325",
                        "PHYS 2326",
                        "GOVT 2305",
                        "GOVT 2306",
                        "AHST 1303",
                        "AHST 1304",
                        "AHST 2331",
                        "ARTS 1301",
                        "FILM 2332",
                        "MUSI 1306",
                        "THEA 1310",
                        "AMS 2300",
                        "AMS 2341",
                        "HUMA 1301",
                        "LIT 2331",
                        "PHIL 1301",
                        "PHIL 2316",
                        "PHIL 2317",
                        "HIST 1301",
                        "HIST 1302",
                        "HIST 2301",
                        "HIST 2330",
                        "HIST 2332"]

major_prepatory_courses = ["ECS 1100",
                        "CS 1200",
                        "CS 1337",
                        "CS 2305",
                        "CS 2336",
                        "MATH 2413",
                        "MATH 2417",
                        "PHYS 2325",
                        "PHYS 2326",
                        "PHYS 2125",
                        "MATH 2418",
                        "MATH 2414",
                        "MATH 2419",
                        "PHYS 2126",
                        "ARTS 1301",
                        "FILM 2332",
                        "MUSI 1306",
                        "THEA 1310",
                        "AMS 2300",
                        "AMS 2341",
                        "HUMA 1301",
                        "LIT 2331",
                        "PHIL 1301",
                        "PHIL 2316",
                        "PHIL 2317",
                        "HIST 1301",
                        "HIST 1302",
                        "HIST 2301",
                        "HIST 2330",
                        "HIST 2332",
                        "BIOL 1306",
                        "BIOL 1307",
                        "BIOL 1311",
                        "BIOL 1313",
                        "CHEM 1311",
                        "CHEM 1312",
                        "GEOL 1303",
                        "GEOL 1304"
                        ]

major_core_courses = ["CS 3162",
                        "CS 3305",
                        "CS 3340",
                        "CS 3345",
                        "CS 3354",
                        "CS 3377",
                        "ECS 3361",
                        "ECS 3390",
                        "CS 4141",
                        "CS 4337",
                        "CS 4341",
                        "CS 4347",
                        "CS 4348",
                        "CS 4349",
                        "CS 4384",
                        "CS 4485",
                        ]
menu = {}
menu['1']="List of Core Curriculum Classes."
menu['2']="List of mreturnajor_core_courses."
menu['3']="List of major_prepatory_courses"
menu['4']="List of guided_electives"
menu['5']="Input classes for the chosen semester"

while True:
    options=sorted(menu.keys())
    for entry in options:
        print (entry, ":", menu[entry])

    selection=int(input("Please Select:"))
    if selection == 1:
        print('\n'.join(core_curriculum))
    elif selection == 2:
        print('\n'.join(major_core_courses))
    elif selection == 3:
        print('\n'.join(major_prepatory_courses))
    elif selection == 4:
        print('\n'.join(guided_electives))
    elif selection == 5:
        menu = {}
        menu['1'] = "First semester"
        menu['2'] = "Second semester"
        menu['3'] = "Third semester"
        menu['4'] = "Fourth semester"
        menu['5'] = "Fifth semester"
        menu['6'] = "Sixth semester"
        menu['7'] = "Seventh semester"
        menu['8'] = "Eighth semester"
        while True:
            options=menu.keys()
            options=sorted(menu.keys())
            for entry in options:
                print (entry, ":", menu[entry])
            selection=int(input("Please Select:"))
            if selection == 1:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list1  = input_string.split(",")
                    for Class in class_list1:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list1), "credit hours this semester")
            elif selection == 2:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list2  = input_string.split(",")
                    for Class in class_list2:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list2), "credit hours this semester")
            elif selection == 3:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list3  = input_string.split(",")
                    for Class in class_list3:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list3), "credit hours this semester")
            elif selection == 4:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list4  = input_string.split(",")
                    for Class in class_list4:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list4), "credit hours this semester")
            elif selection == 5:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list5 = input_string.split(",")
                    for Class in class_list5:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list5), "credit hours this semester")
            elif selection == 6:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list6  = input_string.split(",")
                    for Class in class_list6:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list6), "credit hours this semester")
            elif selection == 7:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list7  = input_string.split(",")
                    for Class in class_list7:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list7), "credit hours this semester")
            elif selection == 8:
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    class_list8  = input_string.split(",")
                    for Class in class_list8:
                        if not classExists(Class, all_classes):
                            yeah = False
                            print("{} is not a valid class choice for your major".format(Class))
                            break
                    if yeah:
                        break
                print ('You are planning to take' , totalCreditHours(class_list8), "credit hours this semester")
    elif selection == 6:
        print('\n'.join(guided_electives))
    elif selection == 7:
        print('\n'.join(guided_electives))
    else:
        print ("Unknown Option Selected!")
print("Enter the courses you want to take in the first semester: ")
