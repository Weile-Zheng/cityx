import sqlite3

try:
    connection = sqlite3.connect('cityx.db')
    cursor = connection.cursor()
    print("DB Created")

    createTable = f"""
        CREATE TABLE IF NOT EXISTS guides(
        guideID INTEGER PRIMARY KEY AUTOINCREMENT,
        date_created DATE NOT NULL
        );
    """

    cursor.execute(createTable)
    connection.commit()
    print("Table Created")

    cursor.close()
    connection.close()

except sqlite3.Error as error:
    print("Error connecting to MySQL:", error)
