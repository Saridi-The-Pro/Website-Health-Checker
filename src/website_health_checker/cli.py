import argparse
from website_health_checker.checker import check_multiple_websites

__version__ = "0.1.0"

def main():
    parser = argparse.ArgumentParser(
        description="An open-source Python library for real-time URL health checks and latency monitoring. Designed to be modular, lightweight, and freely reusable across any Python application or script."
    )
    parser.add_argument(
        "urls",
        type=str,
        nargs="+",
        help="One or more URLs to be checked (e.g., https://google.com)."
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=5.0,
        help="Response timeout limit in seconds (default: 5.0)."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Display program version."
    )
    args = parser.parse_args()
    results = check_multiple_websites(args.urls, timeout=args.timeout)
    for result in results:
        status_tag = "HEALTHY" if result['status'] == "healthy" else "UNHEALTHY"
        print(f"[{status_tag}] {result['url']} - {result['response_time_ms']}ms (code: {result['status_code']})")

if __name__ == "__main__":
    main()