#Credit/Debit Card Number Validation using numbers and string concepts with python programming
def verify_card_number(card_number): # function to validate the given number
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():                  # main function to read the users input , calling verifty_card_number function
    card_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number): # checks the validity and indvalidity by calling verifty_card_number function
        print('VALID!')
    else:
        print('INVALID!')

main()
