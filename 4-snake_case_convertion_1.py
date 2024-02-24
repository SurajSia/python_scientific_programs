#Python Program to convert a string in pascal or camel case into a clean snake case using string manipulation

#MIT License Board
#copyright(cc) @ GudalaSaiSuraj 
#Authorized By freecodecamp.org

def convert_to_snake_case(pascal_or_camel_case):
    
    snake_case_list = []    # declaring an empty list
    
    for char in pascal_or_camel_case:
        if char.isupper():
            
            converted_char='_' + char.lower()
            snake_case_list.append(converted_char)
        else:
            snake_case_list.append(char)
    
    return ''.join(snake_case_list).strip('_')

def main():
    
    string = 'aLongStringForExample'   # input was given in pascal-case i.e.;
                                       # needed to converted using fucntion call
    print(convert_to_snake_case(string))    

if __name__ == '__main__':
    main()
