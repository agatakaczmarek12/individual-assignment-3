# -*- coding: utf-8 -*-

#%% Excersise 3

from flask import Flask, jsonify


server = Flask("Phonebook")


phonebook = {"anastasia": "1113333444",
           "agata": "222333444",
           "octavio":"3334445555", 
           "david":"444555666"}


@server.route("/home")
def home_page(): 
    return "Welcome to the best phonebook ever"


@server.route("/add-contact/<name>/<phone>")
def add_contact(name, phone): 
    
    phonebook.update({name:phone})
    
    return jsonify(phonebook)


@server.route("/get-phone/<name>/")
def get_phone(name): 
    
    for i in phonebook:
                
        if i == name.lower():
         
            return (name + "'s phone is " + phonebook[i])
        
    else:
        
        return ("Sorry, your search was not successful")
    
    
@server.route("/delete-phone/<name>")

def del_phone(name): 
    
    for i in phonebook:
                
        if i == name.lower():
         
            del phonebook [i]
        
    else:
        
        return ("Sorry, your search was not successful")
        

@server.route("/update-phone/<name>/<phone>")

def update_phone(name,phone): 
    
    for i in phonebook:
                
        if i == name.lower():
         
            phonebook[i] = phone
            
            return ("The phonebook has been updated. The new {}'s number is {}".format(name,phone))
    else:
        
        return ("Sorry, your update was not successful")

server.run()
