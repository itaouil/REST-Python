import pymysql.cursors

class Database:

    def __init__(self):
        """
            Constructor.

            Sets the connection state.
        """
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          db='petdb',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def update(self, id, pet):
        """
            Updates the database entry
            with the correspondant ID.

            Arguments:
                int: Pet's ID
                Pet: Pet object
        """
        try:
            with self.connection.cursor() as cursor:
                # Add record to pets table
                sql = "UPDATE `pets` SET `name`=%s, `species`=%s, `gender`=%c, `birthday`=%d) WHERE `id`=%s"
                cursor.execute(sql, (pet.name, pet.species, pet.gender, pet.birthday, id))

            # Save changes
            self.connection.commit()

        finally:
            self.connection.close()

    def list(self):
        """
            Fetches all instances of the
            pets databse.

            Returns:
                list: List of database entries
        """
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `*` FROM `pets`"
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result)
                return result

        finally:
            self.connection.close()
