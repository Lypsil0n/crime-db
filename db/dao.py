import psycopg2 as p

class DAO:
    def __init__(self):
        self.conn_string = "dbname='crimedb' user='dbadm' password='dbadm' host='localhost' port='5432'"

    def connect(self):
        "Connect to the database"
        conn = p.connect(self.conn_string)
        return conn
    
    def close(self, conn):
        "Close the connection to the database"
        conn.close()
    
    def get_by_query(self, conn, query):
        "Fetch records based on query"
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM mal where malnummer like '%{query}%' OR tilltalad like '%{query}%' OR personnummer like '%{query}%' OR brottsrubricering like '%{query}%'")
        res = cursor.fetchall()

        cursor.close()
        return res
    
    def get_all(self, conn):
        "Fetch all records"
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM mal")
        res = cursor.fetchall()

        cursor.close()
        return res