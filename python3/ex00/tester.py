from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print("---")
print(Ned.__doc__)
print("---")
print(Ned.__init__.__doc__)
print("---")
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

try:
    hodor = Character("hodor")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
