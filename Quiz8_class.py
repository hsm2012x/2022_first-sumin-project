class House:
    def __init__(self, location, house_type, deal_type, price, completion_year) :
        self.location = location
        self.house_tpye = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year



    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_tpye, self.deal_type, self.price, self.completion_year))

a1 = House("강남", "아파트", "매매", "10억", "2010년")
a1.show_detail()

