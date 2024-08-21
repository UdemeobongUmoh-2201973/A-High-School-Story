import pygame
pygame.init()

class Character:
    def __init__(self, name, role, gender, image_id, popularity=50, energy=100, intelligence=50):
        self.name = name
        self.role = role  # e.g., "Student", "Teacher", "Principal"
        self.gender = gender
        self.image_id = image_id
        self.popularity = popularity
        self.energy = energy
        self.intelligence = intelligence
        self.relationships = {}  # Dictionary to store relationships with other characters
    
    def interact(self, other_character, interaction_type):
        """Interacts with another character, affecting their relationship."""
        if interaction_type == "friendly":
            self.relationships[other_character.name] = self.relationships.get(other_character.name, 50) + 10
        elif interaction_type == "hostile":
            self.relationships[other_character.name] = self.relationships.get(other_character.name, 50) - 10
        else:
            self.relationships[other_character.name] = self.relationships.get(other_character.name, 50)
    
    def study(self, hours):
        """Improves intelligence based on the number of study hours."""
        self.intelligence += hours * 2
        self.energy -= hours * 5
    
    def rest(self, hours):
        """Recovers energy based on rest hours."""
        self.energy += hours * 10
    
    def join_club(self, club):
        """Increases popularity by joining a club."""
        self.popularity += club.popularity_boost

    def __str__(self):
        return f"{self.name} ({self.role}) - Popularity: {self.popularity}, Energy: {self.energy}, Intelligence: {self.intelligence}"



class Location:
    def __init__(self, name, max_capacity, activities):
        self.name = name
        self.max_capacity = max_capacity
        self.activities = activities  # List of activities that can happen here
        self.current_occupants = []

    def enter(self, character):
        """Adds a character to the location if there's space."""
        if len(self.current_occupants) < self.max_capacity:
            self.current_occupants.append(character)
            return f"{character.name} has entered {self.name}."
        else:
            return f"{self.name} is full! {character.name} cannot enter."

    def exit(self, character):
        """Removes a character from the location."""
        if character in self.current_occupants:
            self.current_occupants.remove(character)
            return f"{character.name} has left {self.name}."
        else:
            return f"{character.name} is not in {self.name}."
    
    def start_activity(self, activity):
        """Starts an activity if it's available in this location."""
        if activity in self.activities:
            return f"{activity} is happening now in {self.name}."
        else:
            return f"{activity} cannot be done in {self.name}."

    def __str__(self):
        return f"Location: {self.name} (Capacity: {self.max_capacity})"



class Club:
    def __init__(self, name, popularity_boost):
        self.name = name
        self.popularity_boost = popularity_boost

    def __str__(self):
        return f"Club: {self.name} (Popularity Boost: {self.popularity_boost})"



class Event:
    def __init__(self, name, location, participants):
        self.name = name
        self.location = location
        self.participants = participants

    def start_event(self):
        """Start the event and interact all participants."""
        results = []
        for participant in self.participants:
            results.append(f"{participant.name} is participating in {self.name} at {self.location.name}.")
        return results
    
    def __str__(self):
        return f"Event: {self.name} at {self.location.name}"


"""
# Create some characters


alice = Character(name="Alice", role="Student", popularity=60, intelligence=70)
bob = Character(name="Bob", role="Student", popularity=50, intelligence=80)

# Create a location
cafeteria = Location(name="Cafeteria", max_capacity=50, activities=["Lunch", "Socializing"])

# Create a club
chess_club = Club(name="Chess Club", popularity_boost=10)

# Characters interact
alice.interact(bob, "friendly")
print(alice.relationships)

# Alice joins the Chess Club
alice.join_club(chess_club)
print(alice)

# Characters enter a location
print(cafeteria.enter(alice))
print(cafeteria.enter(bob))

# Start an event
event = Event(name="Chess Tournament", location=cafeteria, participants=[alice, bob])
print(event.start_event())
"""