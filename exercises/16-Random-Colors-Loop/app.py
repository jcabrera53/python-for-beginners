import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")



def get_allStudentColors():
    students_array = []
    for i in range(1,11):
        random_number = random.randint(0,3)
        color = get_color(random_number)
        students_array.append(color)

    return students_array
    #your loop here


print(get_allStudentColors())