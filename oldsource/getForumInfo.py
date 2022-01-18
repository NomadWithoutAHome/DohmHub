# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = latest_threads_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Datum:
    post_time: Optional[str] = None
    post_title: Optional[str] = None
    post_title_link: Optional[str] = None
    post_user: Optional[str] = None
    post_user_link: Optional[str] = None
    index: Optional[int] = None
    timestamp: Optional[int] = None
    uid: Optional[str] = None
    url: Optional[str] = None
    url_uid: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        post_time = from_union([from_str, from_none], obj.get("Post_Time"))
        post_title = from_union([from_str, from_none], obj.get("Post_Title"))
        post_title_link = from_union([from_str, from_none], obj.get("Post_Title_link"))
        post_user = from_union([from_str, from_none], obj.get("Post_User"))
        post_user_link = from_union([from_str, from_none], obj.get("Post_User_link"))
        index = from_union([from_int, from_none], obj.get("index"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        uid = from_union([from_str, from_none], obj.get("uid"))
        url = from_union([from_str, from_none], obj.get("url"))
        url_uid = from_union([from_int, from_none], obj.get("url_uid"))
        return Datum(post_time, post_title, post_title_link, post_user, post_user_link, index, timestamp, uid, url, url_uid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Post_Time"] = from_union([from_str, from_none], self.post_time)
        result["Post_Title"] = from_union([from_str, from_none], self.post_title)
        result["Post_Title_link"] = from_union([from_str, from_none], self.post_title_link)
        result["Post_User"] = from_union([from_str, from_none], self.post_user)
        result["Post_User_link"] = from_union([from_str, from_none], self.post_user_link)
        result["index"] = from_union([from_int, from_none], self.index)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["uid"] = from_union([from_str, from_none], self.uid)
        result["url"] = from_union([from_str, from_none], self.url)
        result["url_uid"] = from_union([from_int, from_none], self.url_uid)
        return result


@dataclass
class LatestThreads:
    name: Optional[str] = None
    url: Optional[str] = None
    date_last_ran_timestamp: Optional[int] = None
    data: Optional[List[Datum]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LatestThreads':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        date_last_ran_timestamp = from_union([from_int, from_none], obj.get("date_last_ran_timestamp"))
        data = from_union([lambda x: from_list(Datum.from_dict, x), from_none], obj.get("data"))
        return LatestThreads(name, url, date_last_ran_timestamp, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["url"] = from_union([from_str, from_none], self.url)
        result["date_last_ran_timestamp"] = from_union([from_int, from_none], self.date_last_ran_timestamp)
        result["data"] = from_union([lambda x: from_list(lambda x: to_class(Datum, x), x), from_none], self.data)
        return result


def latest_threads_from_dict(s: Any) -> LatestThreads:
    return LatestThreads.from_dict(s)