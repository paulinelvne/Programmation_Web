#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime

from flask import Flask, abort
from flask import request, make_response, render_template
from database import get_cocktails, get_cocktail_id, get_cocktail_name, get_cocktail_ingredient, delete_cocktail, write_json, reset_data
import json

#import data
#import cmds

#from model import User, Field
#from model import add_user, delete_user
#from api import SITE_API

# ↓ DO NOT MODIFY THIS PART ↓ #############################################
# init flask app instance
                                                 #
app = Flask(__name__)
app.config.from_mapping(DEBUG = True)                                         #
# setup with the configuration provided by the user / environment         #
##app.config.from_object('config.Development')                              #
##data.init_app(app)                                                        #
##cmds.init_app(app)                                                        #
##app.register_blueprint(SITE_API, url_prefix='/api')                       #
# ↑ DO NOT MODIFY THIS PART ↑ #############################################

cocktails_base = get_cocktails()

@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    front_page_cocktails = []
    for i in range(3):
        front_page_cocktails.append(cocktails_base[i])
    #app.logger.debug(front_page_recipes)
    return render_template('index.html', favorite_cocktails = front_page_cocktails)

@app.route('/cocktails', methods=['GET'])
def cocktails():
    app.logger.debug('serving root URL /')

    cocktails_base = get_cocktails()

    if request.args:
        cocktails = search(request)

    else :
        cocktails = cocktails_base

    module = len(cocktails) // 3
    reste = len(cocktails) % 3

    return render_template('cocktails.html',  cocktails = cocktails, m = module, r = reste)

@app.route('/cocktail/<id>', methods=['GET'])
def cocktail(id):
    app.logger.debug('serving root URL /')
    cocktails_base = get_cocktails()
    cocktail = get_cocktail_id(cocktails_base, id)
    return render_template('cocktails.html', cocktail = cocktail)


@app.route('/cocktail/<id>', methods=['POST'])
def supprimer_cocktail(id):
    app.logger.debug('serving root URL /')

    delete_cocktail(id)

    cocktails=get_cocktails()

    module = len(cocktails) // 3
    reste = len(cocktails) % 3

    return render_template('cocktails.html', cocktails = cocktails, m = module, r = reste)


@app.route('/contact', methods=['GET'])
def contact():
    app.logger.debug('serving root URL /')
    return render_template('contact.html')

@app.route('/ajout', methods=['GET'])
def ajouter():
    app.logger.debug('serving root URL /')
    return render_template('ajout.html')

@app.route('/cocktails', methods=['POST'])
def ajout_cocktail():
    app.logger.debug('serving root URL /')

    cocktails_base = get_cocktails()

    cocktail = {"id" : cocktails_base[len(cocktails_base) - 1]["id"] + 1, 'name': request.form['cocktail_name'], 'ingredients': request.form['type'].split("\n"),
            'quantities': request.form['quantities'].split("\n"), 'preparation': request.form['preparation'].split("\n"), 'image' : "neutre.jpeg",
            'difficulte': request.form['difficulty'], 'cout': request.form['cost']}

    write_json(cocktail, "data.json")

    cocktails_base = get_cocktails()

    module = len(cocktails_base) // 3
    reste = len(cocktails_base) % 3

    return render_template('cocktails.html', cocktails = cocktails_base, m = module, r = reste)

@app.route('/', methods=['POST'])
def reset_json():
    app.logger.debug('serving root URL /')
    reset_data()
    cocktails_base = get_cocktails()

    module = len(cocktails_base) // 3
    reste = len(cocktails_base) % 3

    return render_template('cocktails.html', cocktails = cocktails_base, m = module, r = reste)


def search(request):
    app.logger.debug(request.args)
    cocktails_search = []
    cocktails_base = get_cocktails()

    c_name = get_cocktail_name(cocktails_base, request.args["pattern"])
    if len(c_name) != 0 :
        cocktails_search=c_name

    cocktails_search = cocktails_search + get_cocktail_ingredient(cocktails_base, request.args["pattern"])
    #print(cocktails_search)

    list = []
    listEntity = []
    for cocktail in cocktails_search:
        if cocktail["id"] not in list:
            listEntity.append(cocktail)
            list.append(cocktail["id"])
    return listEntity

if __name__ == "__main__":
    app.run()

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
