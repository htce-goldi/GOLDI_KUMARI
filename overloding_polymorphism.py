class Order:
    def place_order_1(self, item1):
        print("order placed for:- ")
        print(f"- {item1}")

    def place_order_2(self, item1, item2):
        print("order placed for:- ")
        print(f"- {item1}")
        print(f"- {item2}")

    def place_order_3(self, item1, item2, item3):
        print("order placed for:- ")
        print(f"- {item1}")
        print(f"- {item2}")
        print(f"- {item3}")
order = Order()
order.place_order_1("burger")                         
order.place_order_2("pizza", "pasta")                  
order.place_order_3("pizza", "pasta", "juice")        
