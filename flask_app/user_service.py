from user_model import User

def get_users():
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    return [vars(user1), vars(user2)]
