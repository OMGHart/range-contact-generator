from input_utils import get_partial_number
from contact_utils import get_label, generate_number_list, export_vcard
import argparse

def main():
    print()    
    print()
    print("Welcome to Hart's phone number range contact generator!")
    print()  
    print("This program will generate a contact with every number in the requested range.")
    print("To block a range: add the contact to your device, and block the contact!")
    print()    
    print()

    parser = argparse.ArgumentParser(description='Generate a contact with a range of numbers.')
    parser.add_argument('--prefix', type=int, help='Partial phone number.')
    args = parser.parse_args()

    
    # number = args.prefix if args.prefix else get_partial_number()
    if args.prefix:
        number = args.prefix
        if number < 1000:
            print()
            print("Due to performance concerns, maximum numbers per request is 1,000,000.")
            print("Most mobile devices will not be capable of processing contacts of this size.")
            print("Proceed with caution.")
            print()
            print("Please set prefix to at least 4 digits.\n")
            return
    else:
        number = get_partial_number()
    
    if number is None:
        print("Exiting.")
        return
        
    label = get_label(number)
    numbers = generate_number_list(number)
    export_vcard(numbers, label)

if __name__ == "__main__":
    main()

# Test change with save.
    