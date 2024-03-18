# Define a function syntax: def function_name(parameters)

def hello(language):
    print('Hello World in', language)


# call the function passing argument as a literal string
hello('Python')

language = input('Enter a language: ')
# call the function passing argument as a variable
hello(language)