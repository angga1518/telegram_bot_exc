class Responses():
    list_amount=[]
    list_price=[]
    market_price=0.0
    quantity=0.0
    tax=0.0

    return_message="type following command to fill required data:\n/marketprice : input market price\n/quantity : input quantity \n/tax : input your current tax \n\nor /result : to get your profit result"
    add_more_message="do you want to add more item? (y/n)"

    def reset_message(self):
        self.list_amount.clear()
        self.list_price.clear()
        self.market_price = 0.0
        self.quantity = 0.0
        self.tax = 0.0

    def get_result(self):
        if (len(self.list_amount)==0):
            return "Please enter your item first\namount-price"
        if (self.market_price==0.0):
            return "Please enter market price for the item like this:\nmp-price \nfor example mp-3000"
        if (self.quantity==0.0):
            return "please enter quantity you want to sell like this:\nq-quantity \nfor example q-100"
        if (self.tax==0.0):
            return "please enter your current tax like this:\nt-tax\nfor example t-0.25"   
        modal_satuan = 0.0
        for i in range(len(self.list_price)):
            modal_satuan += self.list_price[i] * self.list_amount[i]
        modal_total = modal_satuan*self.quantity
        revenue = self.market_price * self.quantity
        tax_price = self.tax * revenue
        result = revenue-tax_price-modal_total
        return result

    def get_response(self, message):
        fw = message.split("-")[0]
        if (not fw.isnumeric()):
            fw = fw.lower()
            if (fw=="n"):
                return self.return_message
            elif (fw=="y"):
                return 'Please input your item amount and price like this:\namount-price'

            try:
                sw = float(message.split("-")[1])
                if (fw=="mp"):
                    self.market_price=sw
                    return self.return_message
                elif (fw=="q"):
                    self.quantity=sw
                    return self.return_message
                elif (fw=="t"):
                    self.tax=sw
                    return self.return_message
                else:
                    return "Sorry, I dont understand that"
            except:
                return "Sorry, I dont understand that"

        try:
            sw = float(message.split("-")[1])
            amount = float(fw)
            price = sw
            self.list_amount.append(amount)
            self.list_price.append(price)

            return self.add_more_message
        except:
            return "Sorry, I dont understand that"
