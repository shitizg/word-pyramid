from lambdas.lambda_function import *
from tests import *


def test_error_scenario_lambda_function():
    event = {
        'word': ""
    }
    resp = lambda_handler(event, None)
    assert resp == {
            'statusCode': 200,
            'body': {
                'message': "Error processing word. Please provide a string value for key 'word' in request body."
            }
    }

def test_success_banana_scenario_lambda_function():
    event = {
        'word': "banana"
    }
    resp = lambda_handler(event, None)
    assert resp == {
        'statusCode': 200,
        'body': {
            'input_word': "banana",
            'result': True,
            'message': "Input word 'banana' is a word pyramid."
        }
    }

def test_valid_words_is_pyramid():
    assert is_pyramid("banana") == True
    assert is_pyramid("abbcccddddeeeeeffffff") == True
    assert is_pyramid("noo") == True
    assert is_pyramid("monanoaoaa") == True
    assert is_pyramid("i") == True

def test_invalid_words_is_pyramid():
    assert is_pyramid("bandana") == False
    assert is_pyramid("robobor") == False
    assert is_pyramid("no") == False
    assert is_pyramid("abbcccddddd") == False