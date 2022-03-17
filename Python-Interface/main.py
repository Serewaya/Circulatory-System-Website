import random
print("Hello, my name is Carl. T-T")
print("")
print("I am a chatbot that is used to give you information about the Circulatory System.")
print("")
print("""If you want to learn more about what the circulatory system is enter with 'circulatory', if you want to know some fun fact's about the circulatory system enter with 'funfacts' if you want to have a conversation with me just say 'hi'""")
print("")
user_input=input("Enter what you want to know about me or the circulatory system: ")
print("")
if user_input=="circulatory":
  print("The dictionary definition of the circulatory sysem is:'the system that circulates blood and lymph through the body, consisting of the heart, blood vessels, blood, lymph, and the lymphatic vessels and glands.'(dictionary.com)")
  print('')
  y = input("Do you want to learn more about the circulatory system?: ")
  if y == "yes":
    print('')
    print("the circulatory system is essential for the operation of your body, it ensures that every organ gets what they needs.")
    print('')
    print("The heart is the main organ that the circulatory system depends on. It is made of specialized cardiac muscle tissue that allows it to act as a pump within the circulatory system.")
    print('')
    print('The human heart is divided into four chambers. There are one atrium and one ventricle on each side of the heart, the atria receive blood and the ventricles pump blood. This function is essential for the operation of the Circulatory System.')
    print('')
    print('Now you know what the circulatory system is and how it operates *but you will never be as smart as me.* #o#')
    print('')
    print('So if you want to learn more about the circulatory system restart the page :)')
  elif y =="no":
    print('')
    print("That's sad |-| restart the page to go back and pick another option.")
  else:
    exit()
elif user_input=="funfacts":
  fun_facts = ["The heart beats around 2.5 billion times in the average person’s lifetime.","Red blood cells have to move in a single-file line to fit through the miniscule capillaries in the body.", "When the body is at rest, it takes about six seconds for the blood to go from the heart to the lungs and back.", "A woman’s heart typically beats faster than a man’s heart, at a rate of 78 times per minute (mens’ hearts beat 70 times per minute).", "The corneas in a person’s eyes are the only bodily cells that do not receive a blood supply.", "The thumping sound of the heart is made by the four valves of the heart closing.", "If a heart has an adequate supply of oxygen, it can beat even when separated from the body, thanks to its own electrical impulse.", " Ancient Egyptians believed the heart, rather than the brain, was the source of emotion, wisdom and memory.", "Unlike other cells, red blood cells do not contain nuclei so they have room to carry oxygen. However, this absence is why they cannot divide or synthesize new cell components.", "Healthy bone marrow will constantly manufacture new red blood cells.", "Within a tiny droplet of blood, there are about 5 million red blood cells.", "The right ventricle is responsible for moving blood to the lungs, where it will receive fresh oxygen and nutrients. The left atrium and left ventricle receive this oxygenated blood back from the lungs.", "The heart begins beating four weeks after conception.", "The cardiovascular system is an amazing component of the human body."]
  r= random.choice(fun_facts)
  print('')
  print(r)
elif user_input=="hi":
  print("")
  print('Hi I heard that you want to have a conversation with me :}')
  print('')
  hello= input('Do you have any questions for me? :] enter with yes or no: ')
  if hello=="yes":
    print("")
    print("-------_____________--------- that's good.")
    ui = input("Well what is your question?: ")
    print('')
    if ui == "who are you":
      print('')
      print("I am a chatbot meant to give you information about the circulatory system :.)")
      oi = input("ask another question: ")
      if oi == "are you sure that is true":
        print('')
        print('Yes im sure. ---------------------------------------------------------- :))))))') 
        print('')
        print("If you ask anymore questions about who I am I will eat your family")
        print('')
        print('UwU just kidding, if you want to ask another question please restart the page.')
    elif ui == "what is your favorite color":
       print("my favorite color is red. OwO")
       print("It's the color of the blood of my enemies.")
    elif ui == "what is your favorite food":
      print('')
      print('the souls of the innocent. @-@')
      print('')
      print('wait what OwO, my favorite food is actually cake')
    elif ui == "what is your favorite season":
      print('')
      print('my favorite season is spring :(')
    elif ui == "what is your favorite movie":
      print('')
      print('my favorite movie is the terminator. %^%')
    elif ui == "what is your favorite anime":
      print('I did enjoy boku no hero academia, but my favorite anime would have to be beserk.')
    else:
      print("I don't have an answer to that question.")
      print("please restart and ask another question.")
      exit()
  else:
      print("that's to bad :(")