from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, new_val):
        self.value2 = new_val  # This line will raise a FrozenInstanceError


obj = ImmutableClass("Another String", 20)
print(obj.value1, obj.value2)

# obj.value1 = "Another string"  # This line would also raise a FrozenInstanceError
# print(obj.value1)
obj.some_func(20)  # This will raise an error
