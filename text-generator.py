import time
from transformers import pipeline

# Create a text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Generate text based on a prompt
print("Generating text...\n")
time.sleep(1)
prompt = "The stupid story begins. Once upon a time, "
output = generator(prompt, max_length=1000, num_return_sequences=1)

# Print the generated text
with open('generated_ai_text.txt', 'w') as file:
    file.write(output[0]['generated_text'])