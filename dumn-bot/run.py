import os

# File to store memory
memory_file = 'chat_memory.txt'

# Function to load the chat history from the memory file
def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, 'r') as file:
            return file.readlines()
    return []

# Function to save a new statement to the memory file
def save_to_memory(statement):
    with open(memory_file, 'a') as file:
        file.write(statement + '\n')

# Function to find patterns in past conversations
def search_memory(user_input, memory):
    user_words = set(user_input.lower().split())
    for line in reversed(memory):
        bot_response = line.split(': ')[-1]
        memory_words = set(line.lower().split())
        # Look for shared words
        if user_words & memory_words:
            return bot_response.strip()  # Return the last known response
    return None

# Function to get a response
def get_bot_response(user_input, memory):
    # Predefined responses
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bunch of code, but I'm functioning well!",
        "bye": "Goodbye! Have a great day!"
    }
    
    # Check if the input matches any predefined responses
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    
    # Try to "learn" from memory by finding a past related statement
    learned_response = search_memory(user_input, memory)
    if learned_response:
        return f"I remember you said something similar before: '{learned_response}'"

    return "I don't know how to respond to that yet, but I'll try to learn!"

# Main loop to handle user input
def chat():
    print("Chatbot initialized! (Type 'exit' to stop)")
    memory = load_memory()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get bot's response
        bot_response = get_bot_response(user_input, memory)
        print("Bot:", bot_response)
        
        # Save both user input and bot response to memory
        save_to_memory(f"You: {user_input}")
        save_to_memory(f"Bot: {bot_response}")
        
        # Update memory in real-time
        memory.append(f"You: {user_input}")
        memory.append(f"Bot: {bot_response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
