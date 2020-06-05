import pyodbc
import argparse


def create_connection(password):
    server = 'NDRACHEVA\\SQLEXPRESS'
    username = 'express'
    database = 'Test_DB'

    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return connection


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--password',
                        help='an express user password for DB connection')
    args = parser.parse_args()
    
    connection = create_connection(args.password)
    cursor = connection.cursor()

    # Update the query: get first name and last name of authors which posted after 2020-01-01
    cursor.execute('SELECT * FROM posts')

    for row in cursor:
        print(row)


if __name__ == "__main__":
    main()