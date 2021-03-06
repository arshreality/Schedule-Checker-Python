import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

input_class_list1 = []
input_class_list2 = []
input_class_list3 = []
input_class_list4 = []
input_class_list5 = []
input_class_list6 = []
input_class_list7 = []
input_class_list8 = []
input_class_list9 = []
input_class_list10 = []
input_class_list11 = []
input_class_list0 = []

output_class_list1 = []
output_class_list2 = []
output_class_list3 = []
output_class_list4 = []
output_class_list5 = []
output_class_list6 = []
output_class_list7 = []
output_class_list8 = []
output_class_list9 = []
output_class_list10 = []
output_class_list11 = []
output_class_list0 = []

free_elective = []
current_classes = []

free_electives_total = 11
guided_electives_total = 9
core_curriculum_total = 42
major_prepatory_courses_total = 20
major_core_courses_total = 42
total_credits_needed_to_graduate = 124

free_electives_count = 0
guided_electives_count = 0
core_curriculum_count = 0
major_prepatory_courses_count = 0
major_core_courses_count = 0


def findPoint(Class):
  numX,numY = 0,0
  if Class in output_class_list0:
        numX = 0
        numY = output_class_list0.index(Class) + 1
  elif Class in output_class_list1:
        numX = 1
        numY = output_class_list1.index(Class) + 1
  elif Class in output_class_list2:
        numX = 2
        numY = output_class_list2.index(Class) + 1
  elif Class in output_class_list3:
        numX = 3
        numY = output_class_list3.index(Class) + 1
  elif Class in output_class_list4:
        numX = 4
        numY = output_class_list4.index(Class) + 1
  elif Class in output_class_list5:
        numX = 5
        numY = output_class_list5.index(Class) + 1
  elif Class in output_class_list6:
        numX = 6
        numY = output_class_list6.index(Class) + 1
  elif Class in output_class_list7:
        numX = 7
        numY = output_class_list7.index(Class) + 1
  elif Class in output_class_list8:
        numX = 8
        numY = output_class_list8.index(Class) + 1
  elif Class in output_class_list9:
        numX = 9
        numY = output_class_list9.index(Class) + 1
  elif Class in output_class_list10:
        numX = 10
        numY = output_class_list10.index(Class) + 1
  elif Class in output_class_list11:
        numX = 11
        numY = output_class_list11.index(Class) + 1
  else:
        numX = None
        numY = None
  return numX, numY

def totalCreditHours(input_class_list):
    credit = 0
    for s in input_class_list:
        l = list(s)
        for i in range(len(l)):
            if l[i] == ' ':
                credit = credit + int(l[i+2])
    return credit

def classExists(Class, input_class_list):
    yeah = False
    for element in input_class_list:
        if Class.lower() == element.lower():
            yeah = True
            break
    return yeah

def Credit(Class):
    credit = 0
    for i in range(len(Class)):
        l = list(Class)
        if l[i] == ' ':
            credit = int(l[i+2])
    return credit

def KindOfClass(Class):
    global free_electives_count
    global guided_electives_count
    global core_curriculum_count
    global major_prepatory_courses_count
    global major_core_courses_count

    if classExists(Class, guided_electives):
      guided_electives_count += Credit(Class)
    if classExists(Class, core_curriculum):
      core_curriculum_count += Credit(Class)
    if classExists(Class, major_prepatory_courses):
      major_prepatory_courses_count += Credit(Class)
    if classExists(Class, major_core_courses):
      major_core_courses_count += Credit(Class)

def CheckClass():
    if free_electives_count >= free_electives_total:
      print("You have reached the maximum number of free elective credits")
    if guided_electives_count >= guided_electives_total:
      print("You have reached the maximum number of guided elective credits")
    if core_curriculum_count >= core_curriculum_total:
      print("You have reached the maximum number of core curriculum credits")
    if major_prepatory_courses_count >= major_prepatory_courses_total:
      print("You have reached the maximum number of major prepatory credits")
    if major_core_courses_count >= major_core_courses_total:
      print("You have reached the maximum number of major core credits")
    if free_electives_count + guided_electives_count + core_curriculum_count + major_prepatory_courses_count + major_core_courses_count >= total_credits_needed_to_graduate:
      print("You are ready to graduate lmao leave")

def CheckClassFormat(Class):
    s= list(Class)
    for i in range(len(s)):
      if s[i] == ' ':
        if (s[i+1].isdigit() and s[i+2].isdigit() and s[i+3].isdigit() and s[i+4].isdigit() and s[0].isalpha() and s[1].isalpha() and s[i-1].isalpha() and s[i-2].isalpha()):
          return True
        else:
          return False

def CheckIfClassTakenPreviously(Class):
  if Class in current_classes:
    return True

def PreReq(Class):
  if Class == 'CS 1337':
    if CheckIfClassTakenPreviously('CS 1336') and CheckIfClassTakenPreviously('CS 1136'):
      return True
    else:
      print('You must take CS 1336 and CS 1136 before {}'.format(Class))
      return False

  elif Class == 'CS 2336':
    if CheckIfClassTakenPreviously('CS 1337') and CheckIfClassTakenPreviously('CS 2305'):
      return True
    else:
      print('You must take CS 1337 before {} and CS 2305 along/before {}'.format(Class))
      return False

  elif Class == 'MATH 2414':
    if CheckIfClassTakenPreviously('MATH 2413'):
      return True
    else:
      print('You must take MATH 2413 before {}'.format(Class))
      return False

  elif Class == 'MATH 2419':
    if CheckIfClassTakenPreviously('MATH 2417'):
      return True
    else:
      print('You must take MATH 2417 before {}'.format(Class))
      return False

  elif Class == 'PHYS 2325' or Class == 'PHYS 2125':
    if (CheckIfClassTakenPreviously('MATH 2413') or CheckIfClassTakenPreviously('MATH 2417')) and (CheckIfClassTakenPreviously('MATH 2414') or CheckIfClassTakenPreviously('MATH 2419')):
      return True
    else:
      print('You must take MATH 2413 or MATH 2417 before {} and you must take MATH 2414 or MATH 2419 concurrently'.format(Class))
      return False

  elif Class == 'PHYS 2326' or Class == 'PHYS 2126':
    if (CheckIfClassTakenPreviously('MATH 2414') or CheckIfClassTakenPreviously('MATH 2419')) and (CheckIfClassTakenPreviously('PHYS 2325') and CheckIfClassTakenPreviously('PHYS 2125')):
      return True
    else:
      print('You must take MATH 2414 or MATH 2419 and PHYS 2325 and PHYS 2125 before {}'.format(Class))
      return False

  elif Class == 'CS 3305':
    if (CheckIfClassTakenPreviously('MATH 2414') or CheckIfClassTakenPreviously('MATH 2419')) and CheckIfClassTakenPreviously('CS 2305'):
      return True
    else:
      print('You must take MATH 2414 or MATH 2419 and CS 2305 before {}'.format(Class))
      return False

  elif Class == 'CS 3340':
    if CheckIfClassTakenPreviously('CS 1337') and CheckIfClassTakenPreviously('CS 2305'):
      return True
    else:
      print('You must take CS 1337 and CS 2305 before {}'.format(Class))
      return False

  elif Class == 'MATH 2418':
    if CheckIfClassTakenPreviously('MATH 2417') or CheckIfClassTakenPreviously('MATH 2413'):
      return True
    else:
      print('You must take MATH 2414 or MATH 2419 before {}'.format(Class))
      return False

  elif Class == 'CS 3341':
    if (CheckIfClassTakenPreviously('MATH 2417') or CheckIfClassTakenPreviously('MATH 2413')) and CheckIfClassTakenPreviously('CS 2305'):
      return True
    else:
      print('You must take MATH 2414 or MATH 2419 and CS 2305 before {} and CS 3345 along/before {}'.format(Class))
      return False

  elif Class == 'CS 3345':
    if CheckIfClassTakenPreviously('CS 2305') and CheckIfClassTakenPreviously('CS 2336'):
      return True
    else:
      print('You must take CS 2305 and CS 2336 before {}'.format(Class))
      return False
    print("You must take CS 3341 concurrently")

  elif Class == 'CS 3377':
    if CheckIfClassTakenPreviously('CS 2336'):
      return True
    else:
      print('You must take CS 2336 before {}'.format(Class))
      return False

  elif Class == 'CS 4341' or Class == 'CS 4141':
    if CheckIfClassTakenPreviously('CS 3340') and CheckIfClassTakenPreviously('PHYS 2325'):
      return True
    else:
      print('You must take CS 3340 and PHYS 2325 before {}'.format(Class))
      return False

  elif Class == 'CS 4337':
    if CheckIfClassTakenPreviously('CS 3340') and CheckIfClassTakenPreviously('CS 2305') and CheckIfClassTakenPreviously('CS 2336'):
      return True
    else:
      print('You must take CS 3340 and CS 2305 and CS 2336 before {}'.format(Class))
      return False

  elif Class == 'CS 3354':
    if CheckIfClassTakenPreviously('CS 2305') and CheckIfClassTakenPreviously('CS 2336') and CheckIfClassTakenPreviously('ECS 3390'):
      return True
    else:
      print('You must take CS 2305 and CS 2336 before {} and ECS 3390 along/bebefore {}'.format(Class))
      return False

  elif Class == 'ECS 3390':
    if CheckIfClassTakenPreviously('RHET 1302') and totalCreditHours(current_classes) >= 54:
      return True
    else:
      print('You must take RHET 1302 before {} and be in junior-standing'.format(Class))
      return False

  elif Class == 'CS 4349':
    if CheckIfClassTakenPreviously('CS 3305') and CheckIfClassTakenPreviously('CS 3345'):
      return True
    else:
      print('You must take CS 3305 and CS 3345 before {}'.format(Class))
      return False

  elif Class == 'CS 3162':
    if CheckIfClassTakenPreviously('CS 3345') and CheckIfClassTakenPreviously('CS 3354') and CheckIfClassTakenPreviously('ECS 3361'):
        return True
    else:
        print('You must take CS 3354 and CS 3345 and ECS 3361 with {}'.format(Class))
        return False

  elif Class == 'CS 4348':
    if CheckIfClassTakenPreviously('CS 3340') and CheckIfClassTakenPreviously('CS 3345') and CheckIfClassTakenPreviously('CS 3377'):
      return True
    else:
      print('You must take CS 3340 and CS 3345 and CS 3377 before {}'.format(Class))
      return False

  elif Class == 'ECS 3361':
    if totalCreditHours(current_classes) >= 54:
      return True
    else:
      return False
      print('You must be a junior to take this')

  elif Class == 'CS 4384':
    if CheckIfClassTakenPreviously('CS 3305'):
      return True
    else:
      print('You must take CS 3305 before {}'.format(Class))
      return False

  elif Class == 'CS 4347':
    if CheckIfClassTakenPreviously('CS 3345'):
      return True
    else:
      print('You must take CS 3345 before {}'.format(Class))
      return False

  elif Class == 'CS 4485':
    if CheckIfClassTakenPreviously('CS 3345') and CheckIfClassTakenPreviously('CS 3354'):
      return True
    else:
      print('You must take CS 3345 and CS 3354 before {}'.format(Class))
      return False

  else:
    return True

def zzz(Class):
    global current_classes
    global free_electives_count
    global all_classes

    KindOfClass(Class)
    if not classExists(Class, all_classes):
        print("{} is not in the list of courses for your major. Would you like it to be a free elective?".format(Class))
        FE = input()
        if(FE.lower() == 'yes'):
          free_elective.append(Class)
          yeah = True
          free_electives_count += Credit(Class)
        else:
          print("You can enter a different class in that case")
          yeah = False
          return

def connectpoints(x1,y1,x2,y2):
    plt.plot([x1,x2],[y1,y2],'y-')
    plt.plot([x1],[y1],'ro',markersize=3)
    plt.plot([x2],[y2],'ro',markersize=3)
    plt.title('Customized Flowchart for CS major')

def connect():
  for lists in output_class_list:
    for Class in lists:
      if Class == 'CS 1337':
        connectpoints(*findPoint('CS 1336'),*findPoint(Class))
        connectpoints(*findPoint('CS 1136'),*findPoint(Class))
      elif Class == 'MATH 2419':
        connectpoints(*findPoint('MATH 2417'),*findPoint(Class))
      elif Class == 'MATH 2414':
        connectpoints(*findPoint('MATH 2413'),*findPoint(Class))
      elif Class == 'PHYS 2325':
        connectpoints(*findPoint('MATH 2413'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2417'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2414'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2419'),*findPoint(Class))
      elif Class == 'PHYS 2125':
        connectpoints(*findPoint('MATH 2413'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2417'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2414'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2419'),*findPoint(Class))
      elif Class == 'CS 2336':
        connectpoints(*findPoint('CS 1337'),*findPoint(Class))
      elif Class == 'PHYS 2326':
        connectpoints(*findPoint('PHYS 2325'),*findPoint(Class))
        connectpoints(*findPoint('PHYS 2125'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2414'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2419'),*findPoint(Class))
      elif Class == 'PHYS 2126':
        connectpoints(*findPoint('PHYS 2325'),*findPoint(Class))
        connectpoints(*findPoint('PHYS 2125'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2414'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2419'),*findPoint(Class))
      elif Class == 'CS 3305':
        connectpoints(*findPoint('CS 2305'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2419'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2414'),*findPoint(Class))
      elif Class == 'CS 3340':
        connectpoints(*findPoint('CS 2305'),*findPoint(Class))
        connectpoints(*findPoint('CS 1337'),*findPoint(Class))
      elif Class == 'MATH 2418':
        connectpoints(*findPoint('MATH 2417'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2413'),*findPoint(Class))
      elif Class == 'CS 3341':
        connectpoints(*findPoint('CS 2305'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2419'),*findPoint(Class))
        connectpoints(*findPoint('MATH 2414'),*findPoint(Class))
      elif Class == 'CS 3345':
        connectpoints(*findPoint('CS 2305'),*findPoint(Class))
        connectpoints(*findPoint('CS 2336'),*findPoint(Class))
      elif Class == 'CS 3377':
        connectpoints(*findPoint('CS 2336'),*findPoint(Class))
      elif Class == 'CS 4341':
        connectpoints(*findPoint('PHYS 2326'),*findPoint(Class))
        connectpoints(*findPoint('PHYS 2126'),*findPoint(Class))
        connectpoints(*findPoint('CS 3340'),*findPoint(Class))
      elif Class == 'CS 4141':
        connectpoints(*findPoint('PHYS 2326'),*findPoint(Class))
        connectpoints(*findPoint('PHYS 2126'),*findPoint(Class))
        connectpoints(*findPoint('CS 3340'),*findPoint(Class))
      elif Class == 'CS 4337':
        connectpoints(*findPoint('CS 2305'),*findPoint(Class))
        connectpoints(*findPoint('CS 2336'),*findPoint(Class))
        connectpoints(*findPoint('CS 3340'),*findPoint(Class))
      elif Class == 'CS 3354':
        connectpoints(*findPoint('CS 2305'),*findPoint(Class))
        connectpoints(*findPoint('CS 2336'),*findPoint(Class))
        connectpoints(*findPoint('ECS 3390'),*findPoint(Class))
      elif Class == 'ECS 3390':
        connectpoints(*findPoint('RHET 1302'),*findPoint(Class))
      elif Class == 'CS 4349':
        connectpoints(*findPoint('CS 3305'),*findPoint(Class))
        connectpoints(*findPoint('CS 3345'),*findPoint(Class))
      elif Class == 'CS 4341':
        connectpoints(*findPoint('PHYS 2326'),*findPoint(Class))
        connectpoints(*findPoint('PHYS 2126'),*findPoint(Class))
        connectpoints(*findPoint('CS 3340'),*findPoint(Class))
      elif Class == 'CS 3162':
        connectpoints(*findPoint('CS 3345'),*findPoint(Class))
        connectpoints(*findPoint('CS 3354'),*findPoint(Class))
        connectpoints(*findPoint('ECS 3361'),*findPoint(Class))
      elif Class == 'CS 4348':
        connectpoints(*findPoint('CS 3345'),*findPoint(Class))
        connectpoints(*findPoint('CS 3377'),*findPoint(Class))
        connectpoints(*findPoint('CS 3340'),*findPoint(Class))
      elif Class == 'CS 4384':
        connectpoints(*findPoint('CS 3305'),*findPoint(Class))
      elif Class == 'CS 4347':
        connectpoints(*findPoint('CS 3345'),*findPoint(Class))
      elif Class == 'CS 4485':
        connectpoints(*findPoint('CS 3354'),*findPoint(Class))
        connectpoints(*findPoint('CS 3345'),*findPoint(Class))

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
'CS 1336',
'CS 1136',
'CS 1337',
'CS 2305',
'CS 2336',
'CS 3162',
'CS 3305',
'CS 3340',
'CS 3341',
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
                        "CS 3341",
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

not_degree_plan_courses = ["CS 1336",
"CS 1136",
"ITS"]



while True:
    menu1 = {}
    menu1['1']="See list of Core Curriculum Courses"
    menu1['2']="See list of Major Core Courses"
    menu1['3']="See list of Major Prepatory Courses"
    menu1['4']="See list of Guided Electives"
    menu1['5']="Input classes"
    menu1['6']="Obtain final flowchart"

    print("\n")
    options=sorted(menu1.keys())
    for entry in options:
        print (entry, ":", menu1[entry])

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

        while True:
            menu2 = {}
            menu2['AP'] = "AP Credit"
            menu2['F1'] = "First fall semester"
            menu2['S1'] = "First spring semester"
            menu2['T1'] = "First summer semester"
            menu2['F2'] = "Second fall semester"
            menu2['S2'] = "Second spring semester"
            menu2['T2'] = "Second summer semester"
            menu2['F3'] = "Third fall semester"
            menu2['S3'] = "Third spring semester"
            menu2['T3'] = "Third summer semester"
            menu2['F4'] = "Fourth fall semester"
            menu2['S4'] = "Fourth spring semester"
            menu2['Menu'] = "Menu"

            options=menu2.keys()
            for entry in options:
                print (entry, ":", menu2[entry])
            selection2 = input("Please Select:")

            if selection2.lower() == 'ap':
                while True:
                    yeah = True
                    input_string = input("Enter classes you received AP or other credit separated by comma: ")
                    input_class_list0  = input_string.split(",")
                    for Class in input_class_list0:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list0.append(Class)
                            output_class_list0 = list(set(output_class_list0))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list0)
                print ('You are planning to bring in' , totalCreditHours(output_class_list0), "credit hours")
                CheckClass()

            elif selection2.lower() == 'f1':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list1.extend(input_string.split(","))
                    for Class in input_class_list1:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list1.append(Class)
                            output_class_list1 = list(set(output_class_list1))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list1)
                print ('You are planning to take' , totalCreditHours(output_class_list1), "credit hours in your first fall semester")
                CheckClass()

            elif selection2.lower() == 's1':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list2  = input_string.split(",")
                    for Class in input_class_list2:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list2.append(Class)
                            output_class_list2 = list(set(output_class_list2))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list2)
                print ('You are planning to take' , totalCreditHours(output_class_list2), "credit hours in your second fall semester")
                CheckClass()

            elif selection2.lower() == 't1':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list3  = input_string.split(",")
                    for Class in input_class_list3:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list3.append(Class)
                            output_class_list3 = list(set(output_class_list3))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list3)
                print ('You are planning to take' , totalCreditHours(output_class_list3), "credit hours in your first summer semester")

            elif selection2.lower() == 'f2':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list4  = input_string.split(",")
                    for Class in input_class_list4:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list4.append(Class)
                            output_class_list4 = list(set(output_class_list4))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list4)
                print ('You are planning to take' , totalCreditHours(output_class_list4), "credit hours in your third fall semester")
                CheckClass()

            elif selection2.lower() == 's2':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list5  = input_string.split(",")
                    for Class in input_class_list5:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list5.append(Class)
                            output_class_list5 = list(set(output_class_list5))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list5)
                print ('You are planning to take' , totalCreditHours(output_class_list5), "credit hours in your fourth fall semester")
                CheckClass()

            elif selection2.lower() == 't2':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list6  = input_string.split(",")
                    for Class in input_class_list6:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list6.append(Class)
                            output_class_list6 = list(set(output_class_list6))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list6)
                print ('You are planning to take' , totalCreditHours(output_class_list6), "credit hours in your second summer semester")
                CheckClass()

            elif selection2.lower() == 'f3':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list7 = input_string.split(",")
                    for Class in input_class_list7:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list7.append(Class)
                            output_class_list7 = list(set(output_class_list7))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list7)
                print ('You are planning to take' , totalCreditHours(output_class_list7), "credit hours in your first spring semester")
                CheckClass()

            elif selection2.lower() == 's3':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list8  = input_string.split(",")
                    for Class in input_class_list8:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list8.append(Class)
                            output_class_list8 = list(set(output_class_list8))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list8)
                print ('You are planning to take' , totalCreditHours(output_class_list8), "credit hours in your second spring semester")
                CheckClass()

            elif selection2.lower() == 't3':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list9  = input_string.split(",")
                    for Class in input_class_list9:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list9.append(Class)
                            output_class_list9 = list(set(output_class_list9))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list9)
                print ('You are planning to take' , totalCreditHours(output_class_list9), "credit hours in your third summer semester")
                CheckClass()

            elif selection2.lower() == 'f4':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list10  = input_string.split(",")
                    for Class in input_class_list10:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list10.append(Class)
                            output_class_list10 = list(set(output_class_list10))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list10)
                print ('You are planning to take' , totalCreditHours(output_class_list10), "credit hours in your third spring semester")
                CheckClass()

            elif selection2.lower() == 's4':
                while True:
                    yeah = True
                    input_string = input("Enter classes separated by comma: ")
                    input_class_list11  = input_string.split(",")
                    for Class in input_class_list11:
                        if CheckClassFormat(Class):
                          if PreReq(Class):
                            current_classes.append(Class)
                            current_classes = list(set(current_classes))
                            output_class_list11.append(Class)
                            output_class_list11 = list(set(output_class_list11))
                            zzz(Class)
                        else:
                            print("Try again. The class entered has a wrong format.")
                    if yeah:
                        break
                print('Courses for this semester: ', current_classes)
                print('Courses for this semester: ', output_class_list11)
                print ('You are planning to take' , totalCreditHours(output_class_list11), "credit hours in your fourth spring semester")
                CheckClass()



            elif selection2.lower() =='menu':
                break

            else:
                print ("Unknown Option Selected! Try again.\n")

    elif selection == 6:

        year = int(input('Enter year of admission: 20'))
        output_class_list0 = sorted(output_class_list0)
        output_class_list1 = sorted(output_class_list1)
        output_class_list2 = sorted(output_class_list2)
        output_class_list3 = sorted(output_class_list3)
        output_class_list4 = sorted(output_class_list4)
        output_class_list5 = sorted(output_class_list5)
        output_class_list6 = sorted(output_class_list6)
        output_class_list7 = sorted(output_class_list7)
        output_class_list8 = sorted(output_class_list8)
        output_class_list9 = sorted(output_class_list9)
        output_class_list10 = sorted(output_class_list10)
        output_class_list11 = sorted(output_class_list11)
        output_class_list0 = sorted(output_class_list0)

        x0=[0]*8
        x1=[1]*8
        x2=[2]*8
        x3=[3]*8
        x4=[4]*8
        x5=[5]*8
        x6=[6]*8
        x7=[7]*8
        x8=[8]*8
        x9=[9]*8
        x10=[10]*8
        x11=[11]*8

        y=[1, 2, 3, 4, 5, 6, 7, 8]

        x = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

        plt.subplots(figsize=(20,10))

        # output_class_list1 = ['CS 1336', 'CS 1136','MATH 2417','ECS 1100']
        # output_class_list2 = ['CS 1337', 'MATH 2419','MATH 2418','CS 2305','RHET 1302']
        # output_class_list4 = ['CS 2336', 'PHYS 2325','PHYS 2125']
        # output_class_list = [output_class_list1,output_class_list2,output_class_list4]

        output_class_list = [output_class_list0,output_class_list1,output_class_list2,output_class_list3,output_class_list4, output_class_list5, output_class_list6, output_class_list7, output_class_list8, output_class_list9, output_class_list10, output_class_list11]

        ax = sns.scatterplot(x0[:len(output_class_list0)], y[:len(output_class_list0)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x1[:len(output_class_list1)], y[:len(output_class_list1)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x2[:len(output_class_list2)], y[:len(output_class_list2)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x3[:len(output_class_list3)], y[:len(output_class_list3)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x4[:len(output_class_list4)], y[:len(output_class_list4)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x5[:len(output_class_list5)], y[:len(output_class_list5)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x6[:len(output_class_list6)], y[:len(output_class_list6)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x7[:len(output_class_list7)], y[:len(output_class_list7)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x8[:len(output_class_list8)], y[:len(output_class_list8)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x9[:len(output_class_list9)], y[:len(output_class_list9)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x10[:len(output_class_list10)], y[:len(output_class_list10)], alpha = 0.5,s = 2500)
        ax = sns.scatterplot(x11[:len(output_class_list11)], y[:len(output_class_list11)], alpha = 0.5,s = 2500)

        for line in range(len(output_class_list0)):
             ax.text(x0[line], y[line], output_class_list0[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list1)):
             ax.text(x1[line], y[line], output_class_list1[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list2)):
             ax.text(x2[line], y[line], output_class_list2[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list3)):
             ax.text(x3[line], y[line], output_class_list3[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list4)):
             ax.text(x4[line], y[line], output_class_list4[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list5)):
             ax.text(x5[line], y[line], output_class_list5[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list6)):
             ax.text(x6[line], y[line], output_class_list6[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list7)):
             ax.text(x7[line], y[line], output_class_list7[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list8)):
             ax.text(x8[line], y[line], output_class_list8[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list9)):
             ax.text(x9[line], y[line], output_class_list9[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list10)):
             ax.text(x10[line], y[line], output_class_list10[line], horizontalalignment='center', size='small', color='black', weight='semibold')
        for line in range(len(output_class_list11)):
             ax.text(x11[line], y[line], output_class_list11[line], horizontalalignment='center', size='small', color='black', weight='semibold')

        ax.set(xlim=(-1, 10))
        ax.set(ylim=(0, 10))

        connect()
        plt.xticks([])
        plt.yticks([])
        labels = ["AP Credit","Fall '{}".format(year),"Spring '{}".format(year+1),"Summer '{}".format(year+1),"Fall '{}".format(year+1),"Spring '{}".format(year+2),"Summer '{}".format(year+2),"Fall '{}".format(year+2),"Spring '{}".format(year+3),"Summer '{}".format(year+3),"Fall '{}".format(year+3),"Spring '{}".format(year+4)]
        plt.xticks(np.arange(0,13,1), labels)
        plt.show()


    else:
        print ("Unknown Option Selected!")
