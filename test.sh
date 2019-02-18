#!/bin/bash

KEY_ID='5'

./bin_otp_key_gen.py
./bin_otp.py keyfile.sec $KEY_ID input.txt encrypted.txt
./bin_otp.py keyfile.sec $KEY_ID encrypted.txt decrypted.txt
diff input.txt decrypted.txt