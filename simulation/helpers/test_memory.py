# Initialize an empty memory (dictionary)
memory = {}

# Simulated interaction (you can replace this with your actual interaction)
conversation = ["hello", "world", "hello", "python", "world", "hello"]

# Update the memory based on the words in the conversation
for word in conversation:
    if word in memory:
        # If the word is already in memory, increment its count
        memory[word] += 1
    else:
        # If the word is not in memory, add it with a count of 1
        memory[word] = 1

# Print the memory
for word, count in memory.items():
    print word + ": " + str(count) + " times"
