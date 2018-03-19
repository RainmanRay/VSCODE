class SchoolMember:

    def __init__(self,name,age):
        self.name = name
        self.age = age

        print('Initialized SchoolMember : {}'.format(self.name))

    def self_intro(self):

        print('This is {} doing its self-introducing at its age {}'.format(self.name,self.age))

class Teacher(SchoolMember):

    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        SchoolMember.self_intro(self)
        self.salary = salary

        print('Teacher {}  at its age {} .'.format(self.name,self.age))           
    
    def self_intro(self):
        print('Teacher {} gets paid {} per month'.format(self.name,self.salary))

class Student(SchoolMember):

    def __init__(self,name,age,fee):
        SchoolMember.__init__(self,name,age)
        self.fee = fee
        print('Initialting student {}'.format(self.name))

    def self_intro(self):
        print('student {} need paid its education fee at {} per year'.format(self.name,self.fee))

t1 = Teacher('ray',28,'3000')       

