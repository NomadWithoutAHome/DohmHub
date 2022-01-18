# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = profile_information_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ProfileInformation:
    uid: str
    url_uid: int
    refs_link: str
    username: None
    profile_picture: str
    rep: int
    status_link: str
    url: str
    rep_link: str
    status: str
    timestamp: int
    threads_link: str
    threads: int
    thanks: None
    posts: int
    refs: int
    posts_link: str
    index: int

    def __init__(self, uid: str, url_uid: int, refs_link: str, username: None, profile_picture: str, rep: int, status_link: str, url: str, rep_link: str, status: str, timestamp: int, threads_link: str, threads: int, thanks: None, posts: int, refs: int, posts_link: str, index: int) -> None:
        self.uid = uid
        self.url_uid = url_uid
        self.refs_link = refs_link
        self.username = username
        self.profile_picture = profile_picture
        self.rep = rep
        self.status_link = status_link
        self.url = url
        self.rep_link = rep_link
        self.status = status
        self.timestamp = timestamp
        self.threads_link = threads_link
        self.threads = threads
        self.thanks = thanks
        self.posts = posts
        self.refs = refs
        self.posts_link = posts_link
        self.index = index

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileInformation':
        assert isinstance(obj, dict)
        uid = from_str(obj.get("uid"))
        url_uid = from_int(obj.get("url_uid"))
        refs_link = from_str(obj.get("Refs_link"))
        username = from_none(obj.get("username"))
        profile_picture = from_str(obj.get("ProfilePicture"))
        rep = int(from_str(obj.get("Rep")))
        status_link = from_str(obj.get("Status_link"))
        url = from_str(obj.get("url"))
        rep_link = from_str(obj.get("Rep_link"))
        status = from_str(obj.get("Status"))
        timestamp = from_int(obj.get("timestamp"))
        threads_link = from_str(obj.get("Threads_link"))
        threads = int(from_str(obj.get("Threads")))
        thanks = from_none(obj.get("Thanks"))
        posts = int(from_str(obj.get("Posts")))
        refs = int(from_str(obj.get("Refs")))
        posts_link = from_str(obj.get("Posts_link"))
        index = from_int(obj.get("index"))
        return ProfileInformation(uid, url_uid, refs_link, username, profile_picture, rep, status_link, url, rep_link, status, timestamp, threads_link, threads, thanks, posts, refs, posts_link, index)

    def to_dict(self) -> dict:
        result: dict = {}
        result["uid"] = from_str(self.uid)
        result["url_uid"] = from_int(self.url_uid)
        result["Refs_link"] = from_str(self.refs_link)
        result["username"] = from_none(self.username)
        result["ProfilePicture"] = from_str(self.profile_picture)
        result["Rep"] = from_str(str(self.rep))
        result["Status_link"] = from_str(self.status_link)
        result["url"] = from_str(self.url)
        result["Rep_link"] = from_str(self.rep_link)
        result["Status"] = from_str(self.status)
        result["timestamp"] = from_int(self.timestamp)
        result["Threads_link"] = from_str(self.threads_link)
        result["Threads"] = from_str(str(self.threads))
        result["Thanks"] = from_none(self.thanks)
        result["Posts"] = from_str(str(self.posts))
        result["Refs"] = from_str(str(self.refs))
        result["Posts_link"] = from_str(self.posts_link)
        result["index"] = from_int(self.index)
        return result


def profile_information_from_dict(s: Any) -> ProfileInformation:
    return ProfileInformation.from_dict(s)


def profile_information_to_dict(x: ProfileInformation) -> Any:
    return to_class(ProfileInformation, x)
