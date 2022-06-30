POST_SCHEMA = {
    'type': 'object',
    'properties': {
        "bookingid": {"type": "number"}
    },
    'required': ["bookingid"]
}


POST_SCHEMA_R = {
    'type': 'object',
    'properties': {
        "text": {"type": "string"},
        "number": {"type": "number"},
        "type": {"type": "string"}
    },
    'required': ["text"]
}

# [{'bookingid': 2142},
