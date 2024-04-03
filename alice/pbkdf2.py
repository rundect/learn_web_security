import hashlib
import secrets
import sys
import timeit

sys_argv = sys.argv[0]
iterations = 720000


def test():
    message = b'password'
    salt = secrets.token_bytes(16)
    hash_value = hashlib.pbkdf2_hmac('sha256',
                                     message,
                                     salt,
                                     iterations)
    print(hash_value.hex())


if __name__ == '__main__':
    seconds = timeit.timeit('test()', number=10, globals=globals())
    print('Seconds elapsed: %s' % seconds)
