import sqlite3


class BaseService(object):

    def __init__(self):
        """
        :param cursor:
        """
        super().__init__()
        self.query = ""

    def build_query(self, length: str, word: str) -> None:
        self.query = "SELECT madde FROM madde WHERE LENGTH(madde)={0} and madde LIKE '%{1}%' order by madde".format(length, word)

    def build_query_params(self, length: str, word: str) -> None:
        generated_word = ""
        for letter in word:
            if letter == " ":
                generated_word += "_"
            else:
                generated_word += letter

        return self.build_query(length, generated_word)

    def execute_query_fetchall(self, **character_check: dict) -> list:
        """
        Executes the built query and then fetches all the resulting rows from the db.
        Returns the whole result set.
        :return:
        """
        # TODO : Add Try - Except

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
        if character_check["include"]:
            result_set_json = self.include_control(character_check["include"], result_set_json)
        
        if character_check["exclude"]:
            result_set_json = self.exclude_control(character_check["exclude"], result_set_json)
        result_set_json["result"] = list(map(lambda x: x.upper(), result_set_json["result"]))
        return result_set_json

    def include_control(self, char_list: list, result_set_json: dict) -> dict:
        # TODO : Which faster algorithm can be used here?
        # TODO : Add Try - Except
        # TODO : Add function doc

        hash_map = {}
        include_list = []
        for char in char_list:
            for word in result_set_json["result"]:
                if char in word.lower() and word not in hash_map.keys():
                    hash_map[word] = 1
                elif char in word.lower() and word in hash_map.keys():
                    hash_map[word] += 1
        for word, counter in hash_map.items():
            if counter == len(char_list):
                include_list.append(word)
        result_set_json["result"] = include_list
        return result_set_json


    def exclude_control(self, char_list: list, result_set_json: dict) -> dict:
        # TODO : Which faster algorithm can be used here?
        # TODO : Add Try - Except
        # TODO : Add function doc

        hash_map = {}
        exclude_list = []
        for char in char_list:
            for word in result_set_json["result"]:
                if char not in word.lower() and word not in hash_map.keys():
                    hash_map[word] = 1
                elif char not in word.lower() and word in hash_map.keys():
                    hash_map[word] += 1
        for word, counter in hash_map.items():
            if counter == len(char_list):
                exclude_list.append(word)
        result_set_json["result"] = exclude_list
        return result_set_json

"""
# TODO LIST:
MAX LENGTH is 23 min length is 2 
"""