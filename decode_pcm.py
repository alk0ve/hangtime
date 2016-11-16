import argparse
import struct
import os
import glob

FIRST_DWORDS_TABLE = [0x7, 0x8, 0x9, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x10, 0x11, 0x13, 0x15, 0x17, 0x19, 0x1C, 0x1F,
                      0x22, 0x25, 0x29, 0x2D, 0x32, 0x37, 0x3C, 0x42, 0x49, 0x50, 0x58, 0x61, 0x6B, 0x76, 0x82,
                      0x8F, 0x9D, 0x0AD, 0x0BE, 0x0D1, 0x0E6, 0x0FD, 0x117, 0x133, 0x151, 0x173, 0x198, 0x1C1,
                      0x1EE, 0x220, 0x256, 0x292, 0x2D4, 0x31C, 0x36C, 0x3C3, 0x424, 0x48E, 0x502, 0x583, 0x610,
                      0x6AB, 0x756, 0x812, 0x8E0, 0x9C3, 0x0ABD, 0x0BD0, 0x0CFF, 0x0E4C, 0x0FBA, 0x114C, 0x1307,
                      0x14EE, 0x1706, 0x1954, 0x1BDC, 0x1EA5, 0x21B6, 0x2515, 0x28CA, 0x2CDF, 0x315B, 0x364B,
                      0x3BB9, 0x41B2, 0x4844, 0x4F7E, 0x5771, 0x602F, 0x69CE, 0x7462, 0x7FFF]

SECOND_DWORDS_TABLE = [-1, -1, -1, -1, 2, 4, 6, 8, -1, -1, -1, -1, 2, 4, 6, 8]

assert len(FIRST_DWORDS_TABLE) == (0x58+1)
assert len(SECOND_DWORDS_TABLE) == 0x10


def process_nibble(nibble, out_bytearray, state_a, state_b):
    multiplication_result = ((nibble & 7) * FIRST_DWORDS_TABLE[state_b]) >> 2
    state_b = state_b + SECOND_DWORDS_TABLE[nibble]

    if state_b < 0:
        state_b = 0
    elif state_b > 0x58:
        state_b = 0x58

    if (nibble & 8) == 8:
        # bit is on
        state_a -= multiplication_result
        if state_a < - 0x8000:
            state_a = 0x8000
    else:
        # bit is off
        state_a += multiplication_result
        if state_a > 0x7FFF:
            state_a = 0x7FFF

    signed_le_short = struct.pack('<h', state_a)
    for b in signed_le_short:
        out_bytearray.append(b)

    return state_a, state_b


def decode_file(file_in, file_out):
    with open(file_in, 'rb') as f:
        encoded_pcm = f.read()

    decoded_audio = bytearray()
    state_a = 0
    state_b = 0

    for b in encoded_pcm:
        b = ord(b)
        # first top nibble, then bottom
        state_a, state_b = process_nibble((b >> 4), decoded_audio, state_a, state_b)
        state_a, state_b = process_nibble((b & 0xF), decoded_audio, state_a, state_b)

    with open(file_out, 'wb') as f:
        f.write(decoded_audio)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="PCM file (or wildcard expression) to decode")
    args = parser.parse_args()

    input_files = glob.glob(args.input)

    for input_file in input_files:
        decode_file(input_file, os.path.splitext(input_file)[0] + '.raw')


if '__main__' == __name__:
    main()
