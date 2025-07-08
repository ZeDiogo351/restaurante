from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure key in production

# Database initialization

def init_db():
    conn = sqlite3.connect('restaurant.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS menu (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 description TEXT,
                 price REAL NOT NULL,
                 category TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL,
                 date TEXT NOT NULL,
                 time TEXT NOT NULL,
                 people INTEGER NOT NULL,
                 status TEXT DEFAULT 'Pending')''')
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL,
                 role TEXT DEFAULT 'admin')''')
    conn.commit()
    conn.close()

# Initialize database
init_db()

# Helper function to get database connection
def get_db_connection():
    conn = sqlite3.connect('restaurant.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM menu WHERE category = 'Appetizer'")
    appetizers = c.fetchall()
    c.execute("SELECT * FROM menu WHERE category = 'Main Course'")
    main_courses = c.fetchall()
    c.execute("SELECT * FROM menu WHERE category = 'Dessert'")
    desserts = c.fetchall()
    conn.close()
    return render_template('index.html', appetizers=appetizers, main_courses=main_courses, desserts=desserts)

@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        people = request.form['people']
        
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO reservations (name, email, date, time, people) VALUES (?, ?, ?, ?, ?)",
                 (name, email, date, time, people))
        conn.commit()
        conn.close()
        flash('Reservation submitted successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('reserve.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                     (username, generate_password_hash(password), 'admin'))
            conn.commit()
            flash('Admin registered successfully! You can now log in.', 'success')
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            conn.close()
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['role'] = user[3]
            flash('Logged in successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/admin')
def admin_dashboard():
    if not session.get('role') == 'admin':
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM menu")
    menu_items = c.fetchall()
    c.execute("SELECT * FROM reservations")
    reservations = c.fetchall()
    conn.close()
    return render_template('admin.html', menu_items=menu_items, reservations=reservations)

@app.route('/admin/add_menu', methods=['POST'])
def add_menu():
    if not session.get('role') == 'admin':
        return redirect(url_for('login'))
    
    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])
    category = request.form['category']
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
             (name, description, price, category))
    conn.commit()
    conn.close()
    flash('Menu item added successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/update_status/<int:id>', methods=['POST'])
def update_status(id):
    if not session.get('role') == 'admin':
        return redirect(url_for('login'))
    
    status = request.form['status']
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE reservations SET status = ? WHERE id = ?", (status, id))
    conn.commit()
    conn.close()
    flash('Reservation status updated!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/delete_menu/<int:id>')
def delete_menu(id):
    if not session.get('role') == 'admin':
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM menu WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash('Menu item deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with a secure key

# Lista de usuários autorizados (email e senha hash)
AUTH_USERS = {
    'user1@example.com': generate_password_hash('password1'),
    'user2@example.com': generate_password_hash('password2'),
    'user3@example.com': generate_password_hash('password3')
}

# ... (outras funções como init_db, get_db_connection permanecem)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in AUTH_USERS and check_password_hash(AUTH_USERS[username], password):
            session['user_id'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/')
@app.route('/index')
def index():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM menu WHERE category = 'Appetizer'")
    appetizers = c.fetchall()
    c.execute("SELECT * FROM menu WHERE category = 'Main Course'")
    main_courses = c.fetchall()
    c.execute("SELECT * FROM menu WHERE category = 'Dessert'")
    desserts = c.fetchall()
    conn.close()
    return render_template('index.html', appetizers=appetizers, main_courses=main_courses, desserts=desserts)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

# ... (outras rotas permanecem)