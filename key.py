from bitcoin import *

my_private_key=random_key()

print("private Key:%s" % my_private_key)

my_public_key=privtopub(my_private_key)

print("public Key:%s" % my_public_key)