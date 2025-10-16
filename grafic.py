class UserProfile:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __str__(self):
        return f"Аты: {self.name}, Email: {self.email}, Рөлі: {self.role}"


# Бастапқы объект
user1 = UserProfile("Алина", "alina@example.com", "қолданушы")

print("Бастапқы профиль:")
print(user1)

# Өзгеріс енгізу үшін жаңа объект жасаймыз
user2 = UserProfile("Алина", "alina_new@example.com", "әкімші")

print("\nЖаңартылған профиль:")
print(user2)
