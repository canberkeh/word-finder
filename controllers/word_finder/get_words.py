import json
from flask import request
from controllers import app
from services.base_service import BaseService
from utilities.utilities import check_and_get_parameters, response_success


@app.route('/word_finder/get_words', methods=['POST'])
def get_words():
    """
    GET WORDS ADD DESCRIPTION
    ---
    tags:
        - get_words
    parameters:
      - in: body
        name: body
        description: JSON parameters.
        required: true
        schema:
          required:
            - length
            - word
            - include
            - exclude
          properties:
            length:
              type: string
              description: length of the word.
              example: 5
            word:
              type: string
              description: Word itself.
              example: s lam
            include:
              type: list or None
              description: list of letters that should be in.
              default: None
              example: ["a","s"]
            exclude:
              type: list or None
              description: list of letters that must not be in.
              default: None
              example: ["c", "z"]
    responses:
        200:
            description: If word list can be found. Returns it.
            schema:
              properties:
                error_code:
                  description: 0 if successful, negative value otherwise.
                  type: integer
                  example: 0
                message:
                  description: successful if successful, exception message otherwise.
                  type: string
                  example: successful
                success:
                  type: boolean
                  description: True if successful, False otherwise.
                  example: True
                result:
                  description: result dictionary
                  properties:
                    words:
                      type: list
                      example: ["selam", "salam"]
    """
    request_body = check_and_get_parameters(["word", "length","include", "exclude"],
                                            request.get_json())
    base_service = BaseService()
    base_service.build_query_params(word=request_body["word"],
                                    length=request_body["length"])
    character_check = {
      "include" : request_body["include"],
      "exclude" : request_body["exclude"]
    }
    result_list = base_service.execute_query_fetchall(**character_check)

    return response_success(result_list=result_list).get_json()

#TODO : ADD TRY EXCEPT
# TODO : ADD CONTROL TO IF RESULT IF SUCCESS
"""
response

{
  "error_code": 0,
  "message": "successful",
  "result": {
    "result_list": {
      "result": [
        "salam",
        "selam"
      ]
    }
  },
  "success": true
}
"""