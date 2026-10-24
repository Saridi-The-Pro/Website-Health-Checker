import argsparse
from website_health_checker.checker import check_multiple_websites

def main():
    parser = argparse.ArgumentParser(
        description="An open-source Python library for real-time URL health checks and latency monitoring. Designed to be modular, lightweight, and freely reusable across any Python application or script."
    )
    parser.add_argument(
        "urls",
        nargs="+",
        help="One or more URLs to be checked (e.g., https://google.com)"
    )
    args = parser.parse_args()
    results = check_multiple_websites(args.urls)
    for result in results:
        status_tag = "HEALTHY" if result['status'] == "healthy" else "UNHEALTHY"
        print(f"[{status_tag}] {result['url']} - {result['response_time_ms']}ms (code: {result['status_code']})")

if __name__ == "__main__":
    main()