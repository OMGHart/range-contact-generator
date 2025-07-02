def get_label(number):
    range_power = 10-len(str(number))
    input_num = str(number)
    input_num += 'X' * range_power
    area_code = input_num[:3]
    exchange = input_num[3:6]
    line_num = input_num[6:]
    formatted_num = f'{area_code}-{exchange}-{line_num}'
    label = f'Blocked Range {formatted_num}'
    return label

def generate_number_list(number):
    range_power = 10-len(str(number))
    block_len = 10 ** range_power
    init_num = int(block_len) * number
    stop_num = init_num+block_len
    return list(range(init_num, stop_num))

    
def export_vcard(numbers, label):
    formatted_numbers = [
        f'TEL;type=CELL;type=VOICE:{num}' for num in numbers
    ]
    num_string = '\n'.join(formatted_numbers)
    vcf_content = f"""BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//macOS 15.5//EN
N:;{label};;;
FN:{label}
{num_string}
END:VCARD
    """

    with open(f'{label}.vcf', 'w') as f:
        f.write(vcf_content)
    print()
    print(f"Contact '{label}.vcf' exported successfully!")
    print()

