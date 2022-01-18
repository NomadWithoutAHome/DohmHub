# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = latestdata_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Latest:
    author: str
    time: str
    title: str
    url: str

    def __init__(self, author: str, time: str, title: str, url: str) -> None:
        self.author = author
        self.time = time
        self.title = title
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Latest':
        assert isinstance(obj, dict)
        author = from_str(obj.get("author"))
        time = from_str(obj.get("time"))
        title = from_str(obj.get("title"))
        url = from_str(obj.get("url"))
        return Latest(author, time, title, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["author"] = from_str(self.author)
        result["time"] = from_str(self.time)
        result["title"] = from_str(self.title)
        result["url"] = from_str(self.url)
        return result


class Latestdata:
    latest: List[Latest]

    def __init__(self, latest: List[Latest]) -> None:
        self.latest = latest

    @staticmethod
    def from_dict(obj: Any) -> 'Latestdata':
        assert isinstance(obj, dict)
        latest = from_list(Latest.from_dict, obj.get("Latest"))
        return Latestdata(latest)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Latest"] = from_list(lambda x: to_class(Latest, x), self.latest)
        return result


def latestdata_from_dict(s: Any) -> Latestdata:
    return Latestdata.from_dict(s)
