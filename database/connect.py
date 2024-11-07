import mysql.connector

from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USERBASE"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
)
