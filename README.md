# Website Health Checker
[![CI Test](https://github.com/Saridi-The-Pro/Website-Health-Checker/actions/workflows/ci-test.yml/badge.svg)](https://github.com/Saridi-The-Pro/Website-Health-Checker/actions/workflows/ci-test.yml)

A lightweight and efficient Python CLI tool to monitor website availability, response times, and HTTP status codes.

## Overview
Website Health Checker is an open-source Python project designed to help users check whether a website is reachable and inspect its HTTP response.

## Key Features
* **Fast Checks**: Monitor HTTP/HTTPS status for single or multiple URLs instantly.
* **Automated CI/CD**: Fully tested and verified across a multi-environment GitHub Actions matrix (24/24 jobs passing).
* **Lightweight**: Built with minimal external dependencies, prioritizing CLI speed and reliability.

## Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/Saridi-The-Pro/Website-Health-Checker.git
cd Website-Health-Checker
pip install .
```

## Usage
Once installed, run `website-health-check` directly from your terminal:
```bash
# Check one or multiple URLs at once
website-health-check https://google.com https://github.com

# Set a custom response timeout limit in seconds (default: 5.0)
website-health-check https://example.com -t 3.0

# Display program version
website-health-check --version
```
Alternatively, you can run it via Python module:
```bash
python -m website_health_checker.cli https://example.com
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
