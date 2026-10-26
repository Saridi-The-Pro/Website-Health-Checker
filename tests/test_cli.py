from unittest.mock import patch
import pytest
from website_health_checker.cli import main

@patch("website_health_checker.cli.check_multiple_websites")
def test_cli_success(mock_check, capsys):
    mock_check.return_value = [
        {"url": "https://example.com", "status": "healthy", "status_code": 200, "response_time_ms": 120.0}
    ]
    with patch("sys.argv", ["cli.py", "https://example.com"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 0

    captured = capsys.readouterr()
    assert "https://example.com" in captured.out

@patch("website_health_checker.cli.check_multiple_websites")
def test_cli_failure(mock_check):
    mock_check.return_value = [
        {"url": "https://invalid.test", "status": "error", "status_code": "N/A", "response_time_ms": "N/A"}
    ]
    with patch("sys.argv", ["cli.py", "https://invalid.test"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1