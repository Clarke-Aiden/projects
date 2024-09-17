#aiden Clarke
#12/10/23
#tkinter gui on dad joke 
#imports
import requests
import tkinter as tk
#functions
def get_r_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['joke']
    else:
        return "Failed to fetch dad joke"
#new funtion for tkinter
def show_joke():
    joke_text.set(get_r_joke())

def main():
    jokenumber = 5

    for n in range(jokenumber):
        joke = get_r_joke()
        print("DAD JOKE NUMBER ", n + 1, " IS \n", joke)

# Tkinter GUI
root = tk.Tk()
root.title("Dad Joke Generator")
root.title("Dad Joke Generator")

# Label to display the joke
joke_text = tk.StringVar()
joke_label = tk.Label(root, textvariable=joke_text, wraplength=400, font=('Helvetica', 20))
joke_label.pack(pady=20)

# Button to get a new joke                             v creates next joke 
get_joke_button = tk.Button(root, text="Get Joke", command=show_joke)
get_joke_button.pack()

# Run the Tkinter event loop
root.mainloop()

