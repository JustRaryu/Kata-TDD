from datetime import datetime

class Ohce:
    def __init__(self, user="Usuario", hour=None):
        self.user = user
        self.hour = hour if hour is not None else datetime.now().hour

    def greet(self):
        if 6 <= self.hour < 12:
            return f"¡Buenos días {self.user}!"
        elif 12 <= self.hour < 20:
            return f"¡Buenas tardes {self.user}!"
        else:
            return f"¡Buenas noches {self.user}!"
        
    def reverse(self, text):
        return text[::-1]
    
    def is_palindrome(self, text):
        return text == text[::-1]

    def process(self, text):
        reversed_text = self.reverse(text)
        if self.is_palindrome(text):
            return f"{reversed_text}\n¡Bonita palabra!"
        return reversed_text
