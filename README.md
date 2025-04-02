# Anagram-Finder

## Description
This program groups words from an input list into anagram groups and prints them as separate groups. The program takes a file with a set of words, groups those that are anagrams, and outputs the result.

## Requirements
- Python 3.x (No external dependencies)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Grrame22/Anagram-Finder.git
    cd Anagram-Finder
    ```

2. **Create and activate a virtual environment** (optional, but recommended for isolation):
    - On Mac/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

## How to Run the Program

1. **Prepare the input file**:
    Create a text file named `sample.txt`, where each word is on a new line. For example:

    ```
    act
    cat
    race
    care
    tree
    bee
    ```

2. **Run the program**:
    Once you've prepared the file, you can run the program with the following command:
    ```bash
    python anagram.py sample.txt
    ```

    This will process the words in `sample.txt`, group anagrams together, and print the output in the console.

    **Example output:**
    ```
    act cat
    race care acre
    tree
    bee
    ```
    
## Author
[Natan](https://github.com/Grrame22)
