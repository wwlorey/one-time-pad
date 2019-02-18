#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


# Constants
DEFAULT_KEY_FILE_NAME = 'keyfile.sec'
DEFAULT_KEY_INDEX = 0
DEFAULT_INPUT_FILE_NAME = 'input.txt'
DEFAULT_OUTPUT_FILE_NAME = 'output.txt'


def encrypt_message(key, message):
    """Returns an XOR encrypted version of message."""
    encrypted_message = b''
    message = message.encode()
    key = key.encode()
    
    for i in range(len(key)):
        encrypted_message += str(message[i] ^ key[i]).encode()
    
    return encrypted_message.decode()


if __name__ == '__main__':
    # Ensure the expected number of command line arguments is provided
    if len(sys.argv) == 4:
        key_file_name = sys.argv[1]
        key_index = int(sys.argv[2]) - 1
        input_file_name = sys.argv[3]
        output_file_name = sys.argv[4]

    else:
        # Incorrect number of command line arguments
        # Use defaults
        key_file_name = DEFAULT_KEY_FILE_NAME
        key_index = DEFAULT_KEY_INDEX
        input_file_name = DEFAULT_INPUT_FILE_NAME
        output_file_name = DEFAULT_OUTPUT_FILE_NAME        
        
    with open(key_file_name, 'r') as key_file:
        key = key_file.read().split('\n')[key_index]
        
    with open(input_file_name, 'r') as input_file:
        message = input_file.read()
    
    encrypted_message = encrypt_message(key, message)

    with open(output_file_name, 'w') as output_file:
        output_file.write(str(encrypted_message))
    