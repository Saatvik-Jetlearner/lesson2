class fruit:

    def __init__(self, shape, color, taste, preference):
        self.shape = shape
        self.color = color
        self.taste = taste
        self.preference = preference

    
    def get_shape(self):
        return self.shape
    
    def set_shape(self, shape):
        self.shape = shape

    def increase_preference(self):
        self.preference += 1

    def showFruit(self):
        print("Hello, I am a fruit with {}, {}, {}, {}".format(self.shape, self.color, self.taste, self.preference))

apple = fruit("red", "sour", "round", 1)
apple.showFruit()

print(apple.get_shape())
apple.set_shape("sphere")
apple.showFruit()

banana = fruit("yellow", "sweet", "cylinder", 2)
banana.showFruit()
banana.increase_preference()
banana.showFruit()