# web_scraping_agent

## Project Overview
The web scraping agent is a Python-based application designed to scrape web pages for information. It utilizes the `requests` library to handle HTTP requests and `BeautifulSoup` for parsing HTML content. The agent is configured to extract the title, summary, and cleaned text from specified web pages.

## File Structure
```
web_scraping_agent
├── agent
│   ├── __init__.py
│   ├── .env
│   ├── agent.py
│   └── web_scraping_tool.py
├── Dockerfile
└── README.md
```

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `google.adk`

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd web_scraping_agent
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install requests beautifulsoup4 google.adk
   ```

4. Set up environment variables:
   Create a `.env` file in the `agent` directory and add your `GOOGLE_API_KEY`:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage
To run the web scraping agent, execute the `agent.py` file:
```
python agent/agent.py
```

You can modify the `test_url` variable in `agent.py` to scrape different web pages.

## Docker Instructions
To build and run the Docker container:
1. Build the Docker image:
   ```
   docker build -t web_scraping_agent .
   ```

2. Run the Docker container:
   ```
   docker run -e GOOGLE_API_KEY=your_api_key_here web_scraping_agent
   ```

## License
This project is licensed under the MIT License.