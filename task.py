# 1
text = input("Enter a word or sentence: ")
vowels_found = set()
for ch in text:
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        vowels_found.add(ch.lower())

print("Unique vowels found:", vowels_found)
print("Total number of unique vowels:", len(vowels_found))

#2
dictionary={

}
unique_word=set()
user_input=int(input("how many words do you want to add"))
for i in range(user_input+1):
    choice=int(input("press 1 : add, perss 2 : display,press 3 : remove, press4: exit"))
    if choice==1:
        word=input("enter a word")
        if word in unique_word:
            print(f'{word}already exist')
        else:
            meaning=input("enter meaning of that word")
            dictionary[word]=meaning
            unique_word.add(word)
    elif choice==2:
        for i,j in dictionary.items():
            print(i,' ',j)
    elif choice==3:
        word=input("enter a word you want to remove")
        if word not in unique_word:
            print(f'{word} doesnot exist')
        else:
            dictionary.pop(word)
            unique_word.remove(word)
    else:
        break
print(unique_word)

#3
import random

quiz_questions = {
    1: {
        "question": "What is the capital of Nepal?",
        "options": {
            "A": "Pokhara",
            "B": "Lalitpur",
            "C": "Kathmandu",
            "D": "Biratnagar"
        },
        "answer": "C"
    },
    2: {
        "question": "Which language is mainly used for web development?",
        "options": {
            "A": "Python",
            "B": "HTML",
            "C": "C",
            "D": "Java"
        },
        "answer": "B"
    },
    3: {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "/* */",
            "C": "#",
            "D": "<!-- -->"
        },
        "answer": "C"
    }
}


question_keys = list(quiz_questions.keys())
random.shuffle(question_keys)

score = 0


for key in question_keys:
    print("\n" + quiz_questions[key]["question"])

    
    for option, value in quiz_questions[key]["options"].items():
        print(option + ":", value)

    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    
    if user_answer == quiz_questions[key]["answer"]:
        print("Correct answer")
        score += 1
    else:
        print("Wrong answer")
        print("Correct answer is:", quiz_questions[key]["answer"])

print("\nQuiz Finished!")
print("Your final score:", score, "out of", len(quiz_questions))

#4
total_items = int(input("Enter the total number of items purchased: "))

prices = []

for i in range(1, total_items + 1):
    item_price = float(input(f"Enter price of item {i}: "))
    prices.append(item_price)

total_cost = sum(prices)

print("Total cost of all items:", total_cost)


#5

sentence = input("Enter a full sentence: ")

words = sentence.split()

total_words = len(words)

unique_words = set()

for word in words:
    unique_words.add(word.lower())

print("Total number of words:", total_words)
print("Number of unique words:", len(unique_words))
#6


sentence = input("Enter a sentence: ")

words = sentence.split()


word_count = {}

for word in words:
    word = word.lower()          
    word_count[word] = word_count.get(word, 0) + 1


for word in sorted(word_count):
    print(word + ":", word_count[word])


