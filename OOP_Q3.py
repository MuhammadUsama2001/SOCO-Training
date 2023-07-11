library_cat = {}
availability = {}
class Library:

    def add_item(self, identifier, title):
        library_cat.setdefault(identifier, []).extend([title])

    def display_catalog(self):
        print(f"Available Catalogue: {library_cat}")

    def check_availability(self):
        for identifier in library_cat:
            availability[identifier] = []
            availability[identifier].append(True)
            # self.availability
        print(availability)


class LibraryItems(Library):

    def __init__(self, identifier, title, content):
        super().__init__()
        self.identifier = identifier
        self.title = title
        self.content = content

    def check_availability(self):
        if self.identifier in library_cat:
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
    c = CD('Fww', 'ML', 'Text')
    c.add_item('Fww', 'ML')
    c.display_details()
    b = Book('BB', 'AI', 'Text')
    b.add_item('BB', 'AI')
    b.display_details()
    a.check_availability()