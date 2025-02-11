# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['foo', 'FooBar', 'bar']

# %% ../nbs/00_core.ipynb 4
def foo(): pass

# %% ../nbs/00_core.ipynb 6
class FooBar:

    def __init__(
        self, 
        name: str  # name of this instance
        ):
        """Initialize FooBar instance with a name"""
        self.name = name

    def reveal(self):
        """Say who you are!"""
        print(f"My name is {self.name}")

    def multiply(
        self,
        times=1 # Number of copies to add
    ):
        """Add additional copies"""
        self.name += self.name * times

# %% ../nbs/00_core.ipynb 9
def bar(): pass
