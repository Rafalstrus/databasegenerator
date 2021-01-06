import mysql.connector
import random
from data import combineData, mandatyData


def start():
    printInfo()
    data = inputData()
    mydb = makeConnection(data)
    random.seed(input("wprowadz klucz losowy: "))
    mycursor = mydb.cursor()
    if checkDatabaseName(data[3], mycursor):
        mycursor.execute("create database "+str(data[3])+"")
        mydb = mysql.connector.connect(
            host=data[0],
            user=data[1],
            password=data[2],
            database=data[3])
        mycursor = mydb.cursor()
        info = getInfo()
        insertdata(info, mycursor)
        dataToLogin(mycursor)
        mydb.commit()
    else:
        start()


def printInfo():
    print("informcje")


def inputData():
    hostName = input("prosze podac nazwe lub adres hosta: ")
    userName = input("prosze podac nazwe uzytkownika: ")
    password = input("prosze podac haslo: ")
    databaseName = input("prosze podac nazwe nowej bazy: ")
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
            print('baza o tej nazwie jest zajeta')
    return exist

    mycursor.execute("CREATE DATABASE "+str(databaseName)+"")
    print('utworzono nowa baze')


def getInfo():
    info = []
    info.append(int(input("Proszę podać liczbe osób: ")))
    info.append(int(input("minimalne zarobki (liczba całkowita bez zł): ")))
    info.append(int(input("maksymalne zarobki (liczba całkowita bez zł): ")))
    info.append(int(input("liczba mandatów: ")))
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
    mycursor.execute("CREATE TABLE`mandaty` ( `id` INT NOT NULL UNIQUE AUTO_INCREMENT , `idPerson` INT NOT NULL , `kwota` INT NOT NULL , `komentarz` VARCHAR(512) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB")
    mycursor.execute(
        "ALTER TABLE `mandaty`  ADD CONSTRAINT `FK1` FOREIGN KEY (`idPerson`) REFERENCES `people` (`ID`) ")
    mandaty = mandatyData()
    for x in range(int(info[0])):
        dataToupdate = generatePerson(
            zawody, uczelnie, imionaMeskie, imionaZenskie, nazwiskaDamskie, nazwiskaMeskie, miasta)
        updateData(dataToupdate, mycursor, info)
    for x in range(int(info[3])):
        updatyMandaty(random.randint(
            1, info[0]), mandaty[random.randint(0, len(mandaty)-1)], mycursor)


def updateData(dataToupdate, mycursor, info):
    if dataToupdate[0] == "brak":
        pensja = 0
    else:
        pensja = random.randint(int(info[1]), int(info[2]))
    dataToUpdate = "INSERT INTO people(imie,nazwisko,uczelnia,zawod,miasto,pensja) VALUES('" + \
        dataToupdate[2]+"','"+dataToupdate[3]+"','"+dataToupdate[1]+"','" + \
        dataToupdate[0]+"'"+",'"+dataToupdate[4]+"'"+","+str(pensja)+")"
    mycursor.execute(dataToUpdate)


def updatyMandaty(id, mandaty, mycursor):
    dataToUpdate = "INSERT INTO mandaty(idPerson,kwota,komentarz) Values("+str(
        id)+","+str(mandaty[1])+",'"+mandaty[0]+"'"+")"
    mycursor.execute(dataToUpdate)


def dataToLogin(mycursor):
    mycursor.execute(
        "CREATE TABLE `logins` (`id` INT NOT NULL UNIQUE AUTO_INCREMENT, `name` VARCHAR(32) NOT NULL,`password` VARCHAR(512) NOT NULL)")
    dataToUpdate = "INSERT INTO logins(name,password) Values('admin','5a38afb1a18d408e6cd367f9db91e2ab9bce834cdad3da24183cc174956c20ce35dd39c2bd36aae907111ae3d6ada353f7697a5f1a8fc567aae9e4ca41a9d19d')"
    mycursor.execute(dataToUpdate)


start()
