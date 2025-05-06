from pagerank import transition_model, crawl
import sys

DAMPING = 0.85
SAMPLES = 10000

'''if len(sys.argv) != 2:
    sys.exit("Usage: python pagerank.py corpus")'''
#corpus = crawl(sys.argv[1])
#corpus = crawl('./corpus0')
corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}



print(corpus)
print(transition_model(corpus, '1.html', DAMPING))