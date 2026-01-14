# Use the re module to write a script that searches through a paragraph and extracts all
# words that start with an uppercase letter (e.g., "London", "Python") to identify proper
# nouns or sentence starters.

import re


paragraph = """
Python is a popular programming language. London is a beautiful city.
Many Developers love Python for its simplicity and versatility.
"""

uppercase_words = re.findall(r'\b[A-Z]\w*', paragraph)

print("Words starting with uppercase letters:")
print(uppercase_words)

