#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from os import urandom
import sys


# Constants
DEFAULT_OUTPUT_FILE_NAME = 'keyfile.sec'
NUM_OTP_KEYS = 500
OTP_BIT_LEN = 2048
OTP_BYTE_LEN = OTP_BIT_LEN // 8



if __name__ == '__main__':
    # Ensure the expected number of command line arguments is provided
    if len(sys.argv) == 2:
        output_file_name = sys.argv[1]

    else:
        # Incorrect number of command line arguments
        # Use default file names
        output_file_name = DEFAULT_OUTPUT_FILE_NAME        
    
    # Generate & write OTP keys
    with open(output_file_name, 'w') as output_file:
        for _ in range(NUM_OTP_KEYS):
            output_file.write(str(urandom(OTP_BYTE_LEN)) + '\n')
