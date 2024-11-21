import mysql.connector
from mysql.connector import Error

def crear_tablas():
    try:
        connection = mysql.connector.connect(
            host="cvktne7b4wbj4ks1.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
            user="lruzlxlrpzlm455h",
            password="vrm8gkjtt5drzbws",
            database="kr3s3hkm4w8vai43",
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Script SQL para crear las tablas
            crear_tablas_sql = """
            CREATE TABLE IF NOT EXISTS publishers(
                publisher_id INT NOT NULL,
                name VARCHAR(255) NOT NULL,
                PRIMARY KEY(publisher_id)
            );

            CREATE TABLE IF NOT EXISTS authors(
                author_id INT NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                middle_name VARCHAR(50) NULL,
                last_name VARCHAR(100) NULL,
                PRIMARY KEY(author_id)
            );

            CREATE TABLE IF NOT EXISTS books(
                book_id INT NOT NULL,
                title VARCHAR(255) NOT NULL,
                total_pages INT NULL,
                rating DECIMAL(4, 2) NULL,
                isbn VARCHAR(13) NULL,
                published_date DATE,
                publisher_id INT NULL,
                PRIMARY KEY(book_id),
                CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
            );

            CREATE TABLE IF NOT EXISTS book_authors (
                book_id INT NOT NULL,
                author_id INT NOT NULL,
                PRIMARY KEY(book_id, author_id),
                CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
                CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES authors(author_id) ON DELETE CASCADE
            );
            """

            cursor.execute(crear_tablas_sql, multi=True)
            connection.commit()
            print(".  ")
            print("Tablas creadas correctamente.")
            print(".  ")

    except Error as e:
        print("Error al crear las tablas:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("  ")
            print("Conexión cerrada.")
            print("  ")

def listar_tablas():
    try:
        connection = mysql.connector.connect(
            host="cvktne7b4wbj4ks1.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
            user="lruzlxlrpzlm455h",
            password="vrm8gkjtt5drzbws",
            database="kr3s3hkm4w8vai43",
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES;")
            tablas = cursor.fetchall()
            
            if tablas:
                print("  ")
                print("Tablas en la base de datos:")
                print("  ")
                for tabla in tablas:
                    print(f"- {tabla[0]}")
            else:
                print("No se encontraron tablas en la base de datos.")

    except Error as e:
        print("Error al listar las tablas:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

def insertar():
    try:
        connection = mysql.connector.connect(
            host="cvktne7b4wbj4ks1.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
            user="lruzlxlrpzlm455h",
            password="vrm8gkjtt5drzbws",
            database="kr3s3hkm4w8vai43",
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insertar_sql = """
            -- publishers
            INSERT INTO publishers(publisher_id, name) VALUES (1, 'O Reilly Media');
            INSERT INTO publishers(publisher_id, name) VALUES (2, 'A Book Apart');
            INSERT INTO publishers(publisher_id, name) VALUES (3, 'A K PETERS');
            INSERT INTO publishers(publisher_id, name) VALUES (4, 'Academic Press');
            INSERT INTO publishers(publisher_id, name) VALUES (5, 'Addison Wesley');
            INSERT INTO publishers(publisher_id, name) VALUES (6, 'Albert&Sweigart');
            INSERT INTO publishers(publisher_id, name) VALUES (7, 'Alfred A. Knopf');

            -- authors
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (1, 'Merritt', null, 'Eric');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (2, 'Linda', null, 'Mui');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (3, 'Alecos', null, 'Papadatos');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (4, 'Anthony', null, 'Molinaro');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (5, 'David', null, 'Cronin');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (6, 'Richard', null, 'Blum');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (7, 'Yuval', 'Noah', 'Harari');
            INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (8, 'Paul', null, 'Albitz');

            -- books
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (1, 'Lean Software Development: An Agile Toolkit', 240, 4.17, '9780320000000', '2003-05-18', 5);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (2, 'Facing the Intelligence Explosion', 91, 3.87, null, '2013-02-01', 7);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (3, 'Scala in Action', 419, 3.74, '9781940000000', '2013-04-10', 1);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (4, 'Patterns of Software: Tales from the Software Community', 256, 3.84, '9780200000000', '1996-08-15', 1);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (5, 'Anatomy Of LISP', 446, 4.43, '9780070000000', '1978-01-01', 3);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (6, 'Computing machinery and intelligence', 24, 4.17, null, '2009-03-22', 4);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (7, 'XML: Visual QuickStart Guide', 269, 3.66, '9780320000000', '2009-01-01', 5);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (8, 'SQL Cookbook', 595, 3.95, '9780600000000', '2005-12-01', 7);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (9, 'The Apollo Guidance Computer: Architecture And Operation (Springer Praxis Books / Space Exploration)', 439, 4.29, '9781440000000', '2010-07-01', 6);
            INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (10, 'Minds and Computers: An Introduction to the Philosophy of Artificial Intelligence', 222, 3.54, '9780750000000', '2007-02-13', 7);

            -- book authors
            INSERT INTO book_authors (book_id, author_id) VALUES (1, 1);
            INSERT INTO book_authors (book_id, author_id) VALUES (2, 8);
            INSERT INTO book_authors (book_id, author_id) VALUES (3, 7);
            INSERT INTO book_authors (book_id, author_id) VALUES (4, 6);
            INSERT INTO book_authors (book_id, author_id) VALUES (5, 5);
            INSERT INTO book_authors (book_id, author_id) VALUES (6, 4);
            INSERT INTO book_authors (book_id, author_id) VALUES (7, 3);
            INSERT INTO book_authors (book_id, author_id) VALUES (8, 2);
            INSERT INTO book_authors (book_id, author_id) VALUES (9, 4);
            INSERT INTO book_authors (book_id, author_id) VALUES (10, 1);
            """

            cursor.execute(insertar_sql, multi=True)
            connection.commit()
            print("  ")
            print("Datos insertados correctamente.")
            print("  ")

    except Error as e:
        print("Error al insertar los datos:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

def borrar():
    try:
        connection = mysql.connector.connect(
            host="cvktne7b4wbj4ks1.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
            user="lruzlxlrpzlm455h",
            password="vrm8gkjtt5drzbws",
            database="kr3s3hkm4w8vai43",
            port=3306
        )

        if connection.is_connected():
            cursor = connection.cursor()

            borrar_tablas_sql = """
            DROP TABLE book_authors;
            DROP TABLE books;
            DROP TABLE authors;
            DROP TABLE publishers;
            """

            cursor.execute(borrar_tablas_sql, multi=True)
            connection.commit()

            print("  ")
            print("Tablas eliminadas correctamente.")
            print("  ")

    except Error as e:
        print("Error al eliminar las tablas:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("  ")
            print("Conexión cerrada.")
            print("  ")

def menu():
    while True:
        
        print("  ")
        print("  ")
        print("Estas son las cuatro acciones que puedes realizar según el número que elijas:")
        print("1. Crear tablas")
        print("2. Mostrar las tablas que hay")
        print("3. Insertar datos en cada tabla")
        print("4. Borrar tablas")
        print("----------------------------------")
        print("5. Salir del menú")
        print("  ")
        print("  ")
    
        try:
            opcion = int(input("Ingresa un número del 1 al 5 según lo que quieras hacer: "))
        
            if opcion == 1:
                crear_tablas()
            elif opcion == 2:
                listar_tablas()
            elif opcion == 3:
                insertar()
            elif opcion == 4:
                borrar()
            elif opcion == 5:
                exit()
            else:
                print("Aquí tienes un mensaje de error. Qué esperabas? Esto es lo que pasa cuando introduces un número fuera del rango")
    
        except ValueError:
            print("Por favor, ingresa un número válido.")


# Llamada al menú
menu()