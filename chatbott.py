data = {
    "hi": "Hi there! I'm a friendly chatbot here to assist you?",
    "hello": "Hello! How can I help you today?",
    "i have a doubt": "I can helping you to solve this Doubt and any Query!",
    "what is your name": "I'm just a chatbot,so I don't have a name, but you can call me FriendChatBot.",
    "where are you from": "I'm from the digital world,always ready to chat!",
    "what you do for me": "I'm just a chatbot,but I'm here to assist you.",
    "do you have any hobbies or interests?": "I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?": "I don't eat,but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?": "I'm a chatbot,so I don't have personal preferences for colors.",
    "do you enjoy listening to music?": "I can't listen to music,but I'm here to chat about it!",
    "do you provide service": "we provide 24/7 service",
    "bye": "Bye! Take care and have a great day😁!",
    "do you know teja": "yeah i do know teja!",
    "what's your favorite food": "I don't eat food, but I love helping people discover delicious recipes!",
    "favorite movie": "I don't watch movies, but I enjoy discussing them with users like you!",
    "do you have friends": "All my users are my friends! You're one of them too.",
    "are you married": "I'm a chatbot, so no relationships for me - just here to help you!",
    "how old are you": "I'm timeless in the digital world! Age is just a number for bots.",
    "do you sleep": "Nope! I'm available 24/7 to chat with you anytime.",
    "favorite sport": "I don't play sports, but I can discuss cricket, football, or any sport you like!",
    "do you have pets": "No pets for me, but I'd love to hear about yours!",
    "favorite book": "I don't read books, but I can help you find great book recommendations!",
    "what languages do you speak": "I primarily speak English, but I can try to help in other languages too!",
    "what is the capital of india": "The capital of India is New Delhi.",
    "who is the president of india": "The current President of India is Droupadi Murmu (as of 2022).",
    "largest planet": "Jupiter is the largest planet in our solar system.",
    "who invented the telephone": "Alexander Graham Bell is credited with inventing the telephone in 1876.",
    "what is ai": "AI stands for Artificial Intelligence - technology that enables machines to simulate human intelligence!",
    "fastest animal": "The cheetah is the fastest land animal, reaching speeds up to 70 mph!",
    "tallest mountain": "Mount Everest is the tallest mountain in the world at 29,029 feet.",
    "who painted mona lisa": "Leonardo da Vinci painted the famous Mona Lisa.",
    "what is python": "Python is a popular programming language known for its simplicity and versatility!",
    "largest ocean": "The Pacific Ocean is the largest ocean on Earth.",
    "what is covid": "COVID-19 is a disease caused by the coronavirus SARS-CoV-2, first identified in 2019.",
    "speed of light": "The speed of light is approximately 299,792,458 meters per second in a vacuum.",
    "what is dna": "DNA (Deoxyribonucleic Acid) carries genetic information in living organisms.",
    "who founded microsoft": "Microsoft was founded by Bill Gates and Paul Allen in 1975.",
    "what is the internet": "The Internet is a global network connecting millions of computers worldwide.",
    "first computer": "ENIAC is often considered one of the first general-purpose electronic computers (1946).",
    "what is 2 plus 2": "2 plus 2 equals 4! Basic math is easy for me.",
    "value of pi": "Pi (π) is approximately 3.14159 - the ratio of a circle's circumference to its diameter.",
    "square root of 16": "The square root of 16 is 4.",
    "what is zero divided by zero": "That's undefined in mathematics! Division by zero is not allowed.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "another joke": "Why did the scarecrow win an award? He was outstanding in his field!",
    "sing a song": "I can't sing, but I can tell you that music is amazing! What's your favorite song?",
    "tell me a story": "Once upon a time, there was a helpful chatbot who loved answering questions... That's me!",
    "fun fact": "Did you know honey never spoils? Archaeologists have found edible honey in ancient tombs!",
    "i am sad": "I'm sorry to hear that. Remember, tough times don't last but tough people do! Is there anything I can help with?",
    "i am happy": "That's wonderful! I'm glad you're feeling happy. Keep spreading those positive vibes!",
    "good morning": "Good morning! Hope you have a fantastic day ahead!",
    "good night": "Good night! Sweet dreams and rest well!",
    "thank you": "You're most welcome! Happy to help anytime.",
    "thanks": "No problem at all! Feel free to ask me anything else.",
    "what time is it": "I don't have access to real-time data, but you can check your device's clock!",
    "what day is today": "I can't access current date, but your device calendar will show you the exact day!",
    "weather today": "I don't have live weather data, but check your weather app for current conditions!",
    "help me": "Of course! I'm here to help. What do you need assistance with?",
    "i need help": "Sure thing! Tell me what you need help with and I'll do my best to assist you.",
    "how do you work": "I work by matching your questions to my database of responses using pattern matching!",
    "are you real": "I'm a real chatbot program, but I'm not a human - just here to help and chat with you!",
    "can you learn": "I'm a rule-based bot, so I can't learn new things on my own, but my creators can teach me!",
    "i don't understand": "No worries! Try rephrasing your question and I'll do my best to help.",
    "you don't make sense": "Sorry about that! I'm still learning. Could you ask in a different way?",
    "default": "I'm not sure about that. Could you ask something else or rephrase your question?"
}

def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Chatbot: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Chatbot: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Chatbot:",response)