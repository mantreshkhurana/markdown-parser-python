# Markdown Worker

Markdown Worker is a versatile Python module for parsing, reading, and writing Markdown files. It simplifies the process of working with Markdown documents by providing a convenient interface for common tasks.

## Installation

You can install Markdown Worker via pip:

```bash
pip install markdown-worker
```

or

```bash
pip3 install markdown-worker
```

Alternatively, you can clone the GitHub repository:

```bash
git clone https://github.com/mantreshkhurana/markdown-worker-python.git
cd markdown-worker-python
```

## Features

- Read and parse Markdown files.
- Search for specific headers within a Markdown file.
- Retrieve content associated with a particular header.
- Convert Markdown to HTML.
- Simple and intuitive API.

## Usage

### Reading and Parsing Markdown Files

```python
from markdown_worker import MarkdownParser

# Initialize the parser with a Markdown file
parser = MarkdownParser("example.md")

# Read the entire file
markdown_content = parser.read_complete_file()

# Extract headers and paragraphs
headers, paragraphs, _ = parser.extract_headers_and_paragraphs()

# Print the extracted headers
print("Headers:", headers)

# Print the extracted paragraphs
print("Paragraphs:", paragraphs)
```

### Searching for a Header

```python
from markdown_worker import MarkdownParser

# Initialize the parser with a Markdown file
parser = MarkdownParser("example.md")

# Search for a specific header
heading_to_search = "Usage"
result = parser.search_heading(heading_to_search)

# Print the content under the searched header
print("Content under the heading:", result)
```

### Convert Markdown to HTML

```python
from markdown_worker import MarkdownParser

# Initialize the parser with a Markdown file
parser = MarkdownParser("example.md")

# Read the entire file
markdown_content = parser.read_complete_file()

# Convert Markdown to HTML
html_content = parser.markdown_to_html(markdown_content)

# Print the HTML content
print("HTML Content:", html_content)
```

## Example

An example Markdown file (`example.md`) is provided in the repository, containing documentation for the program.

## Author

- [Mantresh Khurana](https://github.com/mantreshkhurana)
