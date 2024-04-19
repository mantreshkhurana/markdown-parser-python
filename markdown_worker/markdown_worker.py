import re

class MarkdownParser:
    def __init__(self, filename=None):
        self.filename = filename
        self.markdown_text = self.read_markdown_file() if filename else ""

        self.lines = self.markdown_text.split('\n')

    def read_markdown_file(self):
        if self.filename and self.filename.endswith('.md'):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    markdown_text = file.read()
                return markdown_text
            except IOError:
                return "Error: unable to read the markdown file."
        else:
            return "Error: file is not a markdown file."

    def extract_headers_and_paragraphs(self):
        header_pattern = r'^#{1,6}\s(.+)$'
        paragraph_pattern = r'^([^#\n].+)$'

        headers = []
        paragraphs = []
        header_indices = []

        for index, line in enumerate(self.lines):
            header_match = re.match(header_pattern, line)
            paragraph_match = re.match(paragraph_pattern, line)
            
            if header_match:
                headers.append(header_match.group(1))
                header_indices.append(index)
            elif paragraph_match:
                paragraphs.append(paragraph_match.group(1))

        return headers, paragraphs, header_indices

    def search_heading(self, heading_to_search):
        headers, _, header_indices = self.extract_headers_and_paragraphs()

        if heading_to_search in headers:
            heading_index = headers.index(heading_to_search)
            start_index = header_indices[heading_index]
            if heading_index + 1 < len(header_indices):
                end_index = header_indices[heading_index + 1]
            else:
                end_index = len(self.lines)

            content = '\n'.join(self.lines[start_index:end_index])
            result = content
        else:
            result = "Heading not found in the markdown file."

        return result
    
    def read_complete_file(self):
        return self.markdown_text
    
    def read_line(self, line_number):
        if line_number < len(self.lines):
            return self.lines[line_number]
        else:
            return "Line number out of range."
        
    def read_word(self, line_number, word_number):
        if line_number < len(self.lines):
            words = self.lines[line_number].split(' ')
            if word_number < len(words):
                return words[word_number]
            else:
                return "Word number out of range."
        else:
            return "Line number out of range."
        
    def read_character(self, line_number, word_number, character_number):
        if line_number < len(self.lines):
            words = self.lines[line_number].split(' ')
            if word_number < len(words):
                characters = list(words[word_number])
                if character_number < len(characters):
                    return characters[character_number]
                else:
                    return "Character number out of range."
            else:
                return "Word number out of range."
        else:
            return "Line number out of range."
        
    def read_character_from_line(self, line_number, character_number):
        if line_number < len(self.lines):
            characters = list(self.lines[line_number])
            if character_number < len(characters):
                return characters[character_number]
            else:
                return "Character number out of range."
        else:
            return "Line number out of range."
        
    def read_character_from_file(self, character_number):
        if character_number < len(self.markdown_text):
            return self.markdown_text[character_number]
        else:
            return "Character number out of range."
        
    def read_word_from_line(self, line_number, word_number):
        if line_number < len(self.lines):
            words = self.lines[line_number].split(' ')
            if word_number < len(words):
                return words[word_number]
            else:
                return "Word number out of range."
        else:
            return "Line number out of range."

    def markdown_to_html(self, markdown_text, output_filename=None):
        markdown_text = re.sub(r'^(#+)(.*?)$', r'<h\1>\2</h\1>', markdown_text, flags=re.MULTILINE)

        markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_text)

        markdown_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown_text)

        markdown_text = re.sub(r'^\*\s(.*)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
        markdown_text = re.sub(r'(<li>.*<\/li>)+', r'<ul>\g<0></ul>', markdown_text)

        markdown_text = re.sub(r'^\d+\.\s(.*)$', r'<li>\1</li>', markdown_text, flags=re.MULTILINE)
        markdown_text = re.sub(r'(<li>.*<\/li>)+', r'<ol>\g<0></ol>', markdown_text)

        markdown_text = re.sub(r'`([^`]+)`', r'<code>\1</code>', markdown_text)

        if output_filename:
            try:
                with open(output_filename, 'w', encoding='utf-8') as output_file:
                    output_file.write(markdown_text)
            except IOError:
                return "Error: unable to write to the output file."

        return markdown_text
