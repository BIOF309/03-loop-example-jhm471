
# coding: utf-8

# In[21]:


# While loop example to count the number of words spoken in 10 seconds.
# Python needs to be reset before running the program successively to ensure correct timing.
# The following packages need to be installed: 1) pyaudio 2) google-api-python-client 
# 3) FLAC (free lossless audio codec) on some systems such as Raspberry Pi

# Import packages for speech recognition and time.
import speech_recognition as sr
import time

# Create while loop that will record audio for 10 seconds.
t_end = time.time() + 10
r = sr.Recognizer()
print("Say as many words as you can that start with the letter 'b'")
while time.time() <= t_end:
    with sr.Microphone() as source:
        audio = r.listen(source)

# Print out what was recorded.
words = r.recognize_google(audio)
print("Google speech recognition thinks you said: " + words)

# Create list that only contains words starting with letter "b".
words = words.lower()
words_list = words.split(" ")
words_list_b = []
for i in range(len(words_list)):
    if words_list[i][0] == "b":
        words_list_b.append(words_list[i])

# Count the number of unique words that were spoken that start with the letter "b".        
counter = 0
unique_list = []
for i in range(len(words_list_b)):
    if words_list_b[i] in unique_list:
        continue
    else:
        unique_list.append(words_list_b[i])
        counter += 1

print("You said " + str(counter) + " unique words")            

