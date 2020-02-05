import json

def lambda_handler(event, context):
    
    word = event['word']
    
    if not word:
        return {
            'statusCode': 200,
            'body': {
                'message': "Error processing word. Please provide a string value for key 'word' in request body."
            }
        }

    result = is_pyramid(word)
    if (result) :
        message = ("Input word '%1s' is a word pyramid." % word)
    else: 
        message = ("Input word '%1s' is not a word pyramid!" % word)

    
    return {
        'statusCode': 200,
        'body': {
            'input_word': word,
            'result': result,
            'message': message
        }
    }


def is_pyramid(word):
    pyramid_dictionary = {}
    
    
    for letter in word:
        if letter in pyramid_dictionary.keys():
            pyramid_dictionary[letter] += 1
        else:
            pyramid_dictionary[letter] = 1
    
    counts = sorted(pyramid_dictionary.values())
    
    return all(counts[i] == i+1 for i in range(len(counts)))