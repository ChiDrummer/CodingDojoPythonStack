"""With the given list, unpack the keys and values in order"""

"""def studentNames(student_list):
    for key in student_list:
        print key["first_name"], key["last_name"]


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
studentNames(students)"""

"""now add a second list AND sum all characters"""

def stu_inst(new_list):
    count = 0
    for i in users:
        print i
        for key in users[i]:
            count += 1
            letters = len(key['first_name']) + len(key["last_name"])
            print count, "-", key["first_name"].upper(), key["last_name"].upper(), "-", letters

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
stu_inst(users)

