import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sunshine",
    database="smj_airline_reservation"
)
cursor = conn.cursor()
# Function to read reservations
def read_reservations():
    cursor.execute("SELECT * FROM reservations")
    result = cursor.fetchall()
    return result