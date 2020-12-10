# Summarizer Tool: Did You Really Read It? 

This Natural Language Processing project called the "Summarizer Tool" evaluates whether a student has read the reading. We approach by evaluating the quality of the student's summary of the reference text. In research lingo, the Summarizer Tool is an automated summarization evaluation (ASE) tool. 

How it's designed: 
This tool is designed to be generalizable in its ability to accurately assess summaries from new texts. This code is intended for low-risk assessments, determining whether the student receives a pass or fail for the reading summary. 

## Installation

You can run a prototype of the Summarizer Tool <strong>on the branch called "site".</strong> Once you have installed npm, Node.js, and Express, clone the repository into your directory. Remember to switch from master to site! 

```bash
git checkout site
npm install
npm run start
```

## File Structure 
The prototype of the summarization tool is stored in the branch called "site". Below is an explanation of the files in master. The prototype only runs `lsa_with_news_corpus.py`

<strong>Current Version - Using LSA to assess document similarity</strong>


* `lsa_with_news_corpus` - The main technique is Latent Semantic Analysis from the Gensim package, based on the [similarity query tutorial](https://radimrehurek.com/gensim/auto_examples/core/run_similarity_queries.html). The model uses the 20 Newsgroup corpus and incorporates the student's reference text on the spot. These texts are transformed into an LSA space where the similarity between the student response and the reference text is calculated using cosine similarities. 


* `clean_newspaper_corpus.py` - Prepares the corpus using ~3K texts from the [20 Newsgroup] (http://qwone.com/~jason/20Newsgroups/) The code combines text files from science folders into a CSV file.

<strong>Version 1 - Calculating Exact Matches to Predefined Rubric</strong>

* `correctness_on_defined_rubric.py` - Initial version of the code: to score the summaries based on exact matches to a predefined rubric. Eg. if the student response contains two phrases in the rubric, the score is two. Each rubric item is only counted once. Limitations: this code relies on a predefined rubric. 


<strong>Version 2 - Impromptu Rubric </strong>

* `create_and_score_on_impromptu_rubric.py` - Creates an impromptu rubric from the reference text and scores the student response based on that. Currently, the rubric is the top 15 most common words in the reference text. The next step for implementation is to expand the rubric from words to phrases. An idea is to determine which phrases best capture the idea of the meaningful word. ie. There are 15 repetitions of sausage, and you want the phrase "pack into sausage" as the rubric, rather than "sausage with what" 



## Reflections for next steps 
<strong>Version 1</strong>: The code is a straightforward approach to scoring the summary based on a predefined rubric. There are two issues: it relies on an expert to create a rubric. To improve this code, I suggest: 

1. Implement stemming and lemmatization for the rubric and student response for greater score accuracy


2.  Include a plagiarism checker, especially for direct quotes. 

<strong>Version 2</strong>: The idea of Version 2 is to create an impromptu rubric is a potential research area that allows for accurate scoring without intensive computational techniques. 


<strong>Current Version</strong>: The current version of the code relies heavily on document similarity to assess the quality of the summary, which should not be the only indicator of summary quality.  
Another issue is that the current implementation of the LSA has a limited score distribution, ranging above 0.90 from a -1 to 1 similarity scale. A solution that was attempted was to fine-tune the number of topics, but no improvement was found. I suspect this issue can also be attributed to our small corpus. 
Lastly, here's a list of ideas for further implementation: 

* incorporating lemmatization and stemming
* word2vec to assess student summary
* plagiarism check with Levenshtein distance
* a larger corpus (We attempted using TASA but we could not rebuild the model with reference text since it is a predefined LSA space and documents for corpus were inaccessible) 

For reference on related projects, there is an open-source tool called [SEMILAR](http://www.semanticsimilarity.org/) for assessing the similarity of texts. Another project that is most related is [Allen, Crossley, Kim et. al's work on ASE Using Natural Language Processing Tools](https://www.researchgate.net/publication/333909045_Automated_Summarization_Evaluation_ASE_Using_Natural_Language_Processing_Tools) 

## Acknowledgements
Credits to the team: The Learning Agency, Erica Snow, Matt Jacovina, and Katrina Yu

## Project Status 
This project will be continued by another team at the Learning Agency. 
