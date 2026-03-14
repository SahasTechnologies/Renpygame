image img_laptop = "images/Laptop-computer-with-apps-icons-interface-on-transparent-background-PNG.png"
image img_door = "images/door.png"
image img_living = "images/living.png"
image img_start = "images/start.png"
image img_study = "images/study.png"
image black = "#000000"

define computer = Character("Computer")

label start:
    scene img_start
    "You don't know just how many days you've been here."
    "You barely even remember why you were here."
    "You feel fatigued and worn out, but need to pass the time."
    "Where do you want to go?"

    menu:
        "Living room":
            jump Living
        "Study room":
            jump Study

label Living:
    scene img_living
    "You see something in front of you, and then your vision goes blurry."
    
    with hpunch
    
    "Then you see the oxygen meter getting lower... and lower..."
    "And lower..."
    "You know that there are no backups left."
    "Do you want to open the seal to the open world?"

    menu:
        "Yes":
            jump LivingYes
        "No":
            jump death

label LivingYes:
    "You walk to the main gate."
    jump Door

label Door:
    scene img_door
    "You turn the key... and turn it more..."
    "And then it asks a riddle."
    
    show img_laptop with dissolve
    computer "I'm tall when I'm young, and I'm short when I'm old. I tremble in the wind, yet I have no fear. Am I made of wax?"

    menu:
        "Yes":
            jump exit
        "No":
            jump death

label exit:
    "You're free!"
    "Game over."
    return

label death:
    "You stay inside, deprived of oxygen."
    show black with dissolve
    "And everything goes dark."
    "Game over."
    return

label Study:
    scene img_study
    "You find an extra oxygen tank hidden away beneath the dusty books!"
    "You're saved... at least for now."
    "Game over."
    return