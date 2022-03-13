from ast import Pass
import sqlite3

from pyrsistent import v
from utilities.exceptions import DBCursorError, DatabaseConnectionError, QueryError


class BaseService(object):

    def __init__(self):
        """
        :param cursor:
        """
        super().__init__()
        self.query = ""


    def execute_query_fetchall(self, **character_check: dict) -> dict:
        """
        Executes the built query and then fetches all the resulting rows from the db.
        Returns the whole result set.
        :param character_check: a dict that includes
            language as string
            include as list[str]
            exclude as list[str]
        :return: result_set_json as dict.
        """
        try:
            if character_check["language"] == "tr":
                conn = sqlite3.connect('database/gtsTR.sqlite3.db')
            else:
                conn = sqlite3.connect('database/gtsEN.sqlite3.db')
        except:
            raise DatabaseConnectionError("Can not connect to sqlite db.")
        
        try:
            conn.row_factory = lambda cursor, row: row[0]
            cursor = conn.cursor()
        except:
            raise DBCursorError("Can not initialize cursor.")

        try:
            cursor.execute(self.query)
            result_set = cursor.fetchall()
            result_set_json = {"result": result_set}
        except:
            raise QueryError("Can not execute desired query.")
        finally:
            cursor.close()
            conn.close()
        
        if character_check["include"]:
            result_set_json = self.include_control(character_check["include"], result_set_json)
        
        if character_check["exclude"]:
            result_set_json = self.exclude_control(character_check["exclude"], result_set_json)

        result_set_json["result"] = [word.upper() for word in result_set_json["result"] if (" " not in word) and (len(word) > 1)]
        return result_set_json


    def build_query_params(self, length: str, word: str, language: str) -> None:
        """
        Builds query parameters. Removes blank lines,
        Generates query.
        :param: length as str,
                word as str,
                language as str
        :return:
        """
        generated_word = ""
        for letter in word:
            if letter == " ":
                generated_word += "_"
            else:
                generated_word += letter
        if language == "tr":
            return self.build_query_tr(length, generated_word)
        else:
            return self.build_query_en(length, generated_word)


    def build_query_tr(self, length: str, word: str) -> None:
        """
        Builds query with given parameters. 
        :param: length as str, word as str.
        """
        try:
            if length == 0:
                self.query = "SELECT madde FROM madde WHERE madde LIKE '%{0}%' order by madde".format(word)
            else:
                self.query = "SELECT madde FROM madde WHERE LENGTH(madde)={0} and madde LIKE '%{1}%' order by madde".format(length, word)
        except:
                    raise QueryError("Failed to fetch items. Check query parameters!")
    def build_query_en(self, length: str, word: str) -> None:
        """
        Builds query with given parameters. 
        :param: length as str, word as str.
        """
        try:
            if length == 0:
                self.query = "SELECT word FROM entries WHERE word LIKE '%{0}%' order by word".format(word)
            else:
                self.query = "SELECT word FROM entries WHERE LENGTH(word)={0} and word LIKE '%{1}%' order by word".format(length, word)
        except:
            raise QueryError("Failed to fetch items. Check query parameters!")


    def include_control(self, char_list: list, result_set_json: dict) -> dict:
        """
        Executes include letter control.
        :param: char_list as list,
                result_set_json as dict
        :return: result_set_json as dict
        """
        # TODO : Which faster algorithm can be used here?

        # hash_map = {}
        # include_list = []
        # for char in char_list:
        #     for word in result_set_json["result"]:
        #         if char in word.lower() and word not in hash_map.keys():
        #             hash_map[word] = 1
        #         elif char in word.lower() and word in hash_map.keys():
        #             hash_map[word] += 1
        # for word, counter in hash_map.items():
        #     if counter == len(char_list):
        #         include_list.append(word)
        include_list = []
        char_list_set = set(char_list)
        for word in result_set_json["result"]:
            set_word = set(word)
            if len(char_list_set.intersection(set_word)) == len(char_list):
                include_list.append(word)
        result_set_json["result"] = include_list

        return result_set_json


    def exclude_control(self, char_list: list, result_set_json: dict) -> dict:
        """
        Executes exclude letter control.
        :param: char_list as list,
                result_set_json as dict
        :return: result_set_json as dict
        """
        # TODO : Which faster algorithm can be used here?

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
