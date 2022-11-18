import pyrebase
import json

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=jsn.load(f)
            
            firebase = pyrebase.initialize_app(config)
            self.db = firebase.database()
            
            
    # 메인메뉴 데이터베이스 함수
    def insert_mainmenu(self, name, data, img_path):
        mainmenu_info={
            "menu_name": data['menu_name'],
            "menu_price": data['menu_price'],
            "imge_path": img_path       
        }
        self.db.child("mainmenu").child(name).set(mainmenu_info)
        print(data, img_path)
        return True
            
            
    