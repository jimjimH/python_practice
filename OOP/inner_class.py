"""
https://www.datacamp.com/community/tutorials/inner-classes-python#IONC
Why Inner Classes?
Grouping of two or more classes. Suppose you have two classes Car and Engine. Every Car needs an Engine. But, Engine won't be used without a Car. So, you make the Engine an inner class to the Car. It helps save code.

Hiding code is another use of Nested classes. You can hide the Nested classes from the outside world.

It's easy to understand the classes. Classes are closely related here. You don't have to search for the classes in the code. They are all together.

Inner or Nested classes are not the most commonly used feature in Python. But, it can be a good feature to implement code. The code is straightforward to organize when you use the inner or nested classes.
"""
class Outer:
    """Outer Class"""
    def __init__(self):
        ## Instantiating the 'Inner' class
        self.inner = self.Inner()
        ## Instantiating the '_Inner' class
        self._inner = self._Inner()

    def show_classes(self):
        print("This is Outer class")
        print(inner)
        print(_inner)

    class Inner:
        """First Inner Class"""

        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

    class _Inner:
        """Second Inner Class"""

        def inner_display(self, msg):
            print("This is _Inner class")
            print(msg)

outer = Outer()

inner = outer.Inner()

_inner = outer._Inner()

outer.show_classes()

Outer().Inner().inner_display("Just Print It!")
inner.inner_display("Just Print It!")