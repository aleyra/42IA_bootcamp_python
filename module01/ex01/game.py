class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        #checks
        assert isinstance(first_name, str), "the first name must be a string"
        assert first_name != "", "the character must have a name"
        assert isinstance(is_alive, bool)

        #init
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        if self.is_alive == True:
            status = "yes"
        else:
            status = "no"
        to_print = f"{self.first_name} (is alive : {status})"
        return to_print

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False

if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__dict__)
    arya.print_house_words()
    print(arya)
    arya.die()
    print(arya)