import secrets
import string
import time


def generate_code(value):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
    letters_and_digits) for i in range(value))
    return crypt_rand_string

# emulate sms sending
def delay_func(value):
    time.sleep(value)