import util
from generator import generate
import sqlite3


def createdGuideList(cursor):
    """
    Get all entries of created guides from DB
    and print to screen

    Parameters:
    cursor for running the query
    """

    print("Created Guides: ")
    getGuide = """
    Select *
    From guides
    """
    cursor.execute(getGuide)
    try:
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print("Error Connecting")
    print("\n---")


def createGuide(cursor, cityname, date):
    try:
        cursor.execute(
            'INSERT INTO guides (city, date_created) VALUES (?, ?)', (cityname, date))
        print("Entry successfull saved to DB")

    except sqlite3.Error as error:
        print("Error at createGuide")

    generate(cityname)


def deleteGuide(cursor, cityname):
    confirm = input(("Confirm to delete" + cityname + "? [y/n]"))
    if confirm == "n":
        return 0

    try:
        delete = f"""
        DELETE FROM guides
        WHERE city = \"{cityname}\";     
        """

        cursor.execute(delete)
        print("Entry successfull deleted from DB")

    except sqlite3.Error as error:
        print("Error at deleteGuide")


def viewGuide(cursor):
    print("viewGuide")
