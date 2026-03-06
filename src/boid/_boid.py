class Boid:
    def __init__(self, *args):
        print("Hello from Boid")
        self.arg = args[0]


def run_app():
    my_obj = Boid("Hi!")
    print(f"{my_obj.arg = }")
