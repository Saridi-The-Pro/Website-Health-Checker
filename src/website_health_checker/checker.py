import time
import requests

ERRORS:dict = {
    requests.exceptions.MissingSchema: "Unknown domain protocol!",
    requests.exceptions.InvalidSchema: "Invalid protocol schema!",
    requests.exceptions.InvalidURL: "Invalid URL!",
    requests.exceptions.SSLError: "Security Certificate Problem!",
    requests.exceptions.ConnectTimeout: "Connection handshake timeout!",
    requests.exceptions.ReadTimeout: "Server took too long to respond!",
    requests.exceptions.ConnectionError: "Domain cannot be found or connection have been cut!",
    requests.exceptions.TooManyRedirects: "Too many redirects!",
    requests.exceptions.ChunkedEncodingError: "Connection broken during data transfer!"
}

HEADERS:dict = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def check_website(url: str, timeout: int = 5) -> dict:
    clean_url = url.strip()
    if not clean_url:
        return {
            "url": url,
            "status": "error",
            "status_code": None,
            "response_time_ms": None,
            "error": "URL cannot be empty!"
        }
    if not clean_url.startswith(("http://", "https://")):
        clean_url = "https://" + clean_url
    try:
        start_time = time.perf_counter()
        response = requests.get(clean_url, timeout=timeout, headers=HEADERS)
        duration = round((time.perf_counter() - start_time) * 1000, 2)
        return {
                "url": clean_url,
                "status": "healthy" if response.ok else "unhealthy",
                "status_code": response.status_code,
                "response_time_ms": duration,
                "error": None
                }
    except requests.exceptions.RequestException as e:
        error_msg = ERRORS.get(type(e), f"Error: Unexpected error ({e})")
        return {
            "url": clean_url,
            "status": "error",
            "status_code": None,
            "response_time_ms": None,
            "error": error_msg
        }

def check_multiple_website(urls: list[str], timeout: int = 5) -> list:
    results = []
    for url in urls:
        results.append(check_website(url, timeout=timeout))
    return results

if __name__ == "__main__":
    url = input("URL: ")
    try:
        result = check_website(url=url)
        print(f"URL: {result['url']}")
        print(f"Status: {result['status']}")
        print(f"Status Code: {result['status_code']}")
        print(f"Response Time: {result['response_time_ms']}")
        print(f"Error: {result['error']}")
    except Exception as e:
        print(f"Error: {e}")