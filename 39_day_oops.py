class Insta:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0  # in python we can define a default value to the attributes
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = Insta("001", "Ram")
user_2 = Insta("002", "krishna")

user_1.follow(user_2)
# print(user_1.id,user_1.username)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
