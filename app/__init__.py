from flask import Flask	#1º
app = Flask(__name__)  	#2º Este orden es esencial
from app import routes	#3º
