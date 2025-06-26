import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from utils import extract_emails, is_valid_url
from config import MAX_DEPTH, MAX_THREADS, USER_AGENT, TIMEOUT
from colorama import Fore

emails_found = set()
visited_urls = set()
lock = Lock()

def get_page_content(url):
    """Fetch page HTML content safely"""
    try:
        headers = {"User-Agent": USER_AGENT}
        res = requests.get(url, headers=headers, timeout=TIMEOUT)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        return ""
    return ""

def crawl(url, depth):
    """Crawl a URL and collect emails + links recursively"""
    if depth > MAX_DEPTH:
        return

    with lock:
        if url in visited_urls:
            return
        visited_urls.add(url)

    print(Fore.YELLOW + f"[{depth}] Crawling: {url}")
    html = get_page_content(url)
    if not html:
        return

    for email in extract_emails(html):
        with lock:
            if email not in emails_found:
                emails_found.add(email)
                print(Fore.GREEN + f"[✔] Found: {email}")

    soup = BeautifulSoup(html, "html.parser")
    links = {urljoin(url, a['href']) for a in soup.find_all("a", href=True)}
    links = filter(is_valid_url, links)

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for link in links:
            executor.submit(crawl, link, depth + 1)

def crawl_website(start_url):
    crawl(start_url, 0)
