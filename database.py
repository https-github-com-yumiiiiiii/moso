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
            value = res.val()
            
            if value['name'] == name:
                return False
            
            return True
    
    def mainmenu_duplicate_check(self, menu_name):
        mainmenus = self.db.child("mainmenu").get()
        
        for menu in mainmenus.each():
            value = menu.val()
            
            if value['menu_name'] == menu_name:
                return False
            return True
            
    def insert_restaurant(self, name, data, image_path):
        restaurant_info = {
            "name": name,
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
            #self.db.child("restaurant").child(name).set(restaurant_info)
            self.db.child("restaurant").push(restaurant_info)
            print(data,image_path)
            return True
        else:
            return False
        
    
    # 메인메뉴 데이터베이스 함수
    def insert_mainmenu(self, menu_name, data, image_path):
        mainmenu_info={
            "restaurant_name": data['restaurant_name'],
            "menu_name": data['menu_name'],
            "menu_price": data['menu_price'],
            "image_path": image_path       
        }
        if self.mainmenu_duplicate_check(menu_name):
            #self.db.child("mainmenu").child(menu_name).set(mainmenu_info)
            self.db.child("mainmenu").push(mainmenu_info)
            print(data,image_path)
            return True
        else:
            return False
        
    def get_mainmenus(self):
        mainmenus = self.db.child("mainmenu").get().val()
        return mainmenus   

    
                

    #리뷰 데이터베이스 함수
    def insert_review(self, write, data):
        review_info={
            "restaurant_name": data['restaurant_name'],
            "year": data['year'],
            "month": data['month'],
            "date": data['day'],
            "star": data['star'],
            "write": data['write']
        }
        if self.restaurant_duplicate_check(write):
            self.db.child("review").push(review_info)
            print(data)
            return True
        else:
            return False
        #self.db.child("review").child(name).set(review_info)
        #print(data)
        #return True
        
    #리뷰 평점 계산 함수
    def get_avgrate_byname(self, name):
        reviews=self.db.child("review").get()
        rates=[]
        for res in reviews.each():
            value=res.val()
            if value['restaurant_name']==name:
                rates.append(float(value['star']))
        return sum(rates)/len(rates)
    
    #리뷰 리스트 가져오기(레스토랑 이름별로)
    def get_review_byname(self, name):
        restaurants=self.db.child("review").get()
        target_value=[]
        for res in restaurants.each():
            value=res.val()
            
            if value['restaurant_name']==name:
                target_value.append(value)
        return target_value
    
    #메뉴 리스트 가져오기(레스토랑 이름별로)
    def get_food_byname(self, name):
        restaurants=self.db.child("mainmenu").get()
        target_value=[]
        for res in restaurants.each():
            value=res.val()
            
            if value['restaurant_name']==name:
                target_value.append(value)
        return target_value
    
    def get_restaurants(self):
        restaurants = self.db.child("restaurant").get().val()
        return restaurants
    
    def get_restaurant_byname(self, name):
        restaurants = self.db.child("restaurant").get()
        target_value=""
        for res in restaurants.each():
            value = res.val()
            
            if value['name'] == name:
                target_value = value
                
            return target_value
        
    def get_restaurants_bycategory(self,cate):
        restaurants=self.db.child("restaurant").get()
        target_value=[]
        for res in restaurants.each():
            value=res.val()
            
            if value['category']==cate:
                target_value.append(value)
        print("######target_value",target_value)
        new_dict={}
        for k,v in enumerate(target_value):
            new_dict[k]=v
        
        return new_dict
        
    #회원가입 함수
    def insert_user(self, data, pw):
        user_info={
            "id":data['id'],
            "pw":pw,
            "nickname":data['nickname']
        }
        if self.user_duplicate_check(str(data['id'])):
            self.db.child("user").push(user_info)
            print(data)
            return True
        else:
            return False
    
    #유저중복체크 함수
    def user_duplicate_check(self, id_string):
        users=self.db.child("user").get()
        
        print("users##", users.val())
        if str(users.val())=="None":
            return True
        else:
            for res in users.each():
                value=res.val()
                
                if value['id']==id_string:
                    return False
            return True
        
    #로그인 함수
    def find_user(self, id_, pw_):
        users=self.db.child('user').get()
        target_value=[]
        for res in users.each():
            value=res.val()
            
            if value['id']==id_ and value['pw']==pw_:
                return True
        return False
    
    def get_user_byname(self, id_):
        users = self.db.child("usert").get()
        target_value=""
        for res in users.each():
            value = res.val()
            
            if value['id'] == id:
                target_value = value
                
            return target_value