from pymd5 import md5
import urllib
import random
import string

def find_sub(text):
	or_found_idx = (text.find("'||'")
	return text[or_found_idx].is_digit()

i = 0
string_found = 0

while not string_found:
	text = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(40)])
	md5_text = md5(text)
	md5_text = md5_text.digest()
	string_found = find_sub(md5_text)
	i += 1
	if (i % 1000000 == 0):
		print i

print "Password = ", text
print "Hashed Password = ", md5_text
print "Found substring = ", string_found
