import tkinter as tk
from tkinter import filedialog, simpledialog
from tkinter.constants import *
from PIL import ImageTk, Image
import random
import requests

root = tk.Tk()
root.geometry("750x600")
root.resizable(width=False, height=False)
root.title("W.B.I.P")
head = tk.Label(root, text="W.B.I.P", font=15, background="orange")
head.pack(pady=10)
bucks = 0
# Image Processing using pillow
but1_image = "images/gallery.png"
but2_image = "images/ruppee.png"
but3_image = "images/wordle.png"
but4_image = "images/poke_ball.png"

image1 = Image.open(but1_image)
image2 = Image.open(but2_image)
image3 = Image.open(but3_image)
image4 = Image.open(but4_image)

image1 = image1.resize((70, 70))
image2 = image2.resize((70, 70))
image3 = image3.resize((70, 70))
image4 = image4.resize((70, 70))

img1_tk = ImageTk.PhotoImage(image1)
img2_tk = ImageTk.PhotoImage(image2)
img3_tk = ImageTk.PhotoImage(image3)
img4_tk = ImageTk.PhotoImage(image4)


def func_b1():

    def open_file_dialog(w_entry, h_entry):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Image files", "*.png"), ("Image files", "*.jpg")])
        if file_path:
            process_file(file_path, w_entry, h_entry)

    def process_file(file_path, width_entry, height_entry):
        try:
            with Image.open(file_path) as img:
                imgs = img.resize((int(width_entry.get()), int(height_entry.get())))
                def img_tk():
                    imgs.show()
            
            master1 = tk.Frame(new_frame)
            master1.pack()
            # master1 = tk.Frame(root)
            label = tk.Label(master1,text="Image Loaded Successfully",font=5)
            label.pack()
            btu = tk.Button(master1,text="DOWNLOAD IMAGE",command=img_tk)
            btu.pack()
            master1.mainloop()
        except Exception as e:
            pass

    new_frame = tk.Frame(root)
    new_frame.place(x=0, y=0, height=750, width=750)

    head = tk.Label(new_frame, text="Image Compressor", font=15, background="orange")
    head.pack(pady=20)

    labelling = tk.Label(new_frame, text="Enter Height:")
    labelling.pack()

    height_entry = tk.Entry(new_frame, width=5, font=6)
    height_entry.pack()

    labelling2 = tk.Label(new_frame, text="Enter Width:")
    labelling2.pack()

    width_entry = tk.Entry(new_frame, width=5, font=6)
    width_entry.pack()

    open_button = tk.Button(new_frame, text="Select image",activebackground="green", activeforeground="white", command=lambda: open_file_dialog(width_entry, height_entry))
    open_button.pack(padx=20, pady=20)
    back_button = tk.Button(new_frame,text="<--", command=new_frame.destroy, activebackground="red", activeforeground="white")
    back_button.place(x=0,y=0)

def func_b2():
    bank = tk.Tk()
    bank.geometry("500x500")
    end = tk.Button(bank, text="<--", command=bank.destroy, activebackground="red", activeforeground="white")
    end.place(x=0, y=0)
    head = tk.Label(bank, text="Bank", font=15, background="orange")
    head.pack(pady=10)

    class Bank:
        def withdraw(self):
            w_frame = tk.Frame(bank)
            w_frame.place(x=0,y=0, width=500, height=500)
            w_label = tk.Label(w_frame, text="Enter Withdrawl Amount")
            w_label.pack()
            amount = tk.Entry(w_frame, width=10)
            amount.pack()

            def submit():        
                global bucks
                amt = int(amount.get())
                if bucks <= 0:
                    tk.Label(w_frame, text="Not enough balance to withdraw").pack()
                else:
                    bucks -= int(amt)
                    w_success = tk.Label(w_frame, text="Withdrawl Succesful")
                    w_success.pack()
                with open("logs.txt", "a") as logs:
                    logs.write(f">> Withdrawn: {str(amt)}\n")
                    logs.flush()
                return int(amt)        
            
            button_submit = tk.Button(w_frame, text="Withdraw", command=submit)
            button_submit.pack()
            back_button = tk.Button(w_frame,text="<--", command=w_frame.destroy, activebackground="red", activeforeground="white")
            back_button.place(x=0,y=0)
        
        def deposit(self):
            d_frame = tk.Frame(bank)
            d_frame.place(x=0,y=0, width=500, height=500)
            d_label = tk.Label(d_frame, text="Enter Amount To Deposit")
            d_label.pack()
            amount = tk.Entry(d_frame, width=10)
            amount.pack()

            def submit():
                global bucks
                amt = int(amount.get())
                bucks += amt
                with open("logs.txt", "a") as logs:
                    logs.write(f">> Deposited: {str(amt)}\n")
                    logs.flush()
                d_success = tk.Label(d_frame, text="Deposit Succesful")
                d_success.pack()
                return amt

            button_submit = tk.Button(d_frame, text="Deposit", command=submit)
            button_submit.pack()
            back_button = tk.Button(d_frame,text="<--", command=d_frame.destroy, activebackground="red", activeforeground="white")
            back_button.place(x=0,y=0)

        def balance(self):
            global bucks
            b_frame = tk.Frame(bank)
            b_frame.place(x=0,y=0, width=500, height=500)

            def submit():
                with open("logs.txt", "a") as logs:
                    logs.write(f">> Checked Balance ({bucks})\n")
                    logs.flush()
                text = ""
                with open("logs.txt", "r") as logs:
                    for word in logs:
                        text += word

                t_label = tk.Label(b_frame, text=text)
                t_label.pack()

            b_label = tk.Label(b_frame, text=bucks)
            b_label.pack()
            button_submit = tk.Button(b_frame, text="View logs", command=submit)
            button_submit.pack()
            back_button = tk.Button(b_frame,text="<--", command=b_frame.destroy, activebackground="red", activeforeground="white")
            back_button.place(x=0,y=0)
            
        def options(self):
            def submit():
                option = int(choice.get())
                match(option):
                    case 1: self.withdraw()
                    case 2: self.deposit()
                    case 3: self.balance()
                    case 4: bank.destroy()
            

            choices = tk.Label(bank, text="1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit",font=10)
            choices.pack()
            choice = tk.Entry(bank, width=5)
            choice.pack()
            option = choice.get()
            # return option
            button_submit = tk.Button(bank, text="Sumbit", command=submit, activebackground="green", activeforeground="white")
            button_submit.pack()

    user1 = Bank()
    option = user1.options()
    bank.mainloop()

def func_b3():
    word = tk.Tk()
    word.title("Wordle")
    word.geometry("1000x600")
    word.resizable(width=False, height=True)
    # function which checks if the hidden word is equal to the guessed word
    def Wordle(letters, hiddenWord):
        #giving the user 6 chances
        for i in range(1, 7):
            guessedWord = simpledialog.askstring(title="wordle", prompt="Enter a 5 letter word")
            guessedLetters = list(guessedWord)
            label = tk.Label(word, text=guessedLetters)
            label.pack()
            
            match = ""
            rest = ""
            # correct position ("green" letter)
            for j in range(5):
                if letters[j] == guessedLetters[j]:
                    match = f"{guessedLetters[j]}" 
                    rest = f"{guessedLetters[j:]}"
                    m = tk.Label(word, text=match, background="Green")
                    m.pack()
                    r = tk.Label(word, text=rest, background="Grey")
                    r.pack()
            
            mismatch = ""
            # letter exists, but wrong position ("yellow" letter)
            for k in range(5):
                if guessedLetters.count(guessedLetters[k])>1:
                    break
                elif guessedLetters[k] in letters:
                    if letters[k] != guessedLetters[k]:
                        mismatch = f"{guessedLetters[k]}"
                        l = tk.Label(word, text=mismatch, background="Yellow")
                        l.pack()
            # escaping the chances loop when the word is right
            if guessedLetters == letters:
                break
        correct_word = f"the correct word is, {hiddenWord}"
        cw = tk.Label(word, text=correct_word, background="Green")
        cw.pack()
        
    #list of 5 letter words
    words = ["abide","acorn","adopt","afoul","agile","aloud","amber","ample","angry","apex","apple","audio","auger","avert","awful","bacon","badge","beard","bingo","blaze","bleak","blitz","bloom","blush","brave","brick","brisk","brood","brush","bunch","cabin","candy","cater","chaos","cheer","chime","clamp","cloak","clung","coach","coast","couch","crane","crawl","crisp","crown","crust","cubic","dandy","dealt","delta","demon","deter","dodge","drown","drift","drone","drown","dummy","dwarf","eager","eagle","early","earth","edged","eight","elite","ember","enjoy","enter","envoy","equal","equip","erase","ethic","evade","exact","exile","extra","fable","faint","fairy","false","fatal","favor","feast","fever","flock","flute","forum","frost","frown","fruit","fudge","gauge","gazer","ghost","giant","glaze","globe","glory","grain","grape","grasp","grove","guard","guilt","gulch","gushy","habit","happy","haste","hatch","haunt","health","heart","hefty","hello","hinge","honor","horde","hover","human","humor","hurry","hyena","cycle","ideal","image","incur","index","infer","input","irate","ivory","jaded","joint","jolly","juice","jumbo","junta","joust","kayak","keeps","kiosk","knack","knead","knelt","knife","laser","later","latch","laugh","leafy","leash","level","libra","lilac","liver","lobby","lunar","lunch","lyric","macro","magic","major","maple","medal","melon","merry","metal","micro","might","mirth","moist","money","motel","mouse","mower","music","naive","nanny","naval","noble","nudge","nylon","oasis","ocean","olive","onion","orbit","ounce","overt","pacer","paint","panel","piano","pilot","plaid","plaza","pluck","plush","poise","pouch","power","pride","prime","prize","probe","proud","punch","quack","query","quick","quiet","quite","quota","quote","quoth","racer","radar","radio","rally","ranch","range","raven","razor","rebel","reign","relay","renew","revel","rider","ridge","rifle","rider","rival","roast","robin","robot","rodeo","roost","royal","ruler","runes","saber","sable","saint","salsa","sandy","savor","scale","scamp","scold","scone","scout","scuba","seize","sells","sense","shade","shaft","shake","shaky","shear","shine","shock","shout","shred","silly","skate","skirt","slate","sleep","slice","slump","snack","snail","snare","snout","sober","solar","solve","sonic","space","spark","spare","speak","speed","spice","spine","spite","spray","spurx","stain","stare","stash","steer","sting","stoop","strap","straw","strip","stump","style","sugar","sweep","swift","swing","swirl","sword","syrup","table","tacky","taken","tango","taste","tease","tenor","terra","thick","thorn","three","thump","tidal","tiger","tilde","toast","token","tonic","topic","torch","tower","trace","track","trail","train","tramp","truce","trump","tulip","twist","ultra","uncle","under","unify","unite","untie","upend","upset","urban","usher","utter","vacuo","valid","valor","value","vapor","vault","vegan","velve","venom","verse","vexed","vibes","video","vivid","vocal","vodka","vogue","voice","vomit","vowel","vulva","wacky","wager","waste","watch","water","weave","weird","wheel","whisk","whizx","whole","whore","widen","width","wince","wired","witch","witty","wound","wrath","wrist","wrote","wrung","wryly","xerox","yacht","yearn","yield","yodel","young","youth","yucca","yummy","zanyx","zebra","zerox","zesty","zippy","zoned"]

    # randomizing the generation of words
    hiddenWord = random.choice(words)
    #splitting the word into individual letters using list() function
    letters = list(hiddenWord)
    #calling the function Wordle
    head = tk.Label(word, text="Wordle", font=15)
    head.pack(pady=10)
    end = tk.Button(word, text="<--",command=word.destroy, activebackground="red", activeforeground="white")
    end.place(x=0, y=0)
    Wordle(letters, hiddenWord)
    word.mainloop()

def func_b4():
    pok = tk.Tk()
    pok.title("Pokemon Battle")
    pok.geometry("500x500")
    head = tk.Label(pok, text="Pokemon Battle!", font=15, background="orange")
    head.pack(pady=10)

    def fetch_poke_details(player1, player2):    
        poke1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{player1}")
        poke1 = poke1.json()
        poke2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{player2}")
        poke2 = poke2.json()
        return [poke1, poke2]

    def view_details(pokemon):
        for i in range(0, 2):
            #Name
            detail_frame = tk.Frame(pok)
            detail_frame.pack()
            # print(f"{Fore.WHITE}Name: \t\t{Fore.GREEN}{pokemon[i]['name']}")
            name_label = tk.Label(detail_frame, text=pokemon[i]['name'])
            name_label.pack()

            #Base experience
            experiences = []
            base_experience = pokemon[i]['base_experience']
            experiences.append(base_experience)
            # print(f"{Fore.WHITE}Base experience: \t{Fore.GREEN}{base_experience}")
            exp_label = tk.Label(detail_frame, text=f"Base experience: {base_experience}")
            exp_label.pack()

            #Weight
            weights = []
            weight = pokemon[i]['weight']
            weights.append(weight)
            # print(f"{Fore.WHITE}Weight: \t{Fore.GREEN}{weight}")
            weight_label = tk.Label(detail_frame, text=f"Weight: {weight}")
            weight_label.pack()

            #Height
            heights = []
            height = pokemon[i]['height']
            heights.append(height)
            # print(f"{Fore.WHITE}Height: \t{Fore.GREEN}{height}")
            height_label = tk.Label(detail_frame, text=f"Height: {height}")
            height_label.pack()

        experiences.sort()
        # [112, 234]
        for i in range(1, -1, -1):
            if pokemon[i]['base_experience'] > pokemon[i-1]['base_experience']:
                # print(f"The winner is {pokemon[i]['name']}")
                win_label = tk.Label(detail_frame, text="The winner is "+pokemon[i]['name'], background="green")
                win_label.pack()
                break
            else:
                # print(f"The winner is {pokemon[i-1]['name']}")
                winner_label = tk.Label(detail_frame, text="The winner is "+pokemon[i-1]['name'], background="green")
                winner_label.pack()
                break

    def submit():

        def yes():
            view = view_enter.get()
        # view = input("Would you like to see the pokemon's details? [Y / N]: ")
            if view in ['Y', 'Yes', 'y', 'yes']:
                details = view_details(poke_details)
        
        frame = tk.Frame(pok)
        frame.pack()
        player1 = label_1_entry.get()
        player2 = label_2_entry.get()
        poke_details = fetch_poke_details(player1, player2)
        # print(f"Fetched {pokemon}'s details successfully.")
        view_label = tk.Label(frame, text="Are you ready for the battle? [Y / N]")
        view_label.pack()
        view_enter = tk.Entry(frame, width=10)
        view_enter.pack()
        button_yes = tk.Button(frame, text="Submit", command=yes, activebackground="green", activeforeground="white")
        button_yes.pack()

    label_1 = tk.Label(pok,text="Player 1: Enter pokemon")
    label_1.pack()
    label_1_entry = tk.Entry(pok,width=10)
    label_1_entry.pack()
    label_2 = tk.Label(pok,text="Player 2: Enter pokemon")
    label_2.pack()
    label_2_entry = tk.Entry(pok,width=10)
    label_2_entry.pack()
    fight = tk.Button(pok,text="Battle!", command=submit)
    fight.pack()
    back_button = tk.Button(pok,text="<--", command=pok.destroy, activebackground="red", activeforeground="white")
    back_button.place(x=0,y=0)

    pok.mainloop()

# Button Creation
button1 = tk.Button(root, text="Image Compressor", activebackground="green",activeforeground="white",width=110, bg='light green', image=img1_tk, compound=TOP, command=func_b1)
button1.place(relx=0.2, rely=0.2)

button2 = tk.Button(root, text="Banking", activebackground="green",activeforeground="white",width=110, bg='light green', image=img2_tk, compound=TOP, command=func_b2)
button2.place(relx=0.7, rely=0.2)

button3 = tk.Button(root, text="Worlde", activebackground="green",activeforeground="white",width=110, bg='light green', image=img3_tk, compound=TOP, command=func_b3)
button3.place(relx=0.2, rely=0.4)

button4 = tk.Button(root, text="Pokemon Game", activebackground="green",activeforeground="white", width=110, bg='light green', image=img4_tk, compound=TOP, command=func_b4)
button4.place(relx=0.7, rely=0.4)

button_Exit = tk.Button(root, width=20, height=2, text="EXIT", bg='light pink',activeforeground="white", activebackground='red', command=root.destroy)
button_Exit.place(relx=0.4, rely=0.65)

root.mainloop()
