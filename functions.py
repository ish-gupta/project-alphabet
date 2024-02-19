import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
import sqlite3


def create_table():
    connection = sqlite3.connect('pa.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'schools'('s_id' INTEGER NOT NULL, 'username' TEXT NOT NULL UNIQUE, 'hash'"
                   " TEXT NOT NULL,	PRIMARY KEY('id' AUTOINCREMENT))")

