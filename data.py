def combineData():
    zawodyFile = open('zawody.txt', 'r')
    uczelnieFile = open('uczelnie.txt', 'r')
    imionaMeskieFile = open('imionameskie.txt', 'r')
    imionaZenskieFile = open('imionazenskie.txt', 'r')
    nazwiskaDamskieFile = open('nazwiskadamskie.txt', 'r')
    nazwiskaMeskieFile = open('nazwiskameskie.txt', 'r')
    miastaFile = open('miasta.txt', 'r')
    zawody = list(zawodyFile.read().split("\n"))
    uczelnie = list(uczelnieFile.read().split("\n"))
    imionaMeskie = list(imionaMeskieFile.read().split("\n"))
    imionaZenskie = list(imionaZenskieFile.read().split("\n"))
    nazwiskaDamskie = list(nazwiskaDamskieFile.read().split("\n"))
    nazwiskaMeskie = list(nazwiskaMeskieFile.read().split("\n"))
    miasta = list(miastaFile.read().split("\n"))
    zawodyFile.close()
    uczelnieFile.close()
    imionaMeskieFile.close()
    imionaZenskieFile.close()
    nazwiskaDamskieFile.close()
    nazwiskaMeskieFile.close()
    miastaFile.close()
    return zawody, list(uczelnie), list(imionaMeskie), list(imionaZenskie), list(nazwiskaDamskie), list(nazwiskaMeskie), list(miasta)


def mandatyData():
    mandatyFile = open('mandaty.txt', 'r')
    mandaty = list(mandatyFile.read().split("\n"))
    mandatyToReturn = []
    for x in mandaty:
        mandatyToReturn.append(x.split(';'))
    mandatyFile.close()
    return mandatyToReturn

