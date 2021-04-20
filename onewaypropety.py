import random
import string
import hashlib
HASH_VALUE = '286755'
numTrials = 0

while True:
	randomStr = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(20)])
	hash_object = hashlib.md5(randomStr.encode())
	hash_string = hash_object.hexdigest()
	numTrials += 1
	if hash_string[0:6] == HASH_VALUE:
		break;
print "num trials to break one-way property = "
print numTrials
