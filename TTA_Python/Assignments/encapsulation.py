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
                print("Name: {} \nEmail: {} \nPassword: {} \nSSN: {}\n".format(self.name,self.email,self._password,self.__ssn))

        def setPassword(self, protected):
                self._password = protected

        def getSsn(self):
                print("Name: {} \nEmail: {} \nPassword: {} \nSSN: {}".format(self.name,self.email,self._password,self.__ssn))

        def setSsn(self,private):
                self.__ssn = private

# object that makes use of a protected attribute
user_1 = User('','','','')
user_1.setPassword('ilovecats321')
user_1.getPassword()

# object that makes use of a private attribute
user_2 = User('','','','')
user_2.setSsn('123-11-1231')
user_2.getSsn()







