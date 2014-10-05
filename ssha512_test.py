#!/usr/bin/python

from mailgenic.hashers import SSHA512PasswordHasher
import os
import hashlib
import getpass
import base64

password1 = None
password2 = None

while password1 != password2 or password1 == None:
    password1 = getpass.getpass()
    password2 = getpass.getpass("Confirm password: ")
    if (password1 != password2):
        print("\nPassword mismatch, try again.")

    hasher = SSHA512PasswordHasher()
    ssha512 = hasher.encode(password1, hasher.salt())

    print("\n{{SSHA512}}{}".format(ssha512))

    #verify test
    print(hasher.verify(password1, ssha512))
    print(hasher.safe_summary(ssha512))
