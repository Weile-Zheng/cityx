from functions import *
from datetime import datetime
from util import getCityInput
import textwrap


def main():
    current_date = datetime.today().date()
    print("Current date:", current_date)
    print("\n***Enter --help for more information***")
    print("***Enter \"menu\" at anytime to review lists of actions available***\n")

    try:

        connection = sqlite3.connect('cityx.db')
        cursor = connection.cursor()

        createdGuideList(cursor)

        menu = textwrap.dedent("""
            Actions
            Guides
            1) Generate 
            2) Delete
            3) View 
            4) ShowAll
            5) Quit
        """)

        print(menu)
        print("Enter Your Action")
        while True:
            userinput = input("->")
            if userinput.lower() == "generate":
                city = getCityInput()
                createGuide(cursor, util.formatCityInput(city), current_date)
                connection.commit()
            elif userinput.lower() == "delete":
                city = getCityInput()
                deleteGuide(cursor, util.formatCityInput(city))
                connection.commit()
            elif userinput.lower() == "view":
                viewGuide(cursor)
            elif userinput.lower() == "showall":
                createdGuideList(cursor)
            elif userinput.lower() == "menu":
                print(menu)
            else:
                print("Unknown Action")
    except sqlite3.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
