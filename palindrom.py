def is_palindrom(input_string):
    if len(input_string) == 0:
        return False
    else:    
        return input_string == input_string[::-1]