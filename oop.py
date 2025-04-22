# Assignment 1: Design Your Own Class!
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    price = 20.00

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __len__(self):
        return self.pages
    
    def amount(self, qty):
        return self.price * qty
    
class EBook(Book):
    def __init__(self, title, author, pages, size):
        super().__init__(title, author, pages)
        self.size = size

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, {self.size}MB"
    
    def amount(self, qty):
        return self.price * qty * 0.8  # 20% discount for eBooks
    
class AudioBook(Book):
    def __init__(self, title, author, pages, duration):
        super().__init__(title, author, pages)
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, {self.duration} hours"
    
    def amount(self, qty):
        return self.price * qty * 1.2  # 20% extra for audiobooks

# Example usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    ebook1 = EBook("1984", "George Orwell", 328, 1.5)
    audiobook1 = AudioBook("To Kill a Mockingbird", "Harper Lee", 281, 12)

    print(book1)
    print(ebook1)
    print(audiobook1)

    print(f"Price for 2 copies of {book1.title}: ${book1.amount(2)}")
    print(f"Price for 3 copies of {ebook1.title}: ${ebook1.amount(3)}")
    print(f"Price for 1 copy of {audiobook1.title}: ${audiobook1.amount(1)}")
    print(f"Length of {book1.title}: {len(book1)} pages")

# Activity 2: Polymorphism Challenge! 
# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving", while Plane.move() prints "Flying").
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky"
    
# Example usage
if __name__ == "__main__":
    car = Car()
    plane = Plane()

    print(car.move())  # Output: Driving on the road
    print(plane.move())  # Output: Flying in the sky