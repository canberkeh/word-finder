from flask import jsonify


def check_and_get_parameters(parameter_names: [str], json_body) -> dict:
    """
    Takes an array of parameter names and a json (dict) object in which to search for them.
    If it cannot find one of them it raises exception.
    :param parameter_names:
    :param json_body:
    :return:
    """
    result_dict = {}
    for parameter_name in parameter_names:
        if parameter_name in json_body:
            result_dict.update({parameter_name: json_body[parameter_name]})
        else:
            print("error! ")
    return result_dict

def response_success(**kwargs):
    """simplifier for successful response object preparation"""
    return jsonify(success=True, message="successful", error_code=0, result=kwargs)

#TODO : ADD EXCEPTION TO check_and_get_parameters