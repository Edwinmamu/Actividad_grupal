from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Datos ficticios de productos
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 800},
    {"id": 2, "nombre": "Smartphone", "precio": 500},
    {"id": 3, "nombre": "Tablet", "precio": 300},
    {"id": 4, "nombre": "Auriculares", "precio": 150},
    {"id": 5, "nombre": "Monitor", "precio": 250}
]

# Carrito de compras
carrito = []

@app.route('/')
def index():
    return render_template('index.html', productos=productos, carrito=carrito)

@app.route('/agregar', methods=['POST'])
def agregar():
    producto_id = int(request.form['producto_id'])
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto:
        carrito.append(producto)
    return redirect(url_for('index'))

@app.route('/comprar')
def comprar():
    if not carrito:
        mensaje = "Tu carrito está vacío. Agrega productos antes de comprar."
    else:
        total = sum(p["precio"] for p in carrito)
        mensaje = f"¡Compra realizada con éxito! Total: ${total}"
        carrito.clear()
    return render_template('index.html', productos=productos, carrito=carrito, mensaje=mensaje)

@app.route('/vaciar_carrito')
def vaciar_carrito():
    carrito.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
