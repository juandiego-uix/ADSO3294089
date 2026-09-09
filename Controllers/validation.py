def missing_fields(data, required_fields):
    return [
        field
        for field in required_fields
        if field not in data
        or data[field] is None
        or (isinstance(data[field], str) and not data[field].strip())
    ]