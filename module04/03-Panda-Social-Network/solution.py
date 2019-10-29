class Panda():
    
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

'''
ivo.name() == "Ivo" # True
ivo.email() == "ivo@pandamail.com"  # True
ivo.gender() == "male" # True
ivo.isMale() == True # True
ivo.isFemale() == False # True
'''

ivo = Panda('ivo', 'ivo@pandamail.com', 'male')
print(ivo.name, ivo.email, ivo.gender)