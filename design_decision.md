# Design Decision

## Approach and Reasoning
This program processes a large number of words and groups them into anagrams efficiently. The core idea is to use a dictionary where the key is a sorted tuple of letters from each word. This approach allows quick lookup and grouping of anagrams with minimal processing overhead.

## Maintainability
- The code is structured with clear function separation, making it easy to modify or extend.
- The use of built-in Python features like `defaultdict` keeps the code concise and readable.
- The input is read in a streaming fashion to handle large files without excessive memory usage.
- The program separates anagram groups from words without anagrams to ensure correct output formatting.

## Scalability Considerations
**Handling 10 million words**: The current implementation already supports large datasets by reading words one at a time instead of loading everything into memory. Using a dictionary for grouping ensures efficient performance, even with millions of words.

- **Handling 100 billion words (large datasets)**: To scale further, additional techniques would be needed:
  
  - Using a database or key-value store instead of an in-memory dictionary to avoid memory constraints.
  - Implementing parallel processing (e.g., using Python’s `multiprocessing`) to process large datasets more efficiently.
  - Storing intermediate results in external storage (e.g., disk or a distributed system) to prevent memory overflow.
 
## Performance
- Using `tuple(sorted(word))` as a dictionary key ensures quick comparisons and avoids unnecessary string operations.
- Grouped words are stored in a dictionary instead of performing repeated searches, reducing computation time.
- Sorting groups before output ensures consistent order while minimizing performance costs.
- QuickSort and MergeSort were not used because Python’s built-in `sorted()` function is highly optimized and provides better performance for this specific use case.

## External Libraries
The program relies only on Python’s built-in `collections.defaultdict`, which improves readability and performance without adding unnecessary dependencies.
