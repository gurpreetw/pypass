# Manager
import sqlite3
from sqlite3.dbapi2 import Error
from generator import Generator

gen = Generator()

class Manager:
	def __init__(self):
		try:
			self.conn = sqlite3.connect("database.db")
		except Error as e:
			print("fail to make connection Error:", e)

		self.cursor = self.conn.cursor()
		self.query = ""
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS Passwords (
			AccountName		TEXT		NOT NULL,
			Email			TEXT,
			Password		TEXT		NOT NULL
		)""")

		# print("Database Opened")


	def new_entry(self):
		acc_name = input("Enter Account Name -> ")
		email = input("Enter Email ID -> ")
		print("Enter Password or enter g to generate password or Enter your Custom password ")
		password = input("-> ")
		inp = ""
		if password == 'g':
			password = gen.generate_one()
			print(f"Password is {password}")

		# self.query = f"""

		# """

	def delete(self):
		# self.query = f"""
			
		# """
		pass

	def close_db(self):
		self.conn.close()
		print("Database closed")
