from flask import Flask, jsonify, request,render_template,redirect
import json

app = Flask(__name__)

dishes = []
orders = []
with open('dishes.json', 'r') as file:
    dishes = json.load(file)
with open('orders.json', 'r') as file:
    orders = json.load(file)

# Helper function to find a dish by ID
def find_dish(dish_id):
    return next((dish for dish in dishes if dish['id'] == dish_id), None)

# Helper function to find an order by ID
def find_order(order_id):
    return next((order for order in orders if order['id'] == order_id), None)

def save_data():
    with open('dishes.json', 'w') as file:
        json.dump(dishes, file, indent=4)
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

@app.route('/', methods=['GET'])
def homePage():
    return render_template('home.html')


@app.route('/dishes', methods=['POST',"GET"])
def add_dish():
    if request.method == 'POST':
        data = request.form
        dish = {
            'id': len(dishes) + 1,
            'name': data['name'],
            'price': float(data['price']),
            'availability': True if 'availability' in data else False
        }
        dishes.append(dish)
        save_data()
        return redirect('/view_dishes')
    return render_template('add_dish.html')

@app.route('/view_dishes', methods=['GET'])
def get_all_dishes():
    return render_template('view_dishes.html',dishes=dishes)

@app.route('/update_dishes/<int:dish_id>', methods=["POST","GET"])
def update_dish(dish_id):
    dish = find_dish(dish_id)
    if request.method == 'POST':
        if dish is None:
            return jsonify({'message': 'Dish not found'}), 404
        data=request.form
        dish['name'] = request.form['name']
        dish['price'] = request.form['price']
        dish['availability'] = True if 'availability' in data else False
        save_data()
        return {"message": "Dish updated successfully"}
    return render_template('update_dish.html',dish=dish)

@app.route('/delete_dish/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    global dishes
    dishes = [dish for dish in dishes if dish['id'] != dish_id]
    return jsonify({'message': 'Dish deleted successfully'})

@app.route('/view_orders', methods=['GET'])
def get_all_orders():
    status = request.args.get('status')
    if status is None or status=='':
        return render_template('view_orders.html',orders=orders)
    new_orders = [x for x in orders if x['status']==status]
    return render_template('view_orders.html',orders=new_orders)

@app.route('/update_Order/<int:id>', methods=['GET',"POST"])
def update_order(id):
    order = find_order(id)
    if request.method == 'POST':
        order['status']=request.form['status']
        save_data()
        return redirect('/view_orders')
    return render_template('update_order.html',order=order)


@app.route('/new_order', methods=['POST',"GET"])
def new_order():
    if request.method == 'POST':
        data = request.form
        
        order = {
            'id': len(orders) + 1,
            'name': data['name'],
            'dish': data['dish'],
            'quantity': int(data['quantity']),
            'status': "preparing",
        }
        for dish in dishes:
            if dish['name']==data['dish']:
                order["price"]=dish['price']*order['quantity']

        orders.append(order)
        save_data()
        return redirect('/view_orders')
    return render_template('new_order.html',dishes=dishes)


if __name__ == '__main__':
    app.run(debug=True)