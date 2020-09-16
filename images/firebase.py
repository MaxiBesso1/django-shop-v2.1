import pyrebase
import os
from products_catalog.settings import BASE_DIR
def submit_to_firebase(file,name):
    config = {
    "apiKey": "AIzaSyA6WzjkJ2FAgCAoiPmuZMXlBeFSIbeKdgE",
      "authDomain": "test-django-firebase.firebaseapp.com",
      "databaseURL": "https://test-django-firebase.firebaseio.com",
      "projectId": "test-django-firebase",
      "storageBucket": "test-django-firebase.appspot.com",
      "messagingSenderId": "1052531513324",
      "appId": "1:1052531513324:web:94f860e2afca0c700392c9"
    }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    file2 = BASE_DIR + file
    with open(file2,"rb") as TXT_FILE:      
      storage.child("media/"+name+".jpg").put(TXT_FILE)
      url = storage.child("media/"+name+".jpg").get_url(1)
      print(url)
    return url