class Library:
    library_cat = {}
    availability = {}

    def add_item(self, identifier, title):
        Library.library_cat.setdefault(identifier, []).extend([title])

    def display_catalog(self):
        print(f"Available Catalogue: {Library.library_cat}")

    def check_availability(self):
        for identifier in Library.library_cat:
            Library.availability[identifier] = []
            Library.availability[identifier].append(True)
        print(Library.availability)


class LibraryItems(Library):
    def __init__(self, identifier, title, content):
        self.identifier = identifier
        self.title = title
        self.content = content

    def check_availability(self):
        if self.identifier in Library.library_cat:
            return True
        else:
            return False

    def display_details(self):
        print(f"Identifier: {self.identifier}")
        print(f"Title: {self.title}")
        print(f"Availability: {self.check_availability()}")


class Book(LibraryItems):

    def __init__(self, identifier, title, content):
        super().__init__(identifier, title, content)

    def display_details(self):
        super().display_details()
        print(f"Content: {self.content}")


class Magazine(LibraryItems):

    def __init__(self, identifier, title, content):
        super().__init__(identifier, title, content)

    def display_details(self):
        super().display_details()
        print(f"Content: {self.content}")


class CD(LibraryItems):

    def __init__(self, identifier, title, content):
        super().__init__(identifier, title, content)

    def display_details(self):
        super().display_details()
        print(f"Content: {self.content}")

if __name__ == "__main__":
    a = Library()
    a.add_item('FDD', 'Python')
    a.add_item('G454', 'ML')
    a.display_catalog()
    a.check_availability()
    b = LibraryItems('DFW', 'WEEE', 'Text')
    b.display_details()
    b.add_item('DFW', 'WEEE')
    a.display_catalog()
    b.display_details()
    c = CD('QWE', 'MLOPS', 'Topics')
    c.add_item('QWE', 'MLOPS')
    c.check_availability()
    c.display_catalog()
