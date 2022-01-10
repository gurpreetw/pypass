# Manager
import sqlite3

class Manager:
	def __init__(self):
		self.conn = sqlite3.connect("database.db")
		print("Database Opened")


	def new_entry(self):
		pass

	def delete(self):
		pass

	def close_db(self):
		self.conn.close()
		print("Database closed")
