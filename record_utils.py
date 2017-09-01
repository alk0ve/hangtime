import binascii
import argparse
import re

LETTER_SHIFT = ord('A') - 1
DIGIT_SHIFT = ord('0') - 1


def print_all_passwords(records, verbose=False):
    for offset in xrange(0, len(records), 0x78):
        # name at offset +0x10, password at offset +0x16
        # validate them first
        valid_entry = True

        for letter in records[offset + 0x10: offset + 0x16]:
            if not (1 <= ord(letter) <= 27):
                valid_entry = False
                break

        for digit in records[offset + 0x16: offset + 0x1A]:
            # 0 means a space
            if not (0 <= ord(digit) <= 10):
                valid_entry = False
                break
        if not valid_entry and verbose:
            print "ENTRY AT 0x%x invalid, skipping" % offset
            continue

        name = ''.join([chr(ord(c) + LETTER_SHIFT) for c in records[offset + 0x10: offset + 0x16]])
        password = ''.join([chr(ord(c) + DIGIT_SHIFT) for c in records[offset + 0x16: offset + 0x1A]])

        print "0x%x: %s: %s [%s]" % (offset, name, password, binascii.hexlify(records[offset + 0x10: offset + 0x1A]))


def find_silly_passwords(records):
    # find all potential character names with passwords that have four repeating digits
    # each digit is encoded as its value + 1
    for password_digit in xrange(10):
        pattern = chr(password_digit + 1) * 4
        indices = [m.start() for m in re.finditer(pattern, records)]

        for index in indices:
            # validate index
            if index < 6:
                continue
            # validate name letters
            letters_valid = True
            for c in records[index - 6: index]:
                if not (0 <= ord(c) <= 27):
                    letters_valid = False
                    break
            if not letters_valid:
                # skip this instance
                continue
            # print the previous six characters
            # each character is encoded by its 1-based index in the alphabet
            # so A is 1, B is 2, etc.
            name = ''.join([chr(ord(c) + LETTER_SHIFT) for c in records[index - 6: index]])
            password = ''.join([chr(ord(c) + DIGIT_SHIFT) for c in records[index: index + 4]])
            print "0x%x: %s: %s [%s]" % (index, name, password, binascii.hexlify(records[index - 6: index + 4]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("record_bin_path",
                        help="Location of RECORD.BIN")
    args = parser.parse_args()

    with open(args.record_bin_path, 'rb') as f:
        records_content = f.read()

    # find_silly_passwords(records_content)
    print_all_passwords(records_content)


if __name__ == "__main__":
    main()
