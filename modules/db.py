#!/usr/bin/python

import pymysql.cursors
from datetime import datetime

class Database:

    def __init__(self):
        """
            Constructor.

            Creates the connection object.
        """
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          db='petdb',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def add(self, pet):
        """
            Adds a pet entry in the
            pets database.

            Arguments:
                Pet: Pet object
        """
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `pets` (`name`, `gender`, `species`, `birthday`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (pet.name, pet.gender, pet.species, datetime.fromtimestamp(pet.birthday)))

        # Save changes
        self.connection.commit()

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
                sql = "UPDATE `pets` SET `name`=%s, `species`=%s, `gender`=%s, `birthday`=%s WHERE `id`=%s"
                cursor.execute(sql, (pet.name, pet.species, pet.gender, datetime.fromtimestamp(pet.birthday), id))

            # Save changes
            self.connection.commit()

        finally:
            self.connection.close()

    def list(self):
        """
            Fetches all instances of the
            pets database.

            Returns:
                list: List of database entries
        """
        try:
            with self.connection.cursor() as cursor:
                # Read all entries in the table
                sql = "SELECT `*` FROM `pets`"
                cursor.execute(sql)

                # Fetch results
                result = cursor.fetchone()
                print("Result: ", result)

                return result

        finally:
            self.connection.close()
