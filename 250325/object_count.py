class Hotel:
    count = 0
    def __init__(self):
        Hotel.count+=1
    @classmethod
    def show(cls):
        print(Hotel.count)
p = Hotel()
k = Hotel()

Hotel.show()