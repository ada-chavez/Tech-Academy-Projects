##
## Creating two classes that inherit from another class
##
##

class home_furnishings:
    item_name = 'No name provided'
    sku_number = 0
    aisle = None
    price = 0

    def information(self):
        msg = "\nItem Name: {}, \nSKU #: {},\nAisle: {},\nPrice: ${}".format(self.item_name,self.sku_number,self.aisle,self.price)
        return msg
    


class bedroom(home_furnishings):
    item_name = 'Vegan Comforter'
    sku_number = 98801023
    aisle = '34'
    price = 100    
    comforter_filing = 'synthetic down'
    bedframe_height = '24 inches'

    def veganDown(self):
        msg = "\nHeavy down comforter that is completely vegan."
        return msg

class kitchen(home_furnishings):
    item_name = 'Marble counter top'
    sku_number = 98805792
    aisle = '12'
    price = 300  
    counter_material = 'marble'
    sink_material = 'stainless steel'

    def marbleCounter(self):
        msg = "\nLook fancy and expensive with a marble counter top."
        return msg

if __name__ == "__main__":
    bedroom = bedroom()
    print(bedroom.information())
    print(bedroom.veganDown())

    kitchen = kitchen()
    print(kitchen.information())
    print(kitchen.marbleCounter())
    
    
    
    
    
    
    
