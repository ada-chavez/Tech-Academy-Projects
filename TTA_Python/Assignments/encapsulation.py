##Python Version:       3.9.0
##
##Author:               Ada Chavez
##
##Purpose:              Demonstrating the use of encapsulation using private
##                      and protected attribute functions in a class and object


class User:
        def __init__(self, name, email, password, ssn):
            self.name = 'unknown'
            self.email = 'unknown'
            self._password = 'password' #protected
            self.__ssn = '111-11-1111' #private

        def getPassword(self):
            print("Name: {} \nEmail: {} \nPassword: {} \nSSN: {}".format(self.name,self.email,self._password,self.__ssn))

        def setPassword(self, private):
            self._password = private


# object that makes use of a protected attribute
user_1 = User('','','','')
user_1.setPassword('ilovecats321')
user_1.getPassword()





