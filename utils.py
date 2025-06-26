import re
import csv
import os
from urllib.parse import urlparse

email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

def extract_emails(text):
    """Return all email matches found in text"""
    return set(email_regex.findall(text))

def is_valid_url(url):
    """Return True if the URL is HTTP/HTTPS"""
    try:
        result = urlparse(url)
        return result.scheme in ["http", "https"]
    except:
        return False

def export_to_csv(emails, output_path):
    """Write unique emails to CSV"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Email"])
        for email in sorted(emails):
            writer.writerow([email])
