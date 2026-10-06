



print("Welcome to Parnia's general knowledge quizz, each question is worth 5 points, good luck")




questions = [
    "Which animal has three hearts? A) Shark B) Octopus C) Dolphin D) Penguin",

    "Which country gave the Statue of Liberty to the United States? A) France B) Italy C) Spain D) Germany",

    "What is the closest planet to the Sun? A) Venus B) Earth C) Mercury D) Mars",

    "Which human organ can regenerate itself? A) Heart B) Liver C) Brain D) Lung",

    "Which city is famous for the Colosseum? A) Athens B) Rome C) Paris D) Madrid",

    "What is the largest desert in the world? A) Sahara Desert B) Gobi Desert C) Antarctic Desert D) Arabian Desert",

    "Which animal is known for changing its color to hide? A) Chameleon B) Kangaroo C) Zebra D) Panda",

    "Who was the first person to walk on the Moon? A) Yuri Gagarin B) Neil Armstrong C) Buzz Aldrin D) Elon Musk",

    "Which country has a maple leaf on its flag? A) Canada B) Sweden C) Norway D) Finland",

    "What is the hardest natural substance on Earth? A) Gold B) Iron C) Diamond D) Silver",

    "Which planet has the most famous ring system? A) Mars B) Saturn C) Venus D) Mercury",

    "Which animal can sleep while standing? A) Horse B) Dog C) Rabbit D) Monkey",

    "What is the smallest country in the world? A) Monaco B) Vatican City C) Malta D) Luxembourg",

    "Which famous scientist developed the theory of relativity? A) Isaac Newton B) Albert Einstein C) Galileo Galilei D) Nikola Tesla",

    "What is the deepest ocean in the world? A) Atlantic Ocean B) Indian Ocean C) Pacific Ocean D) Arctic Ocean",

    "Which food can last for thousands of years if stored properly? A) Bread B) Honey C) Cheese D) Rice",

    "Which country is shaped like a boot? A) Greece B) Italy C) Portugal D) Croatia",

    "What is the name of the galaxy that contains our Solar System? A) Andromeda B) Milky Way C) Whirlpool D) Sombrero",

    "Which animal has fingerprints that are surprisingly similar to humans? A) Koala B) Tiger C) Elephant D) Penguin",

    "Which ancient civilization built Machu Picchu? A) Romans B) Egyptians C) Incas D) Vikings",

    "What is the fastest animal in the world? A) Cheetah B) Peregrine Falcon C) Horse D) Eagle",

    "Which metal is liquid at room temperature? A) Iron B) Copper C) Mercury D) Aluminum",

    "What is the largest organ of the human body? A) Brain B) Liver C) Skin D) Heart",

    "Which famous ship sank in 1912 after hitting an iceberg? A) Titanic B) Mayflower C) Santa Maria D) Victoria",

    "Which country is home to the ancient city of Petra? A) Jordan B) Egypt C) Turkey D) Morocco",

    "How many bones does an adult human body usually have? A) 106 B) 206 C) 306 D) 406",

    "Which planet is famous for having a giant storm called the Great Red Spot? A) Jupiter B) Saturn C) Neptune D) Uranus",

    "Which animal is the largest living land animal? A) Giraffe B) Hippopotamus C) African Elephant D) Rhinoceros",

    "What does the 'WWW' in a website address stand for? A) World Wide Web B) World Web Window C) Wide World Website D) Web World Wide",

    "Which country is famous for the ancient pyramids of Giza? A) Mexico B) Egypt C) Peru D) India"
]

answers = ["B","A","C","B","B","C","A","B","A","C","B","A","B","B","C","B","B","B","A","C","B","C","C","A","A","B","A","C","A","B"]

score=[]


while True:
  import random
  question= random.choice(questions)
  print(question)
  questions.remove(question)
  answer=input("your answer:")

  match question:
    case"Which animal has three hearts? A) Shark B) Octopus C) Dolphin D) Penguin":
      if answer=="B"or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which country gave the Statue of Liberty to the United States? A) France B) Italy C) Spain D) Germany":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"What is the closest planet to the Sun? A) Venus B) Earth C) Mercury D) Mars":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which human organ can regenerate itself? A) Heart B) Liver C) Brain D) Lung":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which city is famous for the Colosseum? A) Athens B) Rome C) Paris D) Madrid":
      if answer=="B" or answer=="b":
       score.append(5)
       print("bravo")
      else:
        print("oops")

    case"What is the largest desert in the world? A) Sahara Desert B) Gobi Desert C) Antarctic Desert D) Arabian Desert":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which animal is known for changing its color to hide? A) Chameleon B) Kangaroo C) Zebra D) Panda":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Who was the first person to walk on the Moon? A) Yuri Gagarin B) Neil Armstrong C) Buzz Aldrin D) Elon Musk":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which country has a maple leaf on its flag? A) Canada B) Sweden C) Norway D) Finland":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")
   
    case"What is the hardest natural substance on Earth? A) Gold B) Iron C) Diamond D) Silver":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "Which planet has the most famous ring system? A) Mars B) Saturn C) Venus D) Mercury":
      if answer=="B" or answer=="b":
       score.append(5)
       print("bravo")
      else:
        print("oops")

    case"Which animal can sleep while standing? A) Horse B) Dog C) Rabbit D) Monkey":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "What is the smallest country in the world? A) Monaco B) Vatican City C) Malta D) Luxembourg":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which famous scientist developed the theory of relativity? A) Isaac Newton B) Albert Einstein C) Galileo Galilei D) Nikola Tesla":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"What is the deepest ocean in the world? A) Atlantic Ocean B) Indian Ocean C) Pacific Ocean D) Arctic Ocean":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which food can last for thousands of years if stored properly? A) Bread B) Honey C) Cheese D) Rice":
      if answer=="B" or answer=="b":
       score.append(5)
       print("bravo")
      else:
        print("oops")

    case "Which country is shaped like a boot? A) Greece B) Italy C) Portugal D) Croatia":
      if answer=="B" or answer=="b":
       score.append(5)
       print("bravo")
      else:
        print("oops")

    case "What is the name of the galaxy that contains our Solar System? A) Andromeda B) Milky Way C) Whirlpool D) Sombrero":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "Which animal has fingerprints that are surprisingly similar to humans? A) Koala B) Tiger C) Elephant D) Penguin":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "Which ancient civilization built Machu Picchu? A) Romans B) Egyptians C) Incas D) Vikings":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"What is the fastest animal in the world? A) Cheetah B) Peregrine Falcon C) Horse D) Eagle":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "Which metal is liquid at room temperature? A) Iron B) Copper C) Mercury D) Aluminum":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"What is the largest organ of the human body? A) Brain B) Liver C) Skin D) Heart":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "Which famous ship sank in 1912 after hitting an iceberg? A) Titanic B) Mayflower C) Santa Maria D) Victoria":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which country is home to the ancient city of Petra? A) Jordan B) Egypt C) Turkey D) Morocco":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"How many bones does an adult human body usually have? A) 106 B) 206 C) 306 D) 406":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case "Which planet is famous for having a giant storm called the Great Red Spot? A) Jupiter B) Saturn C) Neptune D) Uranus":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which animal is the largest living land animal? A) Giraffe B) Hippopotamus C) African Elephant D) Rhinoceros":
      if answer=="C" or answer=="c":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"What does the 'WWW' in a website address stand for? A) World Wide Web B) World Web Window C) Wide World Website D) Web World Wide":
      if answer=="A" or answer=="a":
        score.append(5)
        print("bravo")
      else:
        print("oops")

    case"Which country is famous for the ancient pyramids of Giza? A) Mexico B) Egypt C) Peru D) India":
      if answer=="B" or answer=="b":
        score.append(5)
        print("bravo")
      else:
        print("oops")

  if questions==[]:
    break


print("your final score is ", sum(score))

   
    

    

    

    
    


    


