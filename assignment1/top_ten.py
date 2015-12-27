import sys
import json

def hash_tags(entities):
	hts = [] if entities == None else entities.get('hashtags')
	return [ht.get('text') for ht in hts]

def merge(existing, new):
	if len(new) == 0:
		return existing

	r = dict([(k, v) for k, v in existing.iteritems()])
	for v in new:
		if v in r:
			r[v] = r[v] + 1
		else:
			r[v] = 1
	return r

def main():
    tweet_file = open(sys.argv[1])
    d = {}
    for line in tweet_file:
    	d = merge(d, hash_tags(json.loads(line).get("entities")))

    top_10 = sorted(d.iteritems(), key=lambda v: v[1])[-10:]
    for v in top_10:
    	print '%s %s' % (v[0], v[1])

if __name__ == '__main__':
    main()
