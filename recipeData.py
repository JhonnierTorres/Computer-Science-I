# Initial Data

recipeNames = ["Spaghetti Bolognese", "Chicken Tikka Masala", "Beef Tacos"]
spaghettiIngredients = ["spaghetti", "minced beef", "tomato sauce", "onion", "garlic"]
chickenTikkaIngredients = ["chicken breast", "yogurt", "tikka masala spice", "rice"]
beefTacosIngredients = ["ground beef", "taco shells", "lettuce", "tomato", "cheese"]

# Task 1:
# Write a function `create_recipe()` that takes recipe name and a list of ingredients as parameters,
# and returns a dictionary representing the recipe.
def create_recipe(name, ingredients):
    recipe = {
        "name": name,
        "ingredients": ingredients
    }
    return recipe

# Task 2:
# Use `create_recipe()` to create a recipe object for each of your recipes, and store them in a list called `recipes`.


recipeIngredients = [spaghettiIngredients, chickenTikkaIngredients, beefTacosIngredients]
recipes = []
for i in range(len(recipeNames)):
    recipes.append(create_recipe(recipeNames[i], recipeIngredients[i]))

# Task 3:
# Write a function `get_recipe()` that takes the recipe name as a parameter and
# returns the matching recipe object from the `recipes` list.
def get_recipe(recipe_name):
    for recipe in recipes:
        if recipe["name"] == recipe_name:
            return recipe
    return None  # Return None if the recipe is not found


# Task 4:
# Use `get_recipe()` to retrieve the "Chicken Tikka Masala" recipe and print its details.
request = "Chicken Tikka Masala"
result = get_recipe(request)

# Check if the recipe exists
if result is not None:
    print("Recipe Name:", result["name"])
    print("Ingredients:", ', '.join(result["ingredients"]))
else:
    print(f"Recipe for '{request}' not found.")

# Task 5:
# Write a function `add_recipe()` that takes a recipe object as a parameter and adds it to the `recipes` list.
def add_recipe(recipe):
    recipes.append(recipe)
# Task 6:
# Use `add_recipe()` to add a new recipe to your `recipes` list.
new_recipe = create_recipe("Chicken-Parm", ["Pasta", "Chicken", "Alfredo Sauce"])
add_recipe(new_recipe)
# Task 7:
# Write a function `remove_recipe()` that takes a recipe name as a parameter and removes the matching recipe object from the `recipes` list.
def remove_recipe(recipe_name):
    for recipe in recipes:
        if recipe["name"] == recipe_name:
            recipes.remove(recipe)
            print(f"{recipe_name} deleted successfully")
            return
    print(f"{recipe_name} not found in the list.")


# Task 8:
# Use `remove_recipe()` to remove the "Beef Tacos" recipe from your `recipes` list.
recipe_to_remove = "Beef Tacos"
remove_recipe(recipe_to_remove)
print("Updated Recipes List:")
for recipe in recipes:
    print("Recipe Name:", recipe["name"])
    print("Ingredients:", ', '.join(recipe["ingredients"]))
# Task 9:
# Write a function update_recipe() that takes a recipe name and a new ingredients list as parameters, and updates the matching recipe object in the recipes list.
def update_recipe(recipe_name, new_ingredients):
    for recipe in recipes:
        if recipe["name"] == recipe_name:
            recipe["ingredients"] = new_ingredients
            print(f"{recipe_name} updated successfully")
            return
    print(f"{recipe_name} not found in the list.")


# Task 10:
# Use `update_recipe()` to update the ingredients for your "Spaghetti Bolognese" recipe.
recipe_name_to_update = "Spaghetti Bolognese"
new_ingredients = ["Pasta", "Tomato Sauce", "Basil", "Parmesan Cheese"]
update_recipe(recipe_name_to_update, new_ingredients)
