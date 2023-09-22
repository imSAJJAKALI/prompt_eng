from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

menu = {}  # A dictionary to store menu items

# Helper function to add a dish to the menu
def add_dish(dish_id, name, price, available):
    if dish_id in menu:
        return "Dish already exists", 400
    menu[dish_id] = {'name': name, 'price': price, 'available': available}
    return "Dish added successfully", 200

# Helper function to get a dish by dish_id
def get_dish(dish_id):
    return menu.get(dish_id)

# TODO: Implement more CRUD operations and order management routes

if __name__ == "__main__":
    app.run(debug=True)
