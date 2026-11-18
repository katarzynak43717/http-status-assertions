def assert_json_keys(payload: dict, required: list[str]) -> None:
    missing = [k for k in required if k not in payload]
    assert not missing, f"Missing keys: {missing}"
