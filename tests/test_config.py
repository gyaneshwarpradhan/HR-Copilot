import pytest
from pydantic import ValidationError

from app.core.config import Settings, EnvironmentType


def test_default