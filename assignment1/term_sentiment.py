import sys
import json
from sets import Set

def read_scores(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	return scores

excluded_words = Set(['', 'a', 'the', 'it', 'in', 'on', 'at', 'has', 'have', 'had', 'is', 'was', 'are', 'were', 'not', 'rt', 'don\'t', 'doesn\'t'])

def word_score(w, scores):
	return (w, 0) if not(w in scores) else (w, scores[w])

def term(text, scores):
	return [] if text == None else term_scores(text, scores)

def term_scores(text, scores):
	ws = [word_score(w, scores) for w in text.split(" ")]
	text_score = (sum(s for w, s in ws), len(filter(lambda x: x[1] != 0, ws)))
	return [(k, text_score) for k, v in filter(lambda x: x[1] == 0 and should_include_term(x[0]), ws)]

def should_include_term(term):
	return not (len(term) == 1 or term.lower() in excluded_words or term.startswith(('#', '@')))

def combine_term_scores(cummulative, term_scores):
	if len(term_scores) == 0:
		return cummulative
	term_dict = dict(term_scores)
	for k, v in cummulative.iteritems():
		if k in term_dict:
			term_dict[k] = merge_score(term_dict[k], v)
		else:
			term_dict[k] = v
	return term_dict

def merge_score(v1, v2):
	return (v1[0] + v2[0], v1[1] + v1[1])

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = read_scores(sent_file)
    new_term_scores = {}
    for line in tweet_file:
    	new_term_scores = combine_term_scores(new_term_scores, term(json.loads(line).get("text"), scores))
    for k, v in new_term_scores.iteritems():
    	if (v[1] != 0):
    		print '%s %s' % (k, v[0] / v[1])

if __name__ == '__main__':
    main()
