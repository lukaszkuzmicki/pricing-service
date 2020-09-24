import re
import uuid
from typing import Dict
from dataclasses import dataclass, field
import requests
from bs4 import BeautifulSoup

from common.database import Database
from models.model import Model

@dataclass(eq=False)
class Item(Model):

    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        # number + optional comma + any numbers . two numbers
        pattern = re.compile(r"(\d+,?\d*\.\d\d)")  # 14.34
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(',', '')
        self.price = float(without_commas)
        return self.price

    def json(self) -> dict:
        return {
            "_id": self._id,
            "url": self.url,
            "price":self.price,
            "tag_name": self.tag_name,
            "query": self.query
        }

    # @classmethod
    # def get_by_id(cls, _id: str) -> "Item":
    #     return cls(**Database.find_one("items", {"_id": _id}))









