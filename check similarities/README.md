# Check Similarities

A Python text-analysis project that uses regular expressions and sets to analyze text files and measure how similar two texts are.

## Files

- `check similarities.py`: main program with all the functions.
- `stopwords.txt`: list of common English words (stop words) ignored when comparing texts.
- `michelle_speech.txt` and `melina_speech.txt`: two speeches used to test the similarity function.
- `obama's speech.txt`: speech used to test the most common words function.
- `hacker_news`: a large text file used to test the line-counting function.

## Functions

- `most_common_words(file, m)`: returns the `m` most frequent words in a file, with their counts.
- `clean_text(text)`: replaces everything that is not a letter or a digit with a space and converts the text to lowercase.
- `remove_support_words(cleaned_text)`: removes the stop words from a cleaned text.
- `check_similarities(file1, file2)`: compares two text files and returns a similarity score between 0 and 1.
- `repeated_words(file)`: returns the 10 most repeated words in a file.
- `find_the_number_of_lines(file)`: counts the lines that mention Python, JavaScript, and Java (not JavaScript), prints the results, and returns them as a tuple.

## How the similarity score works

1. Both texts are cleaned (lowercase, no punctuation).
2. Stop words are removed.
3. Each text is turned into a set of unique words.
4. The score is the number of words the two texts share divided by the total number of different words in both (Jaccard similarity):

```
similarity = shared words / all different words
```

A score of 0 means no words in common, and 1 means identical vocabulary.

## How to run

Make sure the text files are in the same folder as the script, then run:

```
python "check similarities.py"
```

## Concepts practiced

- Reading files with `open` and `with`
- Regular expressions with `re` (`findall`, `sub`)
- Counting with `collections.Counter`
- Sets (`intersection`, `union`)
- List comprehensions
