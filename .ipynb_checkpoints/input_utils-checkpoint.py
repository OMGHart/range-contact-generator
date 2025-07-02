def get_partial_number():
    while True:
        number = input("Enter a partial phone number (X to quit): ")
        if number.lower() == 'x':
            return None
        if number.isdigit():
            number = int(number)
            if number < 1000:
                print()
                print("Due to performance concerns, maximum numbers per request is 1,000,000.")
                print("Most mobile devices will not be capable of processing contacts of this size.")
                print("Proceed with caution.")
                print()
                print("Please enter at least 4 digits.\n")
                continue
            return int(number)
                
            
        else:
            print()
            print("Please enter digits only. No dashes, spaces, or other characters.\n")



