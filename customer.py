class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        self._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be 1–15 characters")
        self._name = value

    