# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = userdata_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Userdata:
    username: str
    active: str
    joindate: str
    pfp: str
    postlink: str
    posts: int
    proflink: str
    rep: int
    replink: str
    status: str
    threadlink: str
    threads: int
    timeonline: str

    def __init__(self, username: str, active: str, joindate: str, pfp: str, postlink: str, posts: int, proflink: str, rep: int, replink: str, status: str, threadlink: str, threads: int, timeonline: str) -> None:
        self.username = username
        self.active = active
        self.joindate = joindate
        self.pfp = pfp
        self.postlink = postlink
        self.posts = posts
        self.proflink = proflink
        self.rep = rep
        self.replink = replink
        self.status = status
        self.threadlink = threadlink
        self.threads = threads
        self.timeonline = timeonline

    @staticmethod
    def from_dict(obj: Any) -> 'Userdata':
        assert isinstance(obj, dict)
        username = from_str(obj.get("Username"))
        active = from_str(obj.get("active"))
        joindate = from_str(obj.get("joindate"))
        pfp = from_str(obj.get("pfp"))
        postlink = from_str(obj.get("postlink"))
        posts = int(from_str(obj.get("posts")))
        proflink = from_str(obj.get("proflink"))
        rep = int(from_str(obj.get("rep")))
        replink = from_str(obj.get("replink"))
        status = from_str(obj.get("status"))
        threadlink = from_str(obj.get("threadlink"))
        threads = int(from_str(obj.get("threads")))
        timeonline = from_str(obj.get("timeonline"))
        return Userdata(username, active, joindate, pfp, postlink, posts, proflink, rep, replink, status, threadlink, threads, timeonline)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Username"] = from_str(self.username)
        result["active"] = from_str(self.active)
        result["joindate"] = from_str(self.joindate)
        result["pfp"] = from_str(self.pfp)
        result["postlink"] = from_str(self.postlink)
        result["posts"] = from_str(str(self.posts))
        result["proflink"] = from_str(self.proflink)
        result["rep"] = from_str(str(self.rep))
        result["replink"] = from_str(self.replink)
        result["status"] = from_str(self.status)
        result["threadlink"] = from_str(self.threadlink)
        result["threads"] = from_str(str(self.threads))
        result["timeonline"] = from_str(self.timeonline)
        return result


def userdata_from_dict(s: Any) -> Userdata:
    return Userdata.from_dict(s)