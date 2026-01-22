import httpx
from bs4 import BeautifulSoup

def scrape_website(url: str):
    print(f"--- Sentinel is visiting: {url} ---")
    
    # 1. Get the page content
    response = httpx.get(url)
    
    # 2. Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Remove script and style elements (we only want text)
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # 4. Get the text and clean up whitespace
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    clean_text = '\n'.join(chunk for chunk in chunks if chunk)

    print("--- Scrape Complete! ---")
    return clean_text[:500] # Return the first 500 characters as a test

if __name__ == "__main__":
    # Test it on a simple site
    test_url = "https://example.com"
    result = scrape_website(test_url)
    print(result)