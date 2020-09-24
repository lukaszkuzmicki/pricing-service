import uuid
from dataclasses import dataclass, field
from typing import Dict
from models.item import Item
from models.model import Model

#eq=false -- nie bedzie mozliwosci porywnywania alertow

@dataclass(eq=False)
class Alert(Model):
    # collection = "alerts" -- to samo niżej tylko jako dataclass
    collection: str = field(init=False, default="alerts") # init false =-== czyli nie bedzie mozna zmieniac tego jak tworzymy obiekt
    item_id : str
    price_limit: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # zmieniamy init metod na @dataclass, wyszlo to w pythonie 3.7 i pozawala na porwnywanie obietów itp.


    def __post__init__(self):
        self.item = Item.get_by_id(self.item_id)


    # this should return all data which should be saved in db
    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reach a price under {self.price_limit}. Latest price: {self.item.price}.")
