# text_summarizer

Note: I am working on adding some cool features such as abstraction summary, sentiment analysis and so much more!!

## Getting Started
Steps to get started on deploying this project on the local machine.

### Prerequisites
This project was developed in python 3.7, it is recommended to create virtual environment to manage dependencies required.

### Installing
Create virtual environment (note: must have virtualenv installed)

```python3 -m virtualenv venv```

Activate virtual environment 

```source venv/bin/activate```

Navigate to the app directory and download the dependencies

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

