
class Book:
    # Class variable to track all instances
    _instances = []

    def __init__(self, title):
        self._title = title
        # Register the instance
        Book._instances.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("Invalid title.")
        self._title = value

    @classmethod
    def get_all_books(cls):
        return cls._instances

    def contracts(self):
        # Return a list of related contracts using Contract as an intermediary
        related_contracts = []
        for contract in Contract.get_all_contracts():
            if contract.book == self:
                related_contracts.append(contract)
        return related_contracts
    def authors(self):
        # Return a list of related authors using Contract as an intermediary
        related_authors = []
        for contract in Contract.get_all_contracts():
            if contract.book == self:
                related_authors.append(contract.author)
        return related_authors

class Author:
    # Class variable to track all instances
    _instances = []

    def __init__(self, name):
        self._name = name
        # Register the instance
        Author._instances.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("Invalid name.")
        self._name = value

    @classmethod
    def get_all_authors(cls):
        return cls._instances

    def books(self):
        # Return a list of related books using Contract as an intermediary
        related_books = []
        for contract in Contract.get_all_contracts():
            if contract.author == self:
                related_books.append(contract.book)
        return related_books

    def sign_contract(self, book, date, royalties):
        # Validate input parameters
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("date must be a non-empty string.")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number.")
        
        # Create a new contract
        new_contract = Contract(author=self, book=book, date=date, royalties=royalties)
        return new_contract

    def contracts(self):
        # Return a list of related contracts using Contract as an intermediary
        related_contracts = []
        for contract in Contract.get_all_contracts():
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts

    def total_royalties(self):
        # Calculate the total royalties earned by the author
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Contract:
    # Class variable to track all instances
    _instances = []

    def __init__(self, author, book, date, royalties):
        self._author = None
        self._book = None
        self.date = date
        self.royalties = royalties

        self.author = author
        self.book = book
        # Register the instance
        Contract._instances.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value:
            raise Exception("Date must be a non-empty string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)) :
            raise Exception("Royalties must be a number .")
        self._royalties = value
    def contracts_by_date(self, target_date):
        # Sort contracts by date and return those matching target_date
        return sorted(
            [contract for contract in self.get_all_contracts() if contract.date == target_date],
            key=lambda c: c.date)    
 

    @classmethod
    def get_all_contracts(cls):
        return cls._instances
    
   
author1 = Author("John Doe")
author2 = Author("Jane Smith")
book1 = Book("Python Programming")
book2 = Book("Data Science Essentials")
book3 = Book("Advanced Python")
contract1 = Contract(author1, book1, "2024-01-01", 10)
print(contract1)