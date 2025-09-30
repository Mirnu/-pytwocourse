import psycopg2
from structs.report import Report

class Repository:
    def __init__(self):
        self.connector = None
        self.cursor = None

    def __connect__(self):
        self.connector = psycopg2.connect(
            host="localhost",
            database="sharaga",
            user="postgres",
            password="postgres",
        )

        self.cursor = self.connector.cursor()

    def create_report(self, report: Report):
        self.execute(f"INSERT INTO avto (marka, model, color, year_build, number)" 
                     f"VALUES('{report.marka}', '{report.model}', '{report.color}'," 
                     f"'{report.year_build}', '{report.number}')")
        
        self.cursor.execute(f"SELECT max(id) from avto")
        for row in self.cursor:
            id_avto = row[0]
        
        self.cursor.execute(f"INSERT INTO customer (surname, name, num_phone, id_avto)" 
                            f"VALUES('{report.surname}', '{report.name}', '{report.phone_number}', '{id_avto}')")

        self.cursor.execute(f"SELECT max(id) from customer")

        for row in self.cursor:
            id_customer = row[0]

        self.cursor.execute(f"SELECT id from services where name = '{report.service}'")

        for row in self.cursor:
            id_services = row[0]

        self.cursor.execute(f"INSERT INTO zakaz (id_customer, id_services)" 
                            f"VALUES('{id_customer}', '{id_services}')")
    

        self.close()


    def execute(self, query: str,  *args):
        self.__connect__()
        return self.cursor.execute(query, args)

    
    def close(self):
        self.connector.commit()
        self.cursor.close()
        self.connector.close()

    def get_services(self):
        self.execute("SELECT * FROM services")
        values = {}

        rows = self.cursor.fetchall()

        for row in rows:
            values[row[1]] = row[2]

        self.close()

        return values