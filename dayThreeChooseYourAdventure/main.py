print('''
            .
         z$$$$$e.
       .$$$$$$$$$c                                 -r     d
       $$$$$$$$$$$.                                 *c.  'L
      4$$$$$$$$$$$F                             4c   "*e. "%c
      ^$$$$$$$$$$$F                              "b    ^b   "*
       *$$$$$$$$$$  ..                            P     $    J"
       ^*$$$$$$$$\e$$$e.                         d"    .F   z"
         "*$$$P".$$$$$$$c                       d%     J" .d"   .P
                $$$$$$$$$$e.                    $      P z*"  .d"
                $$$$$$$$$$$$b.                  ^*ee...  "   zP"
                "*$$$$$$$$$$$$$ee..                ^""*    .d"
                 .$$$$$$$$$$$$$$$$$$eee......eeedec.      e*   .ze
                z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.  .P" .z@*"
               z$$$$$""*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c ^ eP""
              d$$$$$"    "*$$$$$$$$$$$$$$$$$$$$$$$$$$$$   "
            .d$$$$P"       ^"*$$$$$$$$$$$$$$$$$$$$$$$$$   ****$eee
           .$$$$$*            ^"$$$$$$$$$$*$$$$$$$$$$$"   ec.
         .z$$$$$"                "*$$$$$$$$$$$$$$$$$*"     ""**ec.
    .zed$$$$$$$"                    "*$$$$$$$$$$*"              ""
                                    .d$$$$$$$P"
                                  .d$$$$$$$*"
                                z$$$$$$$$"
                              .$$$$$$$*"
                              d$$$$$*"
                             z$$$$"
                            .$$$$$    
''')
print('Welcome to the Fart Story.')
print("")
print("You are sitting in the doctor's office waiting to be called in when you feel a deep and gutteral gurgling from your lower intestine. Oh no. It's gonna be a smelly one.")
choice1 = input("What do you want to do? Should you let it out? Or should you tighten those cheeks and hold on for dear life?(release fart/keep it in)").lower()
print("")

if choice1 == "release fart":
    print("You let it out and you're pretty sure it was not just a fart but it was also some poo.")
    choice2 = input("You have two choices: go to the bathtoom and clean yourself up or you can put on a brave face and leave it in there. Which do you choose?(bathroom/leave it)").lower()
    if choice2 =="bathroom":
        print("You go into the bathroom, throw your underwear in the trash and stick your butt under the sink. Crisis averted. You win the game.")
    elif choice2 == "leave it":
        print("Interesting choice. You look around the room to see if anyone noticed. Nobody seems to have noticed. You squish it down with your cheeks and bite your knuckle. You are a sick fuck. You lose the game.")
    else:
        print("That wasn't a valid choice. The secretary comes out from behind the desk and shoves a pen into your throat and you bleed out on the floor. Game Over. You Lose.")
elif choice1 == "keep it in":
    print("You tried to hold it in but it was too powerful and some snuck its way out. The room is starting to smell.")
    choice3 = input("You can get up and spray the air freshner on the other side of the room or you can own your fart.(air freshner/own it)")
    if choice3 =="air freshner":
        print("You go and spray the air freeshner. Ah yes, fresh lilacs. The room smells better now than it did before. You win. Everybody in the room applauds.")
    elif choice3 == "own it":
        print("You decided to own it. You stand up on top of your chair and announce to the whole room that you are the reason the room now smells like rotten eggs. A fat zitty man in the corner begins to slow clap you, while an old lady in a knit bonnet passes out. You win. But at what cost?")
    else:
        print("What does that even mean? You lose.")
else:
    print("Nope. The doctor came in and stabbed you in the eye with a tongue depresser and you died. You lose.")

