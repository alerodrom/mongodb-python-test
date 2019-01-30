import datetime
import os

from pymongo import ASCENDING, MongoClient

# Variables para la conexión de MongoDB con Docker
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_PORT = os.environ["DATABASE_PORT"]

#Iniciamos el cliente de MongoDB
client = MongoClient()
client = MongoClient(DATABASE_HOST, int(DATABASE_PORT))

#Nos conectamos con la base de datos de pruebas
db = client.test_database
collection = db.test_collection

#Creamos un Post
print("Creamos un Post")
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow(),
}
print(post)
print()

# Obtenemos los Posts
posts = db.posts
#Insertamos el post que hemos creado anteriormente
post_id = posts.insert_one(post).inserted_id
#Listamos todas las colecciones de la base de datos
db.collection_names(include_system_collections=False)
#Devuelve un Post
posts.find_one()

#Creamos un array de Posts
print("Creamos un array de Posts")
new_posts = [
    {
        "author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14),
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45),
    },
]
print(posts)
print()

#Insertamos varios Posts
print("Insertando posts")
result = posts.insert_many(new_posts)
#Devuelve los ids de los Posts creados
print("Devolvemos los ids de los objetos creados... {}".format{result.inserted_ids})

#Devolvemos todos los Posts y los mostramos
print("Devolvemos todos los Posts y los mostramos")
for post in posts.find():
    print('Post con id {}, autor {}, texto {} y tags {}'.format(post.id, post.author, post.text, post.tags))

#Devolvemos todos los Posts filtrados por Autor 'Mike' y los mostramos
print("Devolvemos todos los Posts filtrados por Autor 'Mike' y los mostramos")
for post in posts.find({"author": "Mike"}):
    print('Post con id {}, autor {}, texto {} y tags {}'.format(post.id, post.author, post.text, post.tags))

# Número de posts
print('Número de posts {}'.format(posts.count_documents({})))
# Número de posts filtrados por Author 'Mike'
print("Número de posts por Author 'Mike' {}".format(posts.count_documents({"author": "Mike"})))

d = datetime.datetime(2009, 11, 12, 12)
#Devolvemos todos los Posts menores que la fecha y los mostramos
print("Filtrando posts menores que la fecha {}".format(d))
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print('Post con id {}, autor {}, texto {} y tags {}'.format(post.id, post.author, post.text, post.tags))

result = db.profiles.create_index([("user_id", ASCENDING)], unique=True)

sorted(list(db.profiles.index_information()))

user_profiles = [{"user_id": 211, "name": "Luke"}, {"user_id": 212, "name": "Ziltoid"}]
result = db.profiles.insert_many(user_profiles)
