class Product():
    
    code: str
    name: str
    price: int
    currency: str
    
    def __init__(self, code, name, price) -> None:
        self.code = code,
        self.name = name,
        self.price = price