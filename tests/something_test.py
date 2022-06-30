import requests

from configuration import SERVICE_URL, SERVICE_URL_R
from src.baseclasses.response import Response
# from src.schemas.post import POST_SCHEMA, POST_SCHEMA_R
from src.pydantic_schema.post import Post, Post_R


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate(Post)


def test_getting_posts2():
    r = requests.get(url=SERVICE_URL_R)
    response = Response(r)

    response.assert_status_code(200).validate(Post_R)
