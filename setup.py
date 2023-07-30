import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Weilemysql2004',
}

try:
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()
    createDB = "CREATE DATABASE IF NOT EXISTS cityx;"
    cursor.execute(createDB)
    print("DB Created")
    connection.commit()

    cursor.execute("USE cityx")

    createTable = f"""
        CREATE TABLE IF NOT EXISTS guides(
        guideID INT PRIMARY KEY AUTO_INCREMENT,
        date_created DATE NOT NULL
        );
    """

    cursor.execute(createTable)
    connection.commit()
    print("Table Created")

    cursor.close()
    connection.close()

except mysql.connector.Error as error:
    print("Error connecting to MySQL:", error)
