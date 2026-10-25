from unittest.mock import patch, MagicMock
import pytest
import requests
from website_health_checker.checker import check_website, check_multiple_websites

def test_check_website_empty_url():
    result = check_website(" ")
    assert result["status"] == "ERROR"

@patch("website_health_checker.checker.requests.get")
def test_check_website_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.elapsed.total_seconds.return_value = 0.12
    mock_get.return_value = mock_response

    result = check_website("https://example.com", timeout=1.0)
    assert result["status"] == "HEALTHY"
    assert result["status_code"] == 200

@patch("website_health_checker.checker.requests.get")
def test_check_website_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    result = check_website("https://example.com", timeout=1.0)
    assert result["status"] in ["UNHEALTHY", "ERROR"]

@patch("website_health_checker.checker.requests.get")
def test_check_website_connection_error(mock_check):
    mock_check.side_effect = requests.exceptions.ConnectionError
    
    result = check_website("https://invalid-domain.test")
    assert result["status"] == "ERROR"

@patch("website_health_checker.checker.check_website")
def test_check_multiple_websites(mock_get):
    mock_get.return_value = {"url": "https://example.com", "status": "HEALTHY"}
    result = check_multiple_websites(["https://example.com", "https://google.com"])

    assert len(result) == 2
    assert mock_get.call_count == 2