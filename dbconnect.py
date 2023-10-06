from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')

#plan- just copy the following code and paste it to make more functions
def query_with_fetchall():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM depAirports")
        rows = cursor.fetchall()

        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def test_func():
    wantedList = str(input("Select nationality for list of respective passengers: "))
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT passengerID,lastName,firstName FROM passengers WHERE nationality = "+"'"+wantedList+"'")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def ascendingFlights():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT pilotName, dateOfDept FROM flights WHERE flightStatus = 'On Time' ORDER BY dateOfDept")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def passengerDest():
    chosenArr = str(input("Select a destination aiport: "))
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT firstName,lastName FROM passengers INNER JOIN flights ON flights.passengerID = passengers.passengerID WHERE flights.arrival = "+"'"+chosenArr+"'")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    connect()
    #query_with_fetchall()
    #test_func() # lists simple data on passengers depending on nationality as input by the user
    #ascendingFlights() #lists defining info of flights (pilot name, date of departure) that are on time in order of departure
    passengerDest() #lists all passengers going to a given destination (assumes you can find the airport codes)
