def scrape_website(url: str) -> dict:
    """
    Scrapes a webpage for its content

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        A simple dictionary containing the page's title, a summary, and the cleaned text.
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract Title
        if soup.title:
            title = soup.title.string
        else:
            title = "No Title Found"

        # Extract Summary
        summary_tag = soup.find('meta', attrs={'name': 'description'})
        if summary_tag and summary_tag.has_attr('content'):
            summary = summary_tag['content']
        else:
            summary = "No summary available."
        
        # Extract Body
        body = soup.find('body')
        if not body:
            raise ValueError("Could not find the body of the page.")

        # Clean Body
        tags_to_remove = ['nav', 'footer', 'header', 'aside', 'form', 'script', 'style', 'a']
        for tag_name in tags_to_remove:
            for tag in body.find_all(tag_name):
                tag.decompose()
            
        raw_text = body.get_text(separator=' ', strip=True)
        cleaned_text = re.sub(r'\n\s*\n', '\n\n', raw_text)

        return {
            "status": "success",
            "url": response.url,
            "title": title.strip(),
            "summary": summary.strip(),
            "content": cleaned_text.strip()
        }

    except Exception as e:
        return {
            "status": "error", "url": url, "title": None, "summary": None,
            "cleaned_text": None, "error_message": f"An error occurred: {e}"
        }


if __name__ == '__main__':
    test_url = "https://www.carwale.com/mahindra-cars/xuv-3xo/"
    
    scraped_data = scrape_website(test_url)

    if scraped_data['status'] == 'success':
        print(scraped_data)
        
    else:
        print(f"Scraping failed: {scraped_data['error_message']}")