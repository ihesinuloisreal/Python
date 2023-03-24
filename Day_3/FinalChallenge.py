print('''
                            .-"""""-.
                            /\ /\
                           (  _ ._. _  )
                            '. V   V .'
                             | >===< |
                             | >===< |
                           __| >===< |__
                     _..-"X, | >===< | ,X"-.._ 
                _.-"`Xx,   'X; >===< ;X'   ,xX`"-._
            _.'`X.    'Xx.  'X,>===<,X'  .xX'    .X`._
          .'X    `X,   'Xx   'X === X'   xX'   ,X'   X'.
        .xXXXXx,   'X    'Xx  'X = X'  xX'    X'   ,xXXXXx.
      .'       'X.   'X   'Xx  'X X'  xX'   X'   .X'       '.
    .xXXXXXXXXXXXXX,  `Xx. 'Xx, .X. ,xX' .xX'  ,XXXXXXXXXXXXXx.
   /               `X   XX  'XX//^\\XX'  XX   X`               \
  /XXXXXXXXXXXXXXXXXXX   XX  'X\\_//X'  XX   XXXXXXXXXXXXXXXXXXX\
 /                    X_.XX___XX'='XX___XX._X                    \
 |XXXXXXXXXXXXXXXXXXX.'                     '.XXXXXXXXXXXXXXXXXXX|
 |                  /                         \                  |
 |XXXXXXXXXXXXXXXXX/   ..::::.       .::::..   \XXXXXXXXXXXXXXXXX|
 |                /  .'       '     '       '.  \                |
 /XXXXXXXXXXXXXXXX|  _.-"```"-.     .-"```"-._  |XXXXXXXXXXXXXXXX\
|             .==.;   '._(')_.'\   /'._(')_.'   ;.==.             |
|XXXXXXXXXXX.'.-, |            |   |            | ,-.'.XXXXXXXXXXX|
|           |; (               |   |               ) ;|           |
|XXXXXXXXXXX|;  `,            /    .\            ,'  ;|XXXXXXXXXXX|
|           ;;'--            ( _   _ )            --';;           |
|XXXXXXXXXXXX\' o             `"`-`"`             o '/XXXXXXXXXXXX|
|             '-J-'|            : :            |'-L-'             |
|XXXXXXXXXXXXXX(_)X\          __   __          /X(_)XXXXXXXXXXXXXX|
|                   \      .-'  `'`  '-.      /                   |
|XXXXXXXXXXXXXXXXXXXX\    `-:""""""""":-`    /XXXXXXXXXXXXXXXXXXXX|
|                     \      `-.....-'      /                     |
|XXXXXXXXXXXXXXXXXXXXXX'.                 .'XXXXXXXXXXXXXXXXXXXXXX|
 \                       `;-._       _.-;`                       /
  \XXXXXXXXXXXXXXXXXXXXXXX|   `}}}}}`   |XXXXXXXXXXXXXXXXXXXXXXX/
   '.                     |    {{{{{    |                     .'
     '.XXXJGSXXXXXXXXXXXXX|     }}}}    |XXXXXXXXXXXXXXXXXXX.'
       \                  |     {{{     |                  /
        'XXXXXXXXXXXXXXXXX|      }}     |XXXXXXXXXXXXXXXXX'
         \                |      (      |                /
          'XXXXXXXXXXXXXXX|             |XXXXXXXXXXXXXXX'
           \              |             |              /
            \XXXXXXXXXXXXX|             |XXXXXXXXXXXXX/
            |             |             |             |
            |XXXXXXXXXXXXX|             |XXXXXXXXXXXXX|
            |             |             |             |
            |XXXXXXXXXXXXX|             |XXXXXXXXXXXXX|
            \             |             |             /
             'XXXXXXXXXXXX|             |XXXXXXXXXXXX'
               `-.________/             \________.-`
''')

print("Welcome to treasure hunt. Your task is to find the traesure!!!")
choice = input("You are at a cross road, Where would you love to go, Left or Right? (e.g. L for Left and R for Right) ")

if choice == "L" or choice == "l":
    choice = input("You are standing infront of a river! do you want to swim or wait? (e.g. S for swim or W for wait) ")
    if choice == "W" or choice == "w":
        choice = input("Which door will you want to enter? Red(R), Yello(Y) or Blue(B) ")
        if choice == "Y" or choice == "y":
            print("You win")
        elif choice == "R" or choice == "r":
            print("You Lose")
        elif choice == "B" or choice == "b":
            print("You Lose")
        else:
            print("invalid Input")
    elif choice == "S" or choice == "s":
        print("Game Over")
    else:
        print("Invalid Input")
elif choice == "R" or choice == "r":
    print("Game Over")
else:
    print("You've made an invalid input")