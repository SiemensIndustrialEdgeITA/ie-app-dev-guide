-- Create the database mydb
CREATE DATABASE mydb;
-- Connect to the mydb database
\c mydb;

-- Create the table WORDS
CREATE TABLE WORDS (
    datetimecolumn timestamp,
    word text,
    reverseword text
);

-- Create the user siemens with password 'myPassword'
CREATE USER siemens WITH PASSWORD 'myPassword';

-- Grant all privileges on the mydb database to the siemens user
GRANT ALL PRIVILEGES ON DATABASE mydb TO siemens;

-- Grant all privileges on the words table to the siemens user
GRANT ALL ON TABLE public.words TO siemens;
