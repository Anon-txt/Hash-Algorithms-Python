#!/usr/bin/env python

import hashlib


def sha1(string):
    sha1 = hashlib.sha1(string).hexdigest()
    return sha1


def sha224(string):
    sha224 = hashlib.sha224(string).hexdigest()
    return sha224


def sha256(string):
    sha256 = hashlib.sha256(string).hexdigest()
    return sha256


def sha384(string):
    sha384 = hashlib.sha384(string).hexdigest()
    return sha384


def sha512(string):
    sha512 = hashlib.sha512(string).hexdigest()
    return sha512


def sha3_224(string):
    sha3_224 = hashlib.sha3_224()
    sha3_224.update(string)
    return sha3_224.hexdigest()


def sha3_256(string):
    sha3_256 = hashlib.sha3_256()
    sha3_256.update(string)
    return sha3_256.hexdigest()


def sha3_384(string):
    sha3_384 = hashlib.sha3_384()
    sha3_384.update(string)
    return sha3_384.hexdigest()


def sha3_512(string):
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(string)
    return sha3_512.hexdigest()


def md5(string):
    md5 = hashlib.md5(string).hexdigest()
    return md5


def blake2b(string):
    blake2b = hashlib.blake2b()
    blake2b.update(string)
    return blake2b.hexdigest()


def blake2s(string):
    blake2s = hashlib.blake2s()
    blake2s.update(string)
    return blake2s.hexdigest()
