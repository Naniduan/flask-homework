class Model:
    def __init__(self, database):
        """
        we give the model a database to update and take from
        :param database: String (name of the file)
        """
        pass

    def select(self):
        """
        Gets all rows from the database as a list of lists.
        Row consists of name, email, date, and message.
        :return: List of lists containing all rows of database
        """
        pass

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
