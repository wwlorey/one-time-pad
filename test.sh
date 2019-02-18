#!/bin/bash

./bin_otp_key_gen.py
./bin_otp.py keyfile.sec 50 input.txt encrypted.txt
./bin_otp.py keyfile.sec 50 encrypted.txt decrypted.txt