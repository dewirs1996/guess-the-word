import random

animals = ('Albatross','Alligator','Ant','Anteater','Armadillo','Baboon','Badger','Bat','Bear','Beaver','Beetle','Bird','Boar','Buffalo','Bull','Camel','Cat','Caterpillar','Chameleon','Cheetah','Chicken','Chimpanzee','Chipmunk','Cow','Crab','Crocodile','Deer','Dodo','Dog','Dolphin','Donkey','Duck','Eagle','Eel','Elephant','Emu','Ferret','Fish','Flamingo','Fox','Frog','Gecko','Gerbil','Giraffe','Goat','Goose','Gorilla','Greyhound','Guinea Pig','Hamster','Hare','Hedgehog','Hippopotamus','Horse','Hyena','Ibis','Iguana','Insect','Jaguar','Jellyfish','Kangaroo','Kingfisher','Kiwi','Koala','Komodo Dragon','Leopard','Lion','Lizard','Llama','Lobster','Lynx','Meerkat','Mole','Mongoose','Monkey','Moose','Mouse','Newt','Octopus','Ostrich','Otter','Owl','Panther','Parrot','Peacock','Pelican','Penguin','Pheasant','Pig','Polar Bear','Puffin','Puma','Quail','Rabbit','Raccoon','Rat','Reindeer','Rhinoceros','Seal','Shark','Sheep','Skunk','Snail','Snake','Squirrel','Swan','Tiger','Tortoise','Turkey','Turtle','Walrus','Whale','Wolf','Wombat','Zebra')
asia = ('Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus','East Timor','Egypt','Georgia','Hong Kong','India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia','Myanmar','Nepal','North Korea','Oman','Pakistan','Palestine','Philippines','Qatar','Russia','Saudi Arabia','Singapore','South Korea','Sri Lanka','Syria','Taiwan','Tajikistan','Thailand','Turkey','Turkmenistan','United Arab Emirates','Uzbekistan','Vietnam','Yemen')
city = ('Ambon','Balikpapan','Banda Aceh','Bandar Lampung','Bandung','Banjar','Banjarbaru','Banjarmasin','Batam','Batu','Baubau','Bekasi','Bengkulu','Bima','Binjai','Bitung','Blitar','Bogor','Bontang','Bukittinggi','Central Jakarta','Cilegon','Cimahi','Cirebon','Denpasar','Depok','Dumai','East Jakarta','Gorontalo','Gunungsitoli','Jambi','Jayapura','Kediri','Kendari','Kotamobagu','Kupang','Langsa','Lhokseumawe','Lubuklinggau','Madiun','Magelang','Makassar','Malang','Manado','Mataram','Medan','Metro','Mojokerto','North Jakarta','Padang Panjang','Padang Sidempuan','Padang','Pagar Alam','Palangkaraya','Palembang','Palopo','Palu','Pangkalpinang','Parepare','Pariaman','Pasuruan','Payakumbuh','Pekalongan','Pekanbaru','Pematangsiantar','Pontianak','Prabumulih','Probolinggo','Sabang','Salatiga','Samarinda','Sawahlunto','Semarang','Serang','Sibolga','Singkawang','Solok','Sorong','South Jakarta','South Tangerang','Subulussalam','Sukabumi','Sungai Penuh','Surabaya','Surakarta','Tangerang','Tanjungbalai','Tanjungpinang','Tarakan','Tasikmalaya','Tebing Tinggi','Tegal','Ternate','Tidore','Tomohon','Tual','West Jakarta','Yogyakarta')
fruits = ('Acai','Ackee','Apples','Apricots','Avocado','Bananas','Bilberries','Blackberries','Blueberries','Boysenberries','Bread fruit','Cantalope','Cherimoya','Cherries','Cranberries','Cucumbers','Currants','Dates','Durian','Eggplant','Elderberries','Figs','Gooseberries','Grapefruit','Grapes','Guava','Honeydew melons','Huckleberries','Ita Palm','Jujubes','Kiwis','Kumquat','Lemons','Limes','Lychees','Mangos','Mangosteen','Mulberries','Muskmelon','Nectarines','Olives','Oranges','Papaya','Passion fruit','Peaches','Pears','Peppers','Persimmon','Pineapple','Plums','Pluot','Pomegranate','Quince','Rambuton','Raspberries','Rose Apple','Sapadilla','Starfruit','Strawberries','Tamarind','Tangelo','Tangerines','Tomatoes','Ugli fruit','Watermelons','Zucchini')

def start_game():
    print(" ======================")
    print("|   GUESS THE WORD !   | ")
    print(" ======================")
    print("\n")

def choose_category():
    print("| Category :")
    print("  1. Animals")
    print("  2. Fruits")
    print("  3. Country in Asia")
    print("  4. City in Indonesia")

    category = input("| Choose the category : ")
    if (category == "1"):
        return animals
    elif (category == "2"):
        return fruits
    elif (category == "3"):
        return asia
    elif (category == "4"):
        return city
    else:
        print(" \n   Oops! It's not an available category... \n   We'll choose category 4 for you! Lets play! ")
        return city

def choose_level():
    print("\n")
    print("| Level :")
    print("  1. Easy")
    print("  2. Normal")
    print("  3. Hard")

    level = input("| Choose the level : ")
    if (level == "1"):
        return 15
    elif (level == "2"):
        return 10
    elif (level == "3"):
        return 5
    else:
        print(" \n   Oops! It's not an available level... \n   Let's just make it very very easy then!")
        return 20

def play_again():
    again = input("   Want to play again? (y/n) : ")
    if again == "y":
        print("\n \n")
        print("**************************************** \n \n")
        guess_the_word()
    else:
        input("\n   Thanks for playing! ")
        exit()

def guess_the_word():
    start_game()
    master = random.choice(choose_category())
    chance = choose_level()

    word = list(master.lower())
    length = len(word)
    right = list("_" * length)
    print("\n")
    print(right)

    check = False

    while (chance >= 1):
        guess = input(" Guess a letter : ").lower()
        print("\n")

        if (guess not in master.lower()):
            chance -= 1
            print("   Oops! " + guess.upper() + " is not in the word.\n   " + str(chance) + " chance/s lefted!")
            print("\n")

        for letter in word:
            if letter == guess:
                check = True
                index = word.index(guess)
                right[index] = guess
                word[index] = "_"

        if (check == True):
            print("   Good! " + guess.upper() + " is in the word.")
            print("\n")
            check = False

        if (chance >= 1):
            print(right)

        if list(master.lower()) == right:
            print(" Correct! The word is " + master.upper() + "!")
            print("\n")
            play_again()


    if (chance == 0):
        print(" Too bad! The word is " + master.upper() + "!")
        print("\n")
        print(" ======================")
        print("|      GAME OVER!      | ")
        print(" ======================")
        print("\n")
        play_again()

guess_the_word()
