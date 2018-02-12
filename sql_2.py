from pymd5 import md5
from random import randint
import string, urllib

def find_sub(text):
	return "'='#" in text

i = 0
string_found = 0

while not string_found:
	text = str(randint(0,1000000000000000000000000000000000000000))
	#text = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(100)]
	md5_text = md5(text)
	md5_text = md5_text.digest()
	string_found = ("'='#" in md5_text)
	i += 1
	if (i % 1000000 == 0):
		print i

print "Password = ", text
print "Hashed Password = ", md5_text
print "Found substring = ", string_found
