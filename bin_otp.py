#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


# Constants
DEFAULT_KEY_FILE_NAME = 'keyfile.sec'
DEFAULT_KEY_INDEX = 0
DEFAULT_INPUT_FILE_NAME = 'input.txt'
DEFAULT_OUTPUT_FILE_NAME = 'output.txt'


def encrypt_message(key, message):
    """Returns an XOR encrypted version of message.
    
    Where key is a binary string and message is an ASCII string with a length
    larger than or equal to the byte length of the key.
    """
    # Chunk 8 bits at a time from key and convert them to ints
    # Store these in the key_bytes_list
    key_bytes_list = []
    for byte_index in range(0, len(key) - 1, 8):
        key_bytes_list.append(int(key[byte_index:byte_index + 8], 2))
    
    # Do the same for characters in the message
    message_bytes_list = []
    for char in message[:len(key_bytes_list)]:
        message_bytes_list.append(ord(char))
    
    assert len(message_bytes_list) == len(key_bytes_list), 'Error in message length'    

    # XOR the two lists element by element
    encrypted_bytes_list = []
    for i in range(len(key_bytes_list)):
        encrypted_bytes_list.append(message_bytes_list[i] ^ key_bytes_list[i])
    
    # Convert to ASCII & return
    return ''.join([chr(n) for n in encrypted_bytes_list])


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
        key = key_file.read().split('\n')[key_index].split()[1]
        
    with open(input_file_name, 'r') as input_file:
        message = input_file.read()
    
    encrypted_message = encrypt_message(key, message)

    with open(output_file_name, 'w') as output_file:
        output_file.write(encrypted_message)
    