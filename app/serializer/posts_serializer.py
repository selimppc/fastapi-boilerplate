"""
posts serializer
"""


def post_serializer(post) -> dict:
    """
    post
    """
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["content"],
    }
