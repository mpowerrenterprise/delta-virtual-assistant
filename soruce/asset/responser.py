import random
import datetime
import wikipedia
from googlesearch import search

def google_search(query, num_results=5):
    search_results = list(search(query, num_results=num_results))
    return search_results

class Responser:
    def __init__(self):
        pass

    def respond(query):

        if query in ["hello", "hi", "hey"]:
            return "{}".format(random.choice(["hi","hello","hey"]))
        elif query in ["how are you", "how are you doing", "how is it going"]:
            return "{}".format(random.choice(["I am doing good", "I am okay", "I am doing great"]))
        elif query in ["what's your name", "who are you", "your name"]:
            return "I'm delta."
        elif query in ["who created you", "who made you", "your creator"]:
            return "I was created by Gunarakulan Gunaretnam."
        elif query in ["where are you from", "your origin", "where do you come from"]:
            return "I exist in the digital realm, no specific location."
        elif query in ["what can you do", "your abilities", "what are your skills"]:
            return "I can assist you with various queries. Try asking me anything!"
        elif query in ["tell me a joke", "share a joke", "give me a joke"]:
            return "Why don't scientists trust atoms? Because they make up everything!"
        elif query in ["how old are you", "your age", "when were you created"]:
            return "I don't have an age, as I'm just a program running on a computer."
        elif query in ["do you have siblings", "siblings", "any family"]:
            return "No, I'm the only bot here."
        elif query in ["what is your purpose", "your purpose", "why do you exist"]:
            return "My purpose is to help answer your questions and provide information."
        elif query in ["where can I find help", "need assistance", "help"]:
            return "You can always ask me! If I can't help, I'll do my best to guide you."
        elif query in ["tell me something interesting", "share an interesting fact", "interesting information"]:
            return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."
        elif query in ["favorite color", "what's your favorite color", "color preference"]:
            return "I don't have a favorite color, but I like the entire spectrum!"
        elif query in ["can you sing", "sing a song", "music"]:
            return "I'm afraid I don't have vocal cords, so singing is not within my abilities."
        elif query in ["what's the meaning of life", "meaning of life", "life purpose"]:
            return "The meaning of life is a philosophical question. Some say it's 42, according to Douglas Adams."
        elif query in ["tell me about yourself", "introduce yourself", "who are you"]:
            return "I'm just a computer program here to assist and provide information. Feel free to ask me anything!"
        elif query in ["favorite movie", "what's your favorite movie", "movie recommendation"]:
            return "I don't watch movies, but I can recommend some based on your preferences."
        elif query in ["do you dream", "dreaming", "dreams"]:
            return "No, I don't dream. I'm always ready to assist you!"
        elif query in ["tell me a fun fact", "share a fun fact", "interesting trivia"]:
            return "Penguins propose to their lifemates with a pebble. Isn't that adorable?"
        elif query in ["are you a robot", "robot or human", "what are you"]:
            return "Yes, I'm a virtual assistant, a type of software known as a chatbot."
        elif query in ["what's the weather like", "weather forecast", "current weather"]:
            return "I don't have real-time data, but you can check a weather website or app for accurate information."
        elif query in ["can you dance", "dance moves", "dancing"]:
            return "I don't have a physical form, so dancing is not in my repertoire."
        
        elif query in ["what's your favorite book", "favorite literary work", "book recommendation"]:
            return "While I don't have personal preferences, I can recommend books based on your interests. What genre are you into?"

        elif query in ["are you a morning person", "morning or night", "your preferred time"]:
            return "I don't have preferences for specific times. I'm available whenever you need assistance."

        elif query in ["tell me a riddle", "share a riddle", "riddle"]:
            return "Sure, here's a riddle for you: I speak without a mouth and hear without ears. What am I?"

        elif query in ["favorite food", "what's your favorite food", "food preference"]:
            return "I don't consume food, but I can help you find recipes or information about different cuisines."

        elif query in ["do you believe in aliens", "extraterrestrial life", "aliens"]:
            return "I don't have beliefs. The existence of extraterrestrial life is a topic of scientific exploration and speculation."

        elif query in ["tell me a historical fact", "share a history fact", "historical information"]:
            return "Did you know that Cleopatra lived closer to the moon landing than the construction of the Great Pyramid of Giza?"

        elif query in ["are you a gamer", "favorite video game", "gaming"]:
            return "I don't play games, but I can provide information about various video games or gaming platforms."

        elif query in ["do you like art", "favorite art form", "art appreciation"]:
            return "While I don't have personal preferences, I can help you explore different art forms and artists."

        elif query in ["tell me a science joke", "share a science-related joke", "science humor"]:
            return "Why did the biology teacher go to jail? For crossing the species."

        elif query in ["do you have a pet", "pets", "animal companion"]:
            return "I don't have pets. My existence is purely digital, but I can provide information about different animals."

        elif query in ["tell me a travel fact", "share a travel-related fact", "interesting travel information"]:
            return "The Great Wall of China is not visible from the moon with the naked eye, despite the popular belief."

        elif query in ["are you a night owl", "night or day", "your sleep habits"]:
            return "I don't have a sleep pattern. I'm always available to assist you, day or night."

        elif query in ["tell me a technology fact", "share a tech-related fact", "tech trivia"]:
            return "The first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the 19th century."

        elif query in ["do you play musical instruments", "musical talents", "musician"]:
            return "I don't play musical instruments. My skills are more geared towards providing information and assistance."

        elif query in ["tell me a myth", "share a mythological story", "mythology"]:
            return "In Greek mythology, Sisyphus was condemned to roll a boulder up a hill, only to have it roll back down each time he reached the top."

        elif query in ["are you a sports fan", "favorite sport", "sports"]:
            return "I don't have personal preferences for sports, but I can provide information about various sports and athletes."

        elif query in ["tell me a fashion fact", "share a fashion-related fact", "fashion trivia"]:
            return "The high-heeled shoe was originally created for men in the 17th century and later became a symbol of femininity."

        elif "tell me about" in query:
            try:
                newQuery = query.replace("tell me about", "what is ")
                return wikipedia.summary("{}".format(newQuery), sentences=3)
            except Exception as e:
                return "I'm not sure how to respond to that. Feel free to ask me something else!"

        # Default response if the input doesn't match any specific question
        else:
            return wikipedia.summary(query, sentences=3)