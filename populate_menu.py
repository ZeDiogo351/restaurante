import sqlite3

def populate_menu():
    conn = sqlite3.connect('restaurant.db')
    c = conn.cursor()
    
    # Entradas
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Bruschetta', 'Torrada com tomate fresco, manjericão e azeite', 5.50, 'Appetizer'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Sopa de Cebola', 'Sopa cremosa com queijo gratinado', 4.00, 'Appetizer'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Salada Caprese', 'Tomate, mozzarella fresca e manjericão', 6.00, 'Appetizer'))
    
    # Pratos Principais
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Risoto de Cogumelos', 'Risoto cremoso com cogumelos silvestres', 12.50, 'Main Course'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Frango Assado com Batatas', 'Frango suculento com batatas rústicas', 10.00, 'Main Course'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Peixe Grelhado com Legumes', 'Peixe fresco com legumes sazonais', 14.00, 'Main Course'))
    
    # Sobremesas
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Tiramisú', 'Camadas de café e mascarpone', 5.00, 'Dessert'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Mousse de Chocolate', 'Mousse leve com cacau puro', 4.50, 'Dessert'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Cheesecake de Frutos Vermelhos', 'Cheesecake com topping de frutos vermelhos', 6.00, 'Dessert'))
    
    conn.commit()
    conn.close()
    print("Menu populated successfully!")

if __name__ == "__main__":
    populate_menu()