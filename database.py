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
        
    
    # 메인메뉴 데이터베이스 함수
    def insert_mainmenu(self, menu_name, data, image_path):
        mainmenu_info={
            "menu_name": data['menu_name'],
            "menu_price": data['menu_price'],
            "image_path": image_path       
        }
        if self.restaurant_duplicate_check(menu_name):
            self.db.child("mainmenu").child(menu_name).set(mainmenu_info)
            print(data,image_path)
            return True
        else:
            return False

    #리뷰 데이터베이스 함수
    def insert_review(self, write, data):
        review_info={
            "year": data['year'],
            "month": data['month'],
            "date": data['day'],
            "star": data['star'],
            "write": data['write']
        }
        if self.restaurant_duplicate_check(write):
            self.db.child("review").child(write).set(review_info)
            print(data)
            return True
        else:
            return False
        self.db.child("review").child(name).set(review_info)
        print(data)
        return True



    