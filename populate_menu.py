import sqlite3

def populate_menu():
    conn = sqlite3.connect('restaurant.db')
    c = conn.cursor()
    
    # Entradas (Portuguesas)
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Ameijoas à Bulhão Pato', 'Ameijoas frescas com alho, coentros e azeite', 8.50, 'Appetizer'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Pão com Paté de Sardinha', 'Pão rústico com paté artesanal de sardinha', 5.00, 'Appetizer'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Queijo da Serra com Marmelada', 'Queijo curado com marmelada tradicional', 6.50, 'Appetizer'))
    
    # Pratos Principais (Portugueses)
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Bacalhau à Brás', 'Bacalhau desfiado com ovo, cebola e batata palha', 13.50, 'Main Course'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Cozido à Portuguesa', 'Mistura de carnes e vegetais cozidos ao estilo tradicional', 15.00, 'Main Course'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Arroz de Pato', 'Arroz aromático com pato desfiado e chouriço', 14.50, 'Main Course'))
    
    # Sobremesas (Portuguesas)
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Pastel de Nata', 'Clássico pastel de nata com canela', 2.50, 'Dessert'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Pudim Flan', 'Pudim de ovos com caramelo', 3.00, 'Dessert'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Bolo de Mel', 'Bolo tradicional da Madeira com mel', 4.00, 'Dessert'))
    
    # Bebidas (Portuguesas)
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Vinho Verde', 'Vinho branco leve e fresco', 4.50, 'Beverage'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Ginja', 'Licor de ginja servido em copo de chocolate', 3.00, 'Beverage'))
    c.execute("INSERT INTO menu (name, description, price, category) VALUES (?, ?, ?, ?)",
              ('Sumo de Laranja Natural', 'Sumo fresco espremido na hora', 2.50, 'Beverage'))
    
    conn.commit()
    conn.close()
    print("Menu atualizado com sucesso!")

if __name__ == "__main__":
    populate_menu()