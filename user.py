from mysqlconnection import connectToMySQL

db = "users"


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['name']
        self.last_name = data['last_name']
        self.email = data['email_addy']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users ( first_name, last_name, email_addy, created_at, updated_at )
        VALUES ( %(fname)s, %(lname)s, %(email_addy)s, NOW(), NOW() );"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE users
        SET first_name = %(fname)s, last_name = %(lname)s, email_addy = %(email)s, updated_at = NOW()
        WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users
        WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
