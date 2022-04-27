from __future__ import absolute_import, division, print_function
__metaclass__ = type
from pyDes import triple_des, ECB, PAD_PKCS5
from sys import byteorder
key = [193, 171, 127, 121, 122, 214, 14, 234, 251, 199, 122, 199, 104, 50, 196, 44, 134, 21, 42, 148, 118, 50, 94, 254]
keybytes = b''.join([x.to_bytes(1,byteorder) for x in key])
k = triple_des(keybytes, mode=ECB, pad=None, padmode=PAD_PKCS5)
def encrypt(plaintext):
    return k.encrypt(plaintext).hex()
def decrypt(hexstring):
    return k.decrypt(bytes.fromhex(hexstring)).decode()

print(encrypt("password"))
class FilterModule(object):

    def filters(self):
        return {
            'ign_encrypt': encrypt,
            'ign_decrypt': decrypt,
        }
