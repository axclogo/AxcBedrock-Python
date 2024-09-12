from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# 原始 URL
original_url = "http://www.example.com?key1=value1"


def url_append_fields(url: str, fields: dict):
    """
    This function adds two numbers and returns the result.
    向url后追加参数
    Parameters:
    url (str): The url 
    fields (dict): Append fields 追加参数

    Returns:
    str: The new url 生成新的url
    """
    # parse url and fields
    url_parts = urlparse(url)
    original_fields = parse_qs(url_parts.query)
    # add new param for original fields
    for key, value in fields.items():
        original_fields[key] = value
    # the new url
    url_parts = url_parts._replace(
        query=urlencode(original_fields, doseq=True))
    return urlunparse(url_parts)
