import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

server.config["MYSQL_HOSt"] = os.environ.get("MYSQL_HOST")
print(server.config["MYSQL_HOST"])
