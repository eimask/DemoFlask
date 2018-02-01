import pymysql


class Database:
    def connect(self):
        return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='ptMinh93',
        db='pythondb',
        cursorclass=pymysql.cursors.DictCursor
    )

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id is None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
