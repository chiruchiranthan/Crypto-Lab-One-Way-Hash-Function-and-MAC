import random
import string
import hashlib
numTrials = 0

while True:
	randomString1 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(20)])
	randomString2 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in xrange(20)])
	if randomString1 == randomString2: 
		continue;
	else:
		hash_object_1 = hashlib.md5(randomString1.encode())
		hash_string_1 = hash_object_1.hexdigest()
		hash_object_2 = hashlib.md5(randomString2.encode())
		hash_string_2 = hash_object_2.hexdigest()
		numTrials += 1
		if (hash_string_1[0:6] == hash_string_2[0:6]):
			break;
print "num trials to break collision-resistant property = "
print numTrials
