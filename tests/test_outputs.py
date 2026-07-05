import json
from pathlib import Path


def load_report():
    report = Path("/app/report.json")
    assert report.exists(), "report.json not found"

    with report.open() as f:
        return json.load(f)


def test_total_requests():
    """Verify total request count."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Verify unique client IP count."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Verify most requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"