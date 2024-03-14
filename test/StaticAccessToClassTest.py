class VAT:
    vat_rate = 15

    # This function can be used statically. No 'self' is being
    # passed  through
    def static_get_vat_price(price):
        return price * (1.0 + VAT.vat_rate/100)
    
    # This function cannot be used statically, as it is reliant on self, and
    # self only exist when the object gets created
    def get_vat_price(self, price):
        return price * (1.0 + VAT.vat_rate/100)
    

# No object created
print(VAT.vat_rate)
print(VAT.static_get_vat_price(50)) # Static

# Won't work until object created. Error: paramater does not exit
# print(VAT.get_vat_price(50))    
# Fix it
print(VAT().get_vat_price(50))