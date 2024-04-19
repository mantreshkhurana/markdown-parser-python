from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'A simple markdown parsing package.'
LONG_DESCRIPTION = 'Markdown Worker is a versatile Python module for parsing, reading, and writing Markdown files. It simplifies the process of working with Markdown documents by providing a convenient interface for common tasks.'

# Setting up
setup(
    name="markdown_worker",
    version=VERSION,
    author="Mantresh Khurana",
    author_email="<mantreshkhurana@spyxpo.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'mantresh khurana', 'parser', 'markdown'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)