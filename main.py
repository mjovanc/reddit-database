#!/usr/bin/python
import psycopg2
import json
import time
import datetime


def start():
	create_tables_with_constraints()
	import_data_with_constraints()
	create_tables_without_constraints()
	import_data_without_constraints()
	

def import_data_with_constraints():
	con = psycopg2.connect(host='localhost', database='2dv513_a2', user='postgres', password='test1234')
	cur = con.cursor()

	author_set = set()
	subreddits_set = set()

	start = time.time()

	with open('RC_2011-07', 'r') as file:
		for data in file:
			data = json.loads(data)
		
			# Checking if author not already has been added to database
			if data['author'] not in author_set:
				author_set.add(data['author'])
				cur.execute("INSERT INTO reddit.users VALUES (%s);",
				(str(data['author']), ))


			# Checking if subreddit not already has been added to database
			if data['subreddit'] not in subreddits_set:
				subreddits_set.add(data['subreddit'])
				cur.execute("INSERT INTO reddit.subreddits VALUES (%s, %s);",
					(str(data['subreddit_id']), str(data['subreddit'])))

			# Adding post to database
			cur.execute("INSERT INTO reddit.posts VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
				(
					str(data['id']),
					str(data['parent_id']),
					str(data['link_id']),
					str(data['name']),
					str(data['author']),
					str(data['body']),
					str(data['subreddit_id']),
					str(data['score']),
					data['created_utc'],
				)
			)	
			con.commit()

	end = time.time()
	elapsed = end - start
	elapsed_time = str(datetime.timedelta(seconds=elapsed))
	
	print('IMPORT COMPLETE!')
	print('Elapsed import time: %s' % (elapsed_time))


def import_data_without_constraints():
	con = psycopg2.connect(host='localhost', database='2dv513_a2_nc', user='postgres', password='test1234')
	cur = con.cursor()
	start = time.time()

	with open('RC_2011-07', 'r') as file:
		for data in file:
			data = json.loads(data)

			# Adding post to database
			cur.execute("INSERT INTO reddit.posts VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
				(
					str(data['id']),
					str(data['parent_id']),
					str(data['link_id']),
					str(data['name']),
					str(data['author']),
					str(data['body']),
					str(data['subreddit_id']),
					str(data['subreddit']),
					str(data['score']),
					data['created_utc'],
				)
			)	
			con.commit()

	end = time.time()
	elapsed = end - start
	elapsed_time = str(datetime.timedelta(seconds=elapsed))
	
	print('IMPORT COMPLETE!')
	print('Elapsed import time: %s' % (elapsed_time))


def create_tables_with_constraints():
	con = psycopg2.connect(host='localhost', database='2dv513_a2', user='postgres', password='test1234')

	cur = con.cursor()
	cur.execute('CREATE SCHEMA reddit;')
	cur.execute('CREATE TABLE reddit.users(name VARCHAR(255) PRIMARY KEY NOT NULL);')
	cur.execute('CREATE TABLE reddit.subreddits(subreddit_id VARCHAR(20) PRIMARY KEY NOT NULL, subreddit_name VARCHAR(255) NOT NULL);')
	cur.execute('''CREATE TABLE reddit.posts(
		id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
		post_id VARCHAR(50) NOT NULL, 
		parent_id VARCHAR(50) NOT NULL,
		link_id VARCHAR(50) NOT NULL,
		name VARCHAR(255) NOT NULL,
		author VARCHAR(100) REFERENCES reddit.users(name),
		body VARCHAR(40000),
		subreddit VARCHAR(50) REFERENCES reddit.subreddits(subreddit_id),
		score INT,
		created_utc INT NOT NULL
		);'''
	)

	cur.close()
	con.commit()


def create_tables_without_constraints():
	con = psycopg2.connect(host='localhost', database='2dv513_a2_nc', user='postgres', password='test1234')

	cur = con.cursor()
	cur.execute('CREATE SCHEMA reddit;')
	cur.execute('''CREATE TABLE reddit.posts(
		id VARCHAR(50) NOT NULL, 
		parent_id VARCHAR(50) NOT NULL,
		link_id VARCHAR(50) NOT NULL,
		name VARCHAR(255) NOT NULL,
		author VARCHAR(100) NOT NULL,
		body VARCHAR(40000),
		subreddit_id VARCHAR(50) NOT NULL,
		subreddit VARCHAR(100) NOT NULL,
		score INT,
		created_utc INT NOT NULL
		);'''
	)

	cur.close()
	con.commit()

if __name__ == '__main__':
	start()
