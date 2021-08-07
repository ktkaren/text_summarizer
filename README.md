# text_summarizer

What is a text summarizer? Well, right now it's a tool that takes a chunk of text and spits out an abstraction summary. I am working on adding some cooler features such as extraction summary, sentiment analysis and so much more!!

## Getting Started
Steps to get started on deploying this project on the local machine.

### Prerequisites
This project was developed in python 3.7, it is recommended to create virtual environment to manage dependencies required.

### Installing
Create Virtual Environment 

```python3 -m virtualenv venv```

Activate Virtual Environment 

```source venv/bin/activate```

Download the Dependencies

```./setup.sh```

### Running the function
In your main.py, import summarize function by writing "from PATH.summarize import summarize" and replace 'PATH' with your path to summarize.py

The summarize function expext two parameters (the text you want to summarize and the number of sentences you want to summary to be) and return the summary as a string.

Function header of the summarize function:
```
def summarize(text, number_of_sentences):
    """
    Summarize the text to given number_of_sentences.

    :param text: string (the text being summarized)
    :param number_of_sentences: integer 
    (Must be non-negative. If greater than the total number of sentence in text, returns the whole text)
    :return: string (the summary)
    """
```

