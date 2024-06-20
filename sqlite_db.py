import sqlite3 as sq
import datetime

def db_connect() -> None:
	global db, cur

	db = sq.connect('robota-ua.db')
	cur = db.cursor()

	cur.execute("CREATE TABLE IF NOT EXISTS junior(id_info INTEGER PRIMARY KEY, datetime_info DATETIME, vacancy_count TEXT, change TEXT)")
	
	db.commit()


now = datetime.datetime.today().strftime('%Y-%m-%d')
now_for_table = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')

def create_report(quantity, last_count):
	global db, cur
	db = sq.connect('robota-ua.db')
	cur = db.cursor()
	report = cur.execute("INSERT INTO junior VALUES (NULL, ?, ?, ?)", (now_for_table, quantity, last_count))
	db.commit()

def select_last():
	last_note = cur.execute("SELECT vacancy_count FROM junior ORDER BY id_info DESC LIMIT 1").fetchone()

	return last_note


def get_table_info():
	all_vacansies = cur.execute("SELECT id_info, datetime_info, vacancy_count, change FROM junior WHERE datetime_info LIKE ?", (f"{now}%",)).fetchall()
	return all_vacansies

	
