
# Boolean Retrieval System

## Overview

This Boolean Retrieval System provides a simple yet powerful way to search through a collection of documents using Boolean search queries. It supports exact phrase queries and can be easily extended to handle more complex searches involving logical operators such as AND, OR, and NOT. Built with Python and Streamlit, this project showcases a basic implementation of the Boolean retrieval model, foundational to understanding search engines and information retrieval systems.

## Features

- **Exact Phrase Search**: Search for documents containing an exact sequence of words.
- **Normalization**: Converts all text to lowercase to ensure case-insensitive matching.
- **Stemming**: Reduces words to their root form, enabling the matching of different forms of a word.
- **Web Interface**: A simple and user-friendly web interface powered by Streamlit, allowing users to input search queries and view matching documents.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip

### Setup

1. **Clone the repository**:

   ```bash
   git clone git@github.com:Sohoxic/Boolean-Retrieval-System.git
   cd boolean-retrieval-system
   ```

2. **Install dependencies**:

   - It's recommended to create a virtual environment:

     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

   - Install the required packages:

     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

   Navigate to the URL provided in your terminal to interact with the application.

## Usage

Once the application is running, you can perform searches by entering queries into the search box on the web interface. The system currently supports exact phrase searches. To search for an exact phrase, enclose the phrase in double quotes (e.g., `"quick brown fox"`).

## Extending the Project

- **Complex Boolean Queries**: Enhance the search functionality to handle complex Boolean queries involving AND, OR, and NOT operators.
- **Ranking Results**: Implement a ranking mechanism to order the search results based on relevance.
- **Document Upload**: Add functionality to upload and index new documents through the web interface.

## Contributing

Contributions to the Boolean Retrieval System are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NLTK](https://www.nltk.org/), for providing the tools for text processing.
- [Streamlit](https://streamlit.io/), for making it easy to create web apps for machine learning projects.
