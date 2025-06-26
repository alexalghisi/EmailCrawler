'''
Created on Jun 26, 2025

@author: Alghisi Alessandro Paolo
'''

import argparse
from crawler import crawl_website, emails_found
from utils import export_to_csv
from colorama import Fore, Style

def main():
    parser = argparse.ArgumentParser(description="EmailCrawler - Extract emails from websites")
    parser.add_argument("url", help="Starting URL")
    parser.add_argument("--output", default="output/emails.csv", help="Path to save CSV results")
    args = parser.parse_args()

    print(Fore.CYAN + f"[INFO] Starting crawl: {args.url}")
    crawl_website(args.url)

    print(Style.BRIGHT + f"\n[INFO] Total emails found: {len(emails_found)}")
    export_to_csv(emails_found, args.output)
    print(Fore.GREEN + f"[OK] Emails saved to: {args.output}")

if __name__ == "__main__":
    main()
