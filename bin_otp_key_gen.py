#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import codecs
from os import urandom
import sys


# Constants
DEFAULT_OUTPUT_FILE_NAME = 'keyfile.sec'
NUM_OTP_KEYS = 500
OTP_BIT_LEN = 2048
OTP_BYTE_LEN = OTP_BIT_LEN // 8


def get_bin_str(char):
    """Returns a length 8 binary string (w/o the leading '0b') 
    derived from char."""
    bit_str = bin(char)[2:]
    return '0' * (8 - len(bit_str)) + bit_str


if __name__ == '__main__':
    # Ensure the expected number of command line arguments is provided
    if len(sys.argv) == 2:
        output_file_name = sys.argv[1]

    else:
        # Incorrect number of command line arguments
        # Use defaults
        output_file_name = DEFAULT_OUTPUT_FILE_NAME        
    
    # Determine zero padding amount for key ids
    key_id_len = 0        
    num_otp_keys_copy = NUM_OTP_KEYS
    while num_otp_keys_copy:
        num_otp_keys_copy = num_otp_keys_copy // 10
        key_id_len += 1
    
    format_str = "{:0%id}" % key_id_len
    
    # Generate & write OTP keys
    with codecs.open(output_file_name, 'w', encoding='utf8') as output_file:
        for key_count in range(NUM_OTP_KEYS):
            key_id = format_str.format(key_count + 1)
            key_bytes = urandom(OTP_BYTE_LEN)
            key_bits = ''
            for char in key_bytes:
                key_bits += get_bin_str(char)

            # assert len(key_bits) == OTP_BIT_LEN, 'Error in bytes to bits conversion'

            output_file.write(key_id + ' ' + key_bits)
            
            # Prevent a trailing new line in the file
            if key_count < NUM_OTP_KEYS - 1:
                output_file.write('\n')
        
        print('Key written to', output_file_name)
