# 1 #
# class AudioFile:
    # def __init__(self, filename):
#         if not filename.endswith(self.ext):
#             raise Exception("Invalid file format")
#         self.filename = filename
        
# class MP3File(AudioFile):
#     ext = "mp3"
#     def play(self):
#         print(f"playing {self.filename} as mp3")
        
# class WavFile(AudioFile):
#     ext = "wav"
#     def play(self):
#         print(f"playing {self.filename} as wav")
        
# class OggFile(AudioFile):
#     ext = "ogg"
#     def play(self):
#         print(f"playing {self.filename} as ogg")
        
# ogg = OggFile("myfile.ogg")
# ogg.play()
# not_ogg = OggFile("myfile.mp3")

# 2 #
class Property:
    
    def __init__(self, square_feet='', beds='', baths='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.square_feet, self.bedrooms_num, self.baths_num = square_feet, beds, baths
    
    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print(f"square footage: {self.square_feet}")
        print(f"bedrooms {self.bedrooms_num}")
        print(f"bathrooms {self.baths_num}")
        print()
    
    def prompt_init():
        return dict(
                square_feet=input("Enter the square feet: "),
                beds=input("Enter number of bedrooms: "),
                baths=input("Enter number of baths: ")
                )
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    input_string += f" {(', '.join(valid_options))} "
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    
    valid_laundries = {"coin", "ensuite", "none"}
    valid_balconies = {"yes", "no", "solarium"}
    
    def __init__(self, balcony='', laundry='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.balcony, self.laundry = balcony, laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print(f"laundry {self.laundry}")
        print(f"has balcony: {self.balcony}")

    @staticmethod
    def prompt_init():
        
        parent_init = Property.prompt_init()
        
        laundry = get_valid_input("What laundry facilities does the property have? ", Apartment.valid_laundries)
        
        balcony = get_valid_input("Does the property have a balcony? ", Apartment.valid_balconies)
        
        parent_init.update({"laundry": laundry, "balcony": balcony})
        
        return parent_init


class House(Property):
    
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    
    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage, self.fenced, self.num_stories = garage, fenced, num_stories
        
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print(f"# of stories: {self.num_stories}")
        print(f"garage: {self.garage}")
        print(f"fenced yard: {self.fenced}")
    
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({ "fenced": fenced, "garage": garage, "num_stories": num_stories})
        return parent_init


class Purchase:
    
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price, self.taxes = price, taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print(f"selling price: {self.price}")
        print(f"estimated taxes: {self.taxes}")
    
    @staticmethod
    def prompt_init():
        return dict(
        price=input("What is the selling price? "),
        taxes=input("What are the estimated taxes? "))

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished, self.rent, self.utilities = furnished, rent, utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print(f"rent: {self.rent}")
        print(f"estimated utilities: {self.utilities}")
        print(f"furnished: {self.furnished}")
    
    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished = get_valid_input("Is the property furnished? ",("yes", "no"))
            )

class HouseRental(Rental, House):
    
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

# init = HouseRental.prompt_init()
# house = HouseRental(**init)
# print(HouseRental().display())

class ApartmentRental(Rental, Apartment):

    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):

    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class HousePurchase(Purchase, House):

    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class Agent:
    
    def __init__(self):
        self.property_list = []
    
    def display_properties(self):
        for property in self.property_list:
            property.display()
    
    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase, ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase} 

    def add_property(self):
        
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ", ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

agent = Agent().add_property()
# print(agent.display_properties())
print(agent)