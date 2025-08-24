"""Tests for app module."""

from app import add


def test_add():
    """Test add() returns correct result."""
    assert add(2, 3) == 5
