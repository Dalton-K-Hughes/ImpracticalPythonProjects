import sys
import random

print('Welcome to the Psych "Sidekick Name Picker"')
print('A name just like Sean would pick for Gus:\n\n')

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill",
         "Bob", 'Bowel Noises', 'Boxelder', "Bud",
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
         'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
         'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
         'Huggy', 'Ignatious', 'Jimbo', "Joe", 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', 'Mergatroid',
         'Mr Peabody',  'Oinks', 'Old Scratch', 'Ovaltine',
         'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
         'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         "Sid", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
         'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
         'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         "Winston", 'Worms')

middle = ('Beenie-Weenie', 'Stinkbug', 'Lite', 'Pottin Soil', 'Oil-Can', 
        'Lunch Money', 'Jazz Hands', 'The Squirts')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

def main():
    while True:
        
        chance = random.randint(1, 4)
        first_name = random.choice(first)
        last_name = random.choice(last)
        middle_name = ''
        


        print('\n\n')
        if chance == 2:
            middle_name = random.choice(middle)
            print('{} {} {}'.format(first_name, middle_name, last_name), file=sys.stderr)
        else:
            print('{} {}'.format(first_name, last_name), file=sys.stderr)
        print('\n\n')

        try_again = input('\n\nTry Again? (Enter else n to quit)\n ')
        if try_again.lower() == 'n':
            break

    input('\nPress Enter to exit.')

if __name__ == '__main__':
    main()