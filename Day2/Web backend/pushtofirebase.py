import pyrebase
import random
import time
config = {
  "apiKey": "AIzaSyBLn70sg-p9fzsDxRWy59xMxPYe6Ll-ge4",
  "authDomain": "peapythontraining.firebaseapp.com",
  "databaseURL": "https://peapythontraining.firebaseio.com",
  "projectId": "peapythontraining",
  "storageBucket": "peapythontraining.appspot.com",
  "messagingSenderId": "379229483000"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# # save data
# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("users").push(data)

# update data
while True:
  random_x = random.randrange(1,20)
  db.child("test").child("node1").set(random_x)
  time.sleep(2)