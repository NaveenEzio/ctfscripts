#! /usr/bin/python


cipher = "\x1f \xeca_\xac\xef\xae\xffX F\x90\xacV\xcf\x9c\xab\x86W\xb1\xb9c\x06\xf9\x1c\xa6G\xb2\x96\xf3"
key = "yL\x8d\x06$\x9f\x97\xcd\x93-S/\xe6\xc5\"\xb6\xc3\x9f\xf2\x08\xd8\xcdVY\x9fu\xc8t\xc1\xe2\x8e"

def xor (a,b):
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(a,b))

decrypt =xor(cipher,key)
print(decrypt)



#####

def XORI(enc_message,key):
    dec_message = ""
    for i in range(len(enc_message)):
        dec_message = dec_message + chr(ord(enc_message[i])^ord(key[(lambda x,y:x%y if x%y >=0 else y)(i,len(key))]))
    return dec_message







