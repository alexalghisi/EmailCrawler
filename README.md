# EmailCrawler

A fast, multi-threaded tool to extract emails from websites, written in Python.

## Features

- Recursive crawling with configurable depth
- Regex-based email detection
- Thread-safe parallel crawling
- CSV output
- Modular structure with clear CLI

## Installation

git clone https://github.com/alexalghisi/EmailCrawler
cd EmailCrawler
pip install -r requirements.txt

# EmailCrawler

A fast, multi-threaded tool to extract emails from websites, written in Python.

## Features

- Recursive crawling with configurable depth
- Regex-based email detection
- Thread-safe parallel crawling
- CSV output
- Modular structure with clear CLI

## Installation

```bash
git clone https://github.com/alexalghisi/EmailCrawler
cd EmailCrawler
pip install -r requirements.txt
```
## Usage
To run the crawler, use the following command:

```
python main.py https://website.url
```
This will crawl the specified URL recursively and extract all valid email addresses it finds.

# Optional arguments:

```
--output <path>: Path to the CSV output file. Default is output/emails.csv.
```
### Example:

```
python main.py https://example.com --output output/example-emails.csv
```
After completion, the results will be saved as a CSV file.
