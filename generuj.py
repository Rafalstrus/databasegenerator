import mysql.connector
import random
from data import combineData


def start():
    printInfo()
    data = inputData()
    mydb = makeConnection(data)
    random.seed(input("wprowadz klucz losowy: "))
    mycursor = mydb.cursor()
    if(checkDatabaseName(data[3], mycursor)):
        mydb = mysql.connector.connect(
                host=data[0],
                user=data[1],
                password=data[2],
                database=data[3])
        mycursor = mydb.cursor()
        info = getInfo()
        insertdata(info, mycursor)
        mydb.commit()
    else:
        start()

def printInfo():
    print("database generator is program that can generate random persons to mysql database")
    print("program can make new database with table containing random persons")


def inputData():
    hostName = input("please enter host name or address: ") # 127.0.0.1 or localhost is a adress of local xampp mysql server
    userName = input("please enter a username: ") #default is 'root'
    password = input("please enter a password: ") #default is empty
    databaseName = input("please enter a database name: ")
    return [hostName, userName, password, databaseName]


def makeConnection(data):
    mydb = mysql.connector.connect(
        host=data[0],
        user=data[1],
        password=data[2])
    return mydb


def checkDatabaseName(databaseName, mycursor):
    mycursor.execute("SHOW DATABASES LIKE '"+str(databaseName)+"';")
    exist = True
    for x in mycursor:
        if not(not x):
            exist = False
            print('database with this name already exist')
            x = int(input("if you want to expand existing database write 1, else write 0: "))
            print(x)
            if x:
                return True
    if(exist):
        mycursor.execute("CREATE DATABASE "+str(databaseName)+"")
        print('new database was created')
        return True
    else:
        return False



def getInfo():
    info = []
    info.append(int(input("please specify the number of people to be created: ")))
    info.append(int(input("minimalne zarobki (liczba całkowita bez zł): ")))
    info.append(int(input("maksymalne zarobki (liczba całkowita bez zł): ")))
    return info


def generatePerson(zawody, uczelnie, imionaMeskie, imionaZenskie, nazwiskaDamskie, nazwiskaMeskie, miasta):
    if random.randint(0, 1):
        return [zawody[random.randint(0, len(zawody)-1)], uczelnie[random.randint(0, len(uczelnie)-1)],
                imionaMeskie[random.randint(0, len(
                    imionaMeskie)-1)], nazwiskaMeskie[random.randint(0, len(nazwiskaMeskie)-1)],
                miasta[random.randint(0, len(miasta)-1)]]
    else:
        return [zawody[random.randint(0, len(zawody)-1)], uczelnie[random.randint(0, len(uczelnie)-1)],
                imionaZenskie[random.randint(0, len(
                    imionaZenskie)-1)], nazwiskaDamskie[random.randint(0, len(nazwiskaDamskie)-1)],
                miasta[random.randint(0, len(miasta)-1)]]


def insertdata(info, mycursor):
    university = input(
        "ile osob ma studia wyzsze?(jeżeli 0 - 100%, jeżeli 50 - 50%): ")
    unemployed = input(
        "prosze podac współczynnik bezrobotnosc(jeżeli ma ich nie byc 0, jeżeli ma byc połowa 100)")
    zawody, uczelnie, imionaMeskie, imionaZenskie, nazwiskaDamskie, nazwiskaMeskie, miasta = combineData()
    for x in range(int(university)):
        uczelnie.append("brak")
    for x in range(int(unemployed)):
        zawody.append("brak")
    mycursor.execute("CREATE TABLE `people` ( `id` INT NOT NULL UNIQUE AUTO_INCREMENT , `imie` VARCHAR(32) NOT NULL , `nazwisko` VARCHAR(32) NOT NULL , `uczelnia` VARCHAR(96) NOT NULL , `zawod` VARCHAR(64) NOT NULL , `miasto` VARCHAR(64) NOT NULL , `pensja` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB")
    for x in range(int(info[0])):
        dataToupdate = generatePerson(
            zawody, uczelnie, imionaMeskie, imionaZenskie, nazwiskaDamskie, nazwiskaMeskie, miasta)
        updateData(dataToupdate, mycursor, info)

def updateData(dataToupdate, mycursor, info):
    if dataToupdate[0] == "brak":
        pensja = 0
    else:
        pensja = random.randint(int(info[1]), int(info[2]))
    dataToUpdate = "INSERT INTO people(imie,nazwisko,uczelnia,zawod,miasto,pensja) VALUES('" + \
        dataToupdate[2]+"','"+dataToupdate[3]+"','"+dataToupdate[1]+"','" + \
        dataToupdate[0]+"'"+",'"+dataToupdate[4]+"'"+","+str(pensja)+")"
    mycursor.execute(dataToUpdate)

start()
