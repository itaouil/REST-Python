import pymysql.cursors

class Database:

    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          db='petdb',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def update(self, id, pet):
        try:
            with self.connection.cursor() as cursor:
                # Add record to pets table
                sql = "UPDATE `pets` SET `name`=%s, `species`=%s, `gender`=%c, `birthday`=%d) WHERE `id`=%s"
                cursor.execute(sql, (pet.name, pet.species, pet.gender, pet.birthday, id))

            # Save changes
            self.connection.commit()

        finally:
            self.connection.close()

    def list(self, table):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `*` FROM `pets`
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)

        finally:
            self.connection.close()
