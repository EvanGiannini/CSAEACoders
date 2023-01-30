
#class Student():
    #def __init__(self, student_name, student_contact):
        #self.student_name = student_name
        #self.student_contact = student_contact
        #schedule = []
        #interest_list = []

    #def __str__(self):
        #return f"This student's name is {self.student_name} and their contact is {self.student_contact}"

class Student():
    def __init__(self, student_name, student_contact, schedule, interests):
        self.student_name = student_name
        self.student_contact = student_contact
        self.schedule = schedule
        self.interests = interests

    def __str__(self):
        return f"This student's name is {self.student_name} and their contact is {self.student_contact}. Their classes include {self.schedule} and their interests are {self.interests}"

class Class():
    def __init__(self, class_name, class_topic):
        self.class_name = class_name
        self.class_topic = class_topic

class Student_Class(Class):
    def __init__(self, class_name, class_topic, class_level):
        self.class_level = class_level
        super().__init__(class_name, class_topic)

class Interest():
    def __init__(self, interest_name, interest_topic):
        self.interest_name = interest_name
        self.interest_topic = interest_topic

def compare(schedule1, schedule2, interest1, interest2):
    counter = 0
    x = 0
    for i in schedule1:
        if i.class_name == schedule2[x].class_name:
            if i.class_level == schedule2[x].class_level:
                counter += 1
                x += 1
        else:
            x += 1

    if len(interest1) >= len(interest2):
        for i in interest1:
            for j in interest2:
                if i.interest_name == j.interest_name:
                    counter += 3
        
    if len(interest2) > len(interest1):
        for i in interest2:
            for j in interest1:
                if i.interest_name == j.interest_name:
                    counter += 3

    return counter

def comparePeople(person1, person2):
    counter = 0
    x = 0
    for i in person1.schedule:
        if i.class_name == person2.schedule[x].class_name:
            if i.class_level == person2.schedule[x].class_level:
                counter += 1
                x += 1
        else:
            x += 1

    if len(person1.interests) >= len(person2.interests):
        for i in person1.interests:
            for j in person2.interests:
                if i.interest_name == j.interest_name:
                    counter += 3
        
    if len(person2.interests) > len(person1.interests):
        for i in person2.interests:
            for j in person1.interests:
                if i.interest_name == j.interest_name:
                    counter += 3

    return counter

#testing

class1 = Student_Class("Biology", "Science", "Honors")
class2 = Student_Class("Biology", "Science", "Advanced")
class3 = Student_Class("Chemistry", "Science", "Honors")
class4 = Student_Class("Biology", "Science", "Honors")

in1 = Interest("Lacrosse", "Sports")
in2 = Interest("Basketball" , "Sports")
in3 = Interest("Drawing", "Art")
in4 = Interest("Fishing", "Sports")

schedule11 = []
schedule22 = []

schedule11.extend([class3,class1])
schedule22.extend([class2,class4])

int1 = []
int2 = []

int1.extend([in1,in2])
int2.extend([in4,in3,in2])

student1 = Student("Stacy", "908888888", schedule11, int1)
student2 = Student("Bryan", "907777777", schedule22, int2)

print(student1.student_name)

print(student1)

#rr = compare(schedule11, schedule22, int1, int2)
rr = comparePeople(student1, student2)
print(rr)