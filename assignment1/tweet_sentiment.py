import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def read_scores(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	return scores

def sentiment_score(text, scores):
	if text != None:
		s = 0
		for w in text.split(" "):
			s = s + word_score(w, scores)
		return s
	else:
		return 0

def word_score(w, scores):
	s = scores.get(w)
	return 0 if (s == None) else s

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    # lines(sent_file)
    # lines(tweet_file)
    scores = read_scores(sent_file)
    for line in tweet_file:
    	print sentiment_score(json.loads(line).get("text"), scores)

if __name__ == '__main__':
    main()
