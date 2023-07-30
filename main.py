from functions import *
import textwrap


def main():
    try:
        connection = sqlite3.connect('my_database.db')
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
                createGuide(cursor)
            elif userinput.lower() == "delete":
                deleteGuide(cursor)
            elif userinput.lower() == "view":
                viewGuide(cursor)
            elif userinput.lower() == "showall":
                createdGuideList(cursor)
            else:
                break
    except sqlite3.Error as error:
        print("Error connecting to MySQL:", error)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
