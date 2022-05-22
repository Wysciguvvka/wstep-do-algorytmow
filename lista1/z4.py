class LocalStore:
    def __init__(self) -> None:
        """Przyjąć, że pierwsza macierz przedstawia paragon w sklepie i zawiera w
            kolumnach: numer klienta, numer towaru, liczbę sztuk (lub wagę w kilogramach).
            Druga macierz Zawiera opisy towarów, tj.: numer towaru, cenę jednostkową (lub za
            kg), informację czy towar jest sprzedawany na sztuki czy na wagę."""
        # True - sztuki,False - waga
        self.receipts = [[0, 0, 3], [0, 1, 1], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
        self.products = [[0, 20, True], [1, 13, False], [2, 10, False], [3, 15, True], [4, 12, False]]
        self.validate()

    def validate(self) -> None:
        products = [product[0] for product in self.products]
        if len(set(products)) != len(products):
            raise IndexError('id produktów się powtarzają')
        for client in self.receipts:
            product_id = client[1]
            occurrences = 0
            for product in self.products:
                if product[0] == product_id:
                    occurrences = 1
                    if product[2] is True and not isinstance(client[2], int):
                        raise TypeError(f'Niepoprawna ilość produktu {product_id} u klienta {client[0]}')
                    break
            if occurrences != 1:
                raise IndexError(f'produkt {product_id} nie istnieje')

    def total_price(self, client_id) -> float:
        client_receipts = [client for client in self.receipts if client[0] == client_id]
        _sum = 0.0
        for receipt in client_receipts:
            for product in self.products:
                if product[0] == receipt[1]:
                    _sum += product[1] * receipt[2]
        return _sum


if __name__ == '__main__':
    store = LocalStore()
    assert store.total_price(0) == 73.0
