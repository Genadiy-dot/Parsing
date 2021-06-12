'''

'''

from pymongo import MongoClient

C_MONGO_DBNAME = 'vacancy'
C_COLLECTION = 'jobs'

mdb = MongoClient("10.0.2.15", 27017).C_MONGO_DBNAME


def add_vacancy(company, position, salary):
    mdb.C_COLLECTION.insert_one({"company": company, "position": position, "salary": salary})


def fill_in_vacancies():
    add_vacancy("microsoft", "junior sortware developer", 45000 )
    add_vacancy("oracle", "junior programmer", 50000 )
    add_vacancy("vtb", "middle sortware developer", 90000)
    add_vacancy("sber", "senior sortware developer", 180000)


def show_vacancies():
    for v  in mdb.C_COLLECTION.find({}):
        print(v["position"], "at", v["company"], "company with salary", v["salary"])


fill_in_vacancies()
show_vacancies()





