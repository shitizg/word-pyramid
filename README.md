# Word Pyramid API
This is a repo containing the code of a simple AWS Lambda Function to check if a word is a word pyramid.

This REST API WebService is registered via Amazon API Gateway in a test stage.


# Invoking Word Pyramid REST API via curl POST command
To invoke api, you may use curl command:

Full Usage:

curl -X POST -d "{\\"word\\":\\"${input_word}\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid


Example:

curl -X POST -d "{\\"word\\":\\"banana\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid


Sample Test Requests:

curl -X POST -d "{\\"word\\":\\"\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid
 - Should give error message as no input string was given

curl -X POST -d "{\\"word\\":\\"banana\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid
 - result = true

curl -X POST -d "{\\"word\\":\\"abbcccddddeeeeeffffff\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid
 - result = true

curl -X POST -d "{\\"word\\":\\"abbcccdddeeeeffff\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid
 - result = false

curl -X POST -d "{\\"word\\":\\"bandana\\"}" https://pqdcpajma3.execute-api.us-east-1.amazonaws.com/Test/pyramid
 - result = false



# To Run Unit Tests

1. Clone the repo
2. run command: 'pytest -vv tests/test_lambda_function.py' from base directory.
