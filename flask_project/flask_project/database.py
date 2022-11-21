import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
            
            firebase = pyrebase.initialize_app(config)
            self.db = firebase.database()
            
    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:#if res.name() == name:
              return False
        return True
            
    def insert_restaurant(self, name, data, image_path):
        restaurant_info = {
            "location": data['location'],
            "phone": data['phone'],
            "category": data['category'],
            "park": data['park'],
            "reserve": data['reserve'],
            "monToSun": data['monToSun'],
            "open": data['open'],
            "close": data['close'],
            "image_path": image_path
        }
        
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,image_path)
            return True
        else:
            return False
        

    