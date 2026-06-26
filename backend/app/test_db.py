from database.db import connection

if connection.is_connected:
    print("Data Base Connected ")

else:
    print("Some Thing Happen Not connected")

    