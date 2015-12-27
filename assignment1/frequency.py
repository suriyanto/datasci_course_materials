import sys
import json
from sets import Set

excluded_words = Set(['', 'a', 'the', 'it', 'in', 'on', 'at', 'has', 'have', 'had', 'is', 'was', 'are', 'were', 'not', 'rt', 'don\'t', 'doesn\'t'])

def should_include_term(term):
	return not (len(term) == 1 or term.lower() in excluded_words or term.startswith(('#', '@')))

def line_freq(line):
	return [] if line == None else [(w, 1) for w in filter(lambda x: should_include_term(x.strip()), line.split(' '))]

def merge(existing, new):
	if len(new) == 0:
		return existing

	r = dict([(k, v) for k, v in existing.iteritems()])
	for k, v in new:
		if k in r:
			r[k] = r[k] + v
		else:
			r[k] = v
	return r

def main():
    tweet_file = open(sys.argv[1])
    freq = {}
    for line in tweet_file:
    	freq = merge(freq, line_freq(json.loads(line).get("text")))

    for k, v in freq.iteritems():
    	if v > 1:
    		print '%s %s' % (k, v)

if __name__ == '__main__':
    main()
