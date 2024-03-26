import streamlit as st
import nltk
from nltk.stem import PorterStemmer
import re
from collections import defaultdict
from nltk.tokenize import word_tokenize

# Streamlit app title
st.title("Boolean Retrieval System")

# Initialize the stemmer globally
stemmer = PorterStemmer()

# Sample documents (Replace with the actual documents or a method to upload documents)
documents = {
    1: """
    The quick brown fox jumps over the lazy dog. On a sunny day, in a quiet forest, a brown fox discovered a peaceful spot. 
    This spot was so serene that even the laziest dog wouldn't bother to disturb the quiet. 
    The fox, feeling adventurous, decided to explore beyond the known paths. 
    It was a decision that led to unexpected friendships and tales that would be told for generations.
    """,

    2: """
    Never jump over the lazy dog quickly. It's a lesson in patience and respect that every young animal learns. 
    In the heart of the bustling city, a dog finds solace in the small park where children play and adults stroll. 
    The dog, known for its laziness, is actually the wisest creature, observing life's pace and teaching those who pay attention about the value of slowing down. 
    """,

    3: """
    A quick brown fox. Not just any fox, but one that had tales of cunning and speed. 
    This fox, unlike any other in the forest, had seen the edges of the world and returned. 
    Its adventures spoke of distant lands, mystical creatures, and treasures that sparkled under the moonlight. 
    The fox, through its journey, learned the importance of wisdom, courage, and friendship.
    """
}

# Function to build an inverted index
def build_inverted_index(docs):
    inverted_index = defaultdict(set)
    for doc_id, text in docs.items():
        # Tokenization with normalization (lowercase)
        words = word_tokenize(re.sub(r'\W', ' ', text.lower()))
        for word in words:
            stemmed_word = stemmer.stem(word)
            inverted_index[stemmed_word].add(doc_id)
    return inverted_index

# Function to handle phrase queries and basic Boolean logic
def search(query, inverted_index, docs):
    # Add logic here for handling complex queries if needed
    # For now, we'll focus on phrase queries
    if '"' in query:
        phrase = re.findall('"([^"]*)"', query)[0]
        phrase_words = [stemmer.stem(word) for word in word_tokenize(phrase.lower())]
        candidate_docs = set.intersection(*(inverted_index[word] for word in phrase_words if word in inverted_index))
        final_docs = []
        for doc_id in candidate_docs:
            text = docs[doc_id].lower()
            if all(word in text for word in phrase_words):
                final_docs.append(doc_id)
        return final_docs
    else:
        # Basic Boolean logic (AND, OR, NOT) handling could be added here
        pass

# Building the inverted index
inverted_index = build_inverted_index(documents)

# Streamlit user input for queries
user_query = st.text_input("Enter your search query:")

# Search button
if st.button("Search"):
    # Perform search
    result_docs = search(user_query, inverted_index, documents)
    if result_docs:
        st.write("Documents matching the query:")
        for doc_id in result_docs:
            st.write(f"Document {doc_id}: {documents[doc_id]}")
    else:
        st.write("No documents match your query.")
