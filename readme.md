ATME: Airline Topic Modeling Experiment

License: MIT License

Dataset Used: "Twitter US Airline Sentiment"

Purposes: 
- To practice and review knowledge in Python, SQL, and some Natural Language Processing Concepts.
- Experiment with Topic Modeling Techniques, see what the main topics are for Tweets targeted at certain Airline Companies

Process:
- Using the information of the "Twitter US Airline Sentiment" Dataset found at 
    https://www.kaggle.com/crowdflower/twitter-airline-sentiment/data#database.sqlite
    I first used the "preprocess.py" to separate the SQLITE file into .txt files by their company title, then also removed the 
    first word of each tweet because that is always the @company_name and is useless data that could interfere with future
    topic modeling techniques.
- I then used MALLET Topic Modeling found at http://mallet.cs.umass.edu/topics.php to import each company's text file into
    MALLET's internal format keeping the sequence and removing MALLET's stopwords. I then used the .mallet files created to
    build a topic model, one for each company with 20 topics each. The outputs as well as the .MALLET files are included in this repo.
    
Future Ideas:
- Use STTM methods to infer topic models: https://github.com/qiang2100/STTM, STTM is used specifically for tweets, but requires
    a large corpus to use as a referal, a larger Tweet dataset may be needed for this purpose.
- Use MALLET on the tweets of all companies together to infer a topic model consisting of tweets directed at airlines in general.
- Use PMI or some other topic modeling comparison technique to see what the topic models infered using MALLET have in common, some
    recurring themes in coherence, and what company's topic model has something unique about them.
