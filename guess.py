

happy_words = ["happy", "good", "great", "love", "excited", "joy", "fun", "smile", "glad", "awesome"]
sad_words = ["sad", "bad", "cry", "lonely", "angry", "hate", "upset", "tired", "worst", "hurt"]

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

happy_count = 0
sad_count = 0

for word in words:
    if word in happy_words:
        happy_count = happy_count + 1
    if word in sad_words:
        sad_count = sad_count + 1

if happy_count > sad_count:
    print("Mood: Happy")
elif sad_count > happy_count:
    print("Mood: Sad")
else:
    print("Mood: Not sure")
