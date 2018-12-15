# -*- coding: utf-8 -*-

#%%
import requests
#from flask import Flask, jsonify

def add_contact(name, phone):
    request=requests.get("http://127.0.0.1:5000/add-contact/{}/{}".format(name,phone))
    return request.json()                    


#%%
import requests
#from flask import Flask, jsonify

def get_phone(name): 
    request=requests.get("http://127.0.0.1:5000/get-phone/{}".format(name))
    return request.json()                    

#%%
import requests
#from flask import Flask, jsonify

def del_phone(name): 
    request=requests.get("http://127.0.0.1:5000/delete-phone/{}".format(name))
    return request.json()                    

#%%
import requests
#from flask import Flask, jsonify

def update_phone(name,phone): 
    request=requests.get("http://127.0.0.1:5000/update-phone/{}".format(name,phone))
    return request.json()   