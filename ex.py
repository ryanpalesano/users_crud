
class User:
#     data = {
#       "id": "1"
#       "first_name": "Ryan",
#       "last_name": "Palesano",
#       "email": "Ryan@ryan.com",
#       "created_at": "10,27,2017",
#       "updated_at": "10,27,2017",
# }
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_addy = data['email_addy']
        self.created_at = data['created_by']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for u in results:
#         cls(u) is equivlant to this -->   ryan = User({
#                                                    "first_name": "Ryan",
#                                                   "last_name": "Palesano",
#                                                    "email": "Ryan@ryan.com",
#                                                     "created_at": "10,27,2017",
#                                                      "updated_at": "10,27,2017",
#                                                    })
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email_addy) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        # comes back as the new row id
        result = connectToMySQL('users').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email_addy=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query,data)
    

ryan = {
    "first_name": "Ryan",
    "last_name": "Palesano",
    "email": "Ryan@ryan.com",
    "created_at": "10,27,2017",
    "updated_at": "10,27,2017",
}

ryan = User({
    "first_name": "Ryan",
    "last_name": "Palesano",
    "email": "Ryan@ryan.com",
    "created_at": "10,27,2017",
    "updated_at": "10,27,2017",
})

