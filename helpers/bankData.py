from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


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


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414:
    type: Optional[str]
    amount: Optional[int]
    date: Optional[str]
    time: Optional[datetime]
    payee: Optional[str]

    def __init__(self, type: Optional[str], amount: Optional[int], date: Optional[str], time: Optional[datetime], payee: Optional[str]) -> None:
        self.type = type
        self.amount = amount
        self.date = date
        self.time = time
        self.payee = payee

    @staticmethod
    def from_dict(obj: Any) -> 'The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        date = from_union([from_str, from_none], obj.get("date"))
        time = from_union([from_datetime, from_none], obj.get("time"))
        payee = from_union([from_str, from_none], obj.get("payee"))
        return The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414(type, amount, date, time, payee)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["amount"] = from_union([from_int, from_none], self.amount)
        result["date"] = from_union([from_str, from_none], self.date)
        result["time"] = from_union([lambda x: x.isoformat(), from_none], self.time)
        result["payee"] = from_union([from_str, from_none], self.payee)
        return result


class Transaction:
    the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414: Optional[The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414]

    def __init__(self, the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414: Optional[The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414]) -> None:
        self.the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414 = the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414

    @staticmethod
    def from_dict(obj: Any) -> 'Transaction':
        assert isinstance(obj, dict)
        the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414 = from_union([The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414.from_dict, from_none], obj.get("441b9b7edbff748b19018aff7287165ca713fed51b6e5a947feaa84f423ec414"))
        return Transaction(the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414)

    def to_dict(self) -> dict:
        result: dict = {}
        result["441b9b7edbff748b19018aff7287165ca713fed51b6e5a947feaa84f423ec414"] = from_union([lambda x: to_class(The441B9B7Edbff748B19018Aff7287165Ca713Fed51B6E5A947Feaa84F423Ec414, x), from_none], self.the_441_b9_b7_edbff748_b19018_aff7287165_ca713_fed51_b6_e5_a947_feaa84_f423_ec414)
        return result


class The686347450210058269:
    transactions: Optional[List[Transaction]]
    wallet: Optional[int]
    joindate: Optional[str]
    hash: Optional[str]

    def __init__(self, transactions: Optional[List[Transaction]], wallet: Optional[int], joindate: Optional[str], hash: Optional[str]) -> None:
        self.transactions = transactions
        self.wallet = wallet
        self.joindate = joindate
        self.hash = hash

    @staticmethod
    def from_dict(obj: Any) -> 'The686347450210058269':
        assert isinstance(obj, dict)
        transactions = from_union([lambda x: from_list(Transaction.from_dict, x), from_none], obj.get("transactions"))
        wallet = from_union([from_int, from_none], obj.get("wallet"))
        joindate = from_union([from_str, from_none], obj.get("joindate"))
        hash = from_union([from_str, from_none], obj.get("hash"))
        return The686347450210058269(transactions, wallet, joindate, hash)

    def to_dict(self) -> dict:
        result: dict = {}
        result["transactions"] = from_union([lambda x: from_list(lambda x: to_class(Transaction, x), x), from_none], self.transactions)
        result["wallet"] = from_union([from_int, from_none], self.wallet)
        result["joindate"] = from_union([from_str, from_none], self.joindate)
        result["hash"] = from_union([from_str, from_none], self.hash)
        return result


class Accounts:
    the_686347450210058269: Optional[The686347450210058269]

    def __init__(self, the_686347450210058269: Optional[The686347450210058269]) -> None:
        self.the_686347450210058269 = the_686347450210058269

    @staticmethod
    def from_dict(obj: Any) -> 'Accounts':
        assert isinstance(obj, dict)
        the_686347450210058269 = from_union([The686347450210058269.from_dict, from_none], obj.get("686347450210058269"))
        return Accounts(the_686347450210058269)

    def to_dict(self) -> dict:
        result: dict = {}
        result["686347450210058269"] = from_union([lambda x: to_class(The686347450210058269, x), from_none], self.the_686347450210058269)
        return result


class Bankteller:
    accounts: Optional[Accounts]

    def __init__(self, accounts: Optional[Accounts]) -> None:
        self.accounts = accounts

    @staticmethod
    def from_dict(obj: Any) -> 'Bankteller':
        assert isinstance(obj, dict)
        accounts = from_union([Accounts.from_dict, from_none], obj.get("Accounts"))
        return Bankteller(accounts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Accounts"] = from_union([lambda x: to_class(Accounts, x), from_none], self.accounts)
        return result


def bankteller_from_dict(s: Any) -> Bankteller:
    return Bankteller.from_dict(s)

