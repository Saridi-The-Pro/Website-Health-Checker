import argparse
import sys
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
    has_failure = False
    for result in results:
        status_tag = result['status'].upper()
        if result['status'] != "healthy":
            has_failure = True
        response_time_ms = f"{result['response_time_ms']}ms" if result['response_time_ms'] is not None else "N/A"
        status_info = f"code: {result['status_code']}" if result['status_code'] is not None else f"reason: {result['error']}"
        print(f"[{status_tag}] {result['url']} - {response_time_ms} ({status_info})")

    sys.exit(1 if has_failure else 0)

if __name__ == "__main__":
    main()