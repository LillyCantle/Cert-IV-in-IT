import random


class PetSpecies:
    def __init__(self, name):
        self.name = name


class Task:
    PRIORITY_OPTIONS = {"Normal": 0.1, "High": 0.2}

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def perform(self):
        print(f"You completed the task: {self.name}")
        return self.priority


class VirtualPet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = 0
        self.tasks = []

    def display_status(self):
        print(f"{self.species.name} {self.name}'s Status:")
        print(f"Age: {self.age} days")

    def add_task(self, task):
        self.tasks.append(task)

    def perform_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            growth_rate = self.tasks[task_index].perform()
            self.age += growth_rate


# Define pet species
all_species = [
    PetSpecies("Dragon"),
    PetSpecies("Gryphon"),
    PetSpecies("Lion"),
    PetSpecies("Unicorn"),
    PetSpecies("Serpent")
]

# Choose a random species for the virtual pet
chosen_species = random.choice(all_species)

# Main game loop
pet_name = input(f"Name your {chosen_species.name}: ")
pet = VirtualPet(pet_name, chosen_species)

while True:
    pet.display_status()

    # Display available tasks with priority options
    for i, task in enumerate(pet.tasks):
        print(f"{i + 1}. {task.name} (Priority: {task.priority})")

    print(f"{len(pet.tasks) + 1}. Add Custom Task")
    choice = input(f"Choose an action (1/{len(pet.tasks) + 1}): ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(pet.tasks):
            pet.perform_task(choice - 1)
        elif choice == len(pet.tasks) + 1:
            custom_task_name = input("Enter the name of the custom task: ")

            # Display priority options
            print("Priority Options:")
            for option, growth_rate in Task.PRIORITY_OPTIONS.items():
                print(f"{option}: {growth_rate} Growth")

            custom_task_priority_option = input("Choose a priority option: ")
            custom_task_priority = Task.PRIORITY_OPTIONS.get(custom_task_priority_option, 0.1)

            custom_task = Task(custom_task_name, custom_task_priority)
            pet.add_task(custom_task)
            pet.perform_task(len(pet.tasks) - 1)

    if pet.age >= 1:
        print(f"Your {pet.species.name} {pet.name} has grown to maturity.")
        break
