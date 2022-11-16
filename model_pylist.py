from datetime import date
import sqlite3 as sql
from Model import Model


class model(Model):
    def __init__(self, database):
        self.guestentries = []
        self.database = database
        self.__update_model()

    def __update_model(self):
        comments = '0' #it isn't working otherwise
        self.guestentries = []
        try:
            comments = sql.connect(self.database)
            cursor = comments.cursor()
            print("Подключен к SQLite")

            cursor.execute("SELECT * FROM messages;")
            messages = cursor.fetchall()
            for message in messages:
                params = [i for i in message]
                self.guestentries.append(params)
            comments.commit()
            cursor.close()

        except sql.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if (comments!='0'):
                print("Всего строк, измененных после подключения к базе данных: ", comments.total_changes)
                comments.close()
                print("Соединение с SQLite закрыто")

    def select(self):
        self.__update_model()
        """
        Returns guestentries list of lists
        Each list in guestentries contains: name, email, date, message
        :return: List of lists
        """
        return self.guestentries

    def insert(self, name, email, message):
        """
        Appends a new list of values representing new message into guestentries
        :param name: String
        :param email: String
        :param message: String
        :return: True
        """
        comments = '0' #it isn't working otherwise
        current_date = date.today()
        params = [name, email, current_date, message]
        self.guestentries.append(params)

        try:
            comments = sql.connect(self.database)
            cursor = comments.cursor()
            print("Подключен к SQLite")

            sqlite_insert_query = """INSERT INTO messages
                                  (name, email, date, entry)
                                  VALUES (?,?,?,?);"""
            cursor.execute(sqlite_insert_query, (name, email, current_date, message))

            comments.commit()
            cursor.close()

        except sql.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if (comments!='0'):
                print("Всего строк, измененных после подключения к базе данных: ", comments.total_changes)
                comments.close()
                print("Соединение с SQLite закрыто")

        return True
