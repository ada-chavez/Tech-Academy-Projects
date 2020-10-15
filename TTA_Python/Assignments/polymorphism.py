##      Polymorphism Assignment
##
##      Two classes that inherit from another class
##      Each child has two attributes
##      The parent class has one method
##      Both child classes utilize polymorphism on the parent class method

# Parent class
class Shopping:
    Name = "Ikea"
    Location = "Portland,OR"

    def information(self):
        msg = "\nStore Name: {} \nLocation: {}".format(self.Name,self.Location)
        print(msg)
    

# Child Class
class Online(Shopping):
    Name = "Amazon"
    Location = "Online"
    Website = "www.amazon.com"
    User_Login = "JohnDoe@gmail.com"

    def information(self):
        msg = "\nStore Name: {} \nLocation: {} \nWebsite: {} \nUser Name: {}".format(self.Name,self.Location,self.Website,self.User_Login)
        print(msg)
        

# Child Class
class Physical_Store(Shopping):
    Name = "Costco"
    Location = "Tigard,OR"
    Address = "7850 SW Dartmouth St"
    Membership_Num = 343254

    def information(self):
        msg = "\nStore Name: {} \nLocation: {} \nAddress: {} \nMembership #: {}".format(self.Name,self.Location,self.Address,self.Membership_Num)
        print(msg)





if __name__ == "__main__":
    shopping = Shopping()
    shopping.information()

    online = Online()
    online.information()

    store = Physical_Store()
    store.information()
    
