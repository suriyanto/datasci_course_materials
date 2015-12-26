import sys
import json

def read_scores(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	return scores

def sentiment_score(text, scores):
	return 0 if text == None else tweet_score(text, scores)

def tweet_score(text, scores):
	s = 0
	for w in text.split(" "):
		s = s + word_score(w, scores)
	return s	

def word_score(w, scores):
	return 0 if not(w in scores) else scores[w]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = read_scores(sent_file)
    for line in tweet_file:
    	print sentiment_score(json.loads(line).get("text"), scores)

if __name__ == '__main__':
    main()
