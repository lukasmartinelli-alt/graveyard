import hashlib
import base64
from collections import OrderedDict
from django.contrib.auth.hashers import BasePasswordHasher, mask_hash, constant_time_compare

class SSHA512PasswordHasher(BasePasswordHasher):
    """
    Uses a password scheme that is compatible with Dovecot SSHA512.
    Code derived from https://gist.github.com/garrettreid/8329796
    """
    algorithm = "ssha512"
    iterations = 1

    def verify(self, password, encoded):
        """
        Checks if the given password is correct.
        All bytes after the first 64 Bytes belong to the salt.
        """
        decoded = bytearray(base64.b64decode(encoded))
        salt = decoded[64:].decode('utf-8')
        encoded2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded2)

    def encode(self, password, salt):
        """
        Creates an encoded database value
        The result is normally formatted as "algorithm$salt$hash" and
        must be fewer than 128 characters.
        """
        assert password is not None
        assert salt and '$' not in salt
        password = password.encode('utf-8')
        salt = salt.encode('utf-8')
        sha = hashlib.sha512()
        sha.update(password)
        sha.update(salt)
        ssha512 = base64.b64encode(sha.digest() + salt)
        return ssha512.decode('utf-8')

    def safe_summary(self, encoded):
        """
        Returns a summary of safe values
        The result is a dictionary and will be used where the password field
        must be displayed to construct a safe representation of the password.
        """
        decoded = bytearray(base64.b64decode(encoded))
        hash = decoded[:64]
        salt = decoded[64:]

        return OrderedDict([
             ('algorithm', self.algorithm),
             ('iterations', self.iterations),
             ('salt', salt[4:]),
             ('hash', hash[4:]),
        ])
