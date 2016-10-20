class Item():
    def __init__(self):
            name = self.item_chooser()
            self.name = name       

    def item_chooser(self):
        items = ['wine bottle', 'hat']
        return items[random.randint(-1,len(items)-1)]
        
    def __str__(self):
        return self.name
    
    import random