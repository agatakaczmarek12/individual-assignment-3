# -*- coding: utf-8 -*-
#%%% Exercise 1

class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

carrot = Product("carrot", 3)
potatoe = Product("potatoe",10)
ham = Product("ham",4)
cheese = Product("cheese", 6)


def recalculate_quality(product):
    if product.name == "potatoe":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3

#%%% Excercise 2

import requests


def take_all_repository(user):

    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url).json()
    
    return response
    
take_all_repository("agatakaczmarek12")


#%% Excercise 2

import requests


def description_repository(user):

    url = "https://api.github.com/users/{}/repos".format(user)
    response = requests.get(url).json()
    
    description_lst ={}
    
    
    for i in response:
        
        description_lst.update({"Name":i["name"]})
        description_lst.update({"Number of stars":i["stargazers_count"]})
        description_lst.update({"Language":i["language"]})
        description_lst.update({"Url":i["url"]})
        
        print ([description_lst])


description_repository("agatakaczmarek12")


##%% Excersise 3
#
#from flask import Flask, jsonify
#
#
#server = Flask("Phonebook")
#
#
#phonebook = {"anastasia": "1113333444",
#           "agata": "222333444",
#           "octavio":"3334445555", 
#           "david":"444555666"}
#
#
#@server.route("/home")
#def home_page(): 
#    return "Welcome to the best phonebook ever"
#
#
#@server.route("/add-contact/<name>/<phone>")
#def add_contact(name, phone): 
#    
#    phonebook.update({name:phone})
#    
#    return jsonify(phonebook)
#
#
#@server.route("/get-phone/<name>/")
#def get_phone(name): 
#    
#    for i in phonebook:
#                
#        if i == name.lower():
#         
#            return (name + "'s phone is " + phonebook[i])
#        
#    else:
#        
#        return ("Sorry, your search was not successful")
#    
#    
#@server.route("/delete-phone/<name>")
#
#def del_phone(name): 
#    
#    for i in phonebook:
#                
#        if i == name.lower():
#         
#            del phonebook [i]
#        
#    else:
#        
#        return ("Sorry, your search was not successful")
#        
#
#@server.route("/update-phone/<name>/<phone>")
#
#def update_phone(name,phone): 
#    
#    for i in phonebook:
#                
#        if i == name.lower():
#         
#            phonebook[i] = phone
#            
#            return ("The phonebook has been updated. The new {}'s number is {}".format(name,phone))
#    else:
#        
#        return ("Sorry, your update was not successful")
#
#server.run()

#%%
