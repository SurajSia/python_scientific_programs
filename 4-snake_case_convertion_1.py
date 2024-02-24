# this python is used to take the pascal or camel string as an input and the
# output will be the form of a clean snake case program
def convert_to_snake_case(pascal_or_camel_cased_string):

    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_char= '_' + char.lower()
            snake_char_list.append(converted_char)
        else:
            snake_char_list.append(char)
    #snake_case_string=''.join(snake_char_list)
    #clean_snake_case_string=snake_case_string.strip('_')
    #return clean_snake_case_string
    

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

    

if __name__ == '__main__':
    main()
