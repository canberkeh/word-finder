import sqlite3


class BaseService(object):

    def __init__(self):
        """
        :param cursor:
        """
        super().__init__()
        self.query = ""

    def build_query(self, length: str, word: str) -> None:
        self.query = "SELECT madde FROM madde WHERE LENGTH(madde)={0} and madde LIKE '%{1}%'".format(length, word)

    def build_query_params(self, length: str, word: str) -> None:
        generated_word = ""
        for letter in word:
            if letter == " ":
                generated_word += "_"
            else:
                generated_word += letter
        return self.build_query(length, generated_word)

    def execute_query_fetchall(self) -> list:
        """
        Executes the built query and then fetches all the resulting rows from the db.
        Returns the whole result set.
        :return:
        """
        try:
            conn = sqlite3.connect('database/gts.sqlite3.db')
            conn.row_factory = lambda cursor, row: row[0]
            cursor = conn.cursor()
        except: # add an connection error exception.
            pass

        cursor.execute(self.query)
        result_set = cursor.fetchall()
        result_set_json = {"result": result_set}
        cursor.close()
        conn.close()
        return result_set_json

"""
# TODO LIST:
MAX LENGTH is 23 min length is 2 
"""