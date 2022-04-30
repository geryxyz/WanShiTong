-- TABLE
CREATE TABLE folders
(
	id INTEGER
		constraint folders_pk
			primary key autoincrement,
	parent_id INTEGER,
	name TEXT,
	userid INTEGER
);
CREATE TABLE saved_articles
(
	id integer,
	folderid integer,
	article integer
);
CREATE TABLE "sessions"
(
	id INTEGER not null
		constraint sessions_pk
			primary key autoincrement,
	session TEXT(256),
	user_id INTEGER,
	creation_date DateTime,
	expiry_date DateTime,
	last_usage DateTime
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE users (id INTEGER, username TEXT(256), password INTEGER, regdate TEXT(256), lastlogin TEXT(256), email TEXT(256), name TEXT(256), PRIMARY KEY (id));
 
-- INDEX
CREATE UNIQUE INDEX sessions_id_uindex
	on sessions (id);
 
-- TRIGGER
 
-- VIEW
 
