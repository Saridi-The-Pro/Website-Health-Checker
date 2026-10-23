import time
import requests

errors = {
    requests.exceptions.MissingSchema: "Unknown domain protocol!",
    requests.exceptions.InvalidURL: "Invalid URL!",
    requests.exceptions.SSLError: "Security Certificate Problem!",
    requests.exceptions.Timeout: "Request timeout!",
    requests.exceptions.ConnectionError: "Domain cannot be found or connection have been cut!"
}

def check_website(url: str, timeout: int = 5):
    try:
        start_time = time.perf_counter()
        response = requests.get(url, timeout=timeout)
        duration = round((time.perf_counter() - start_time) * 1000, 2)
        return {
                "url": url,
                "status": "healthy" if response.ok else "unhealthy",
                "status_code": response.status_code,
                "response_time_ms": duration,
                "error": None
                }
    except requests.exceptions.RequestException as e:
        error_msg = errors.get(type(e), f"Error: Unexpected error ({e})")
        return {
            "url": url,
            "status": "error",
            "status_code": None,
            "response_time_ms": None,
            "error": error_msg
        }
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