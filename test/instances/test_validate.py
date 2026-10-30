from pathlib import Path

from validate_entities import create_test_validate

TestValidate = create_test_validate(Path(__file__).parent, ignore=["local_execution"])
