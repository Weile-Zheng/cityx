import util
from generator import generate
from datetime import datetime
import mysql.connector


current_date = datetime.today().date()
print("Current date:", current_date)


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
    try:
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except mysql.connector.Error as error:
        print("\n---")
    print("")


def createGuide(cursor):
    generate()


def deleteGuide(cursor):
    print()


def viewGuide(cursor):
    print("viewGuide")
