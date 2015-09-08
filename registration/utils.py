import uuid


def gen_code():
    """Generates 20 character referal code"""
    return str(uuid.uuid4()).replace("-", '')[:20]
