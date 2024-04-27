import random

def get_random_boy_names():
    # List of boy names
    boys = ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
            "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo"]
    
    # Initialize an empty list to store chosen names
    boy_names = []
    
    # Generate a list of 20 random boy baby names
    for _ in range(20):
        # Select a random name from the list
        chosen_name = random.choice(boys)
        boy_names.append(chosen_name)
    
    return boy_names

def main():
    # Get a list of random boy names
    boy_names = get_random_boy_names()
    
    # Print each chosen name
    for name in boy_names:
        print(name)

# Call the main function if this file is executed as a script
if __name__ == "__main__":
    main()


        