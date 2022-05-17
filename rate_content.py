import random
from time import sleep
import tkinter as tk
import json

HEIGHT = 800
WIDTH = 1000

def generate_random_activity():
    activity_list = ['yoga', 'swimming', 'biking']
    length = len(activity_list)
    random_activity = activity_list[random.randint(0, length-1)]
    return random_activity
    
def send_request():
    activity = generate_random_activity()
    with open('activity_request.txt', 'r+') as f:
        # Clear the file content and move to the beinning of the file             
        f.truncate(0)
        f.seek(0)            
        f.write(activity)    

def get_content(): 
    send_request()
    sleep(0.5)   
    print("hello")
    rate_label['text'] = '0'
    
    with open('activity_data.txt', "r+") as f:
        content_json = json.load(f)
        
        # Clear the file content and move to the beinning of the file             
        f.truncate(0)  
    
    print(content_json)
    print(type(content_json))
    save_content(content_json)
       
    title = content_json['activity']
    content = content_json['content']    
  
    output = tk.Text(frame, width = 75, height = 60, bg = "#FCFBF4", font="none 12 bold")
    output.place(relwidth= 1, relheight=1)
    output.insert(tk.END, title)
    output.insert(tk.END, "\n\n")
    output.insert(tk.END, content)    
    
            
def save_content(data):
    content_file = 'content.json'
    
    # Write json file
    with open(content_file, "w") as file:
        json.dump(data, file, indent = 4 )
    
            
def get_score(rate):
    with open('content.json') as f:
        data = json.load(f)
        
    content_json = data
    current_voted = content_json["voted"]
    current_score = content_json["score"]
    vote_times = current_voted + 1
    score = current_score + rate     
    final_score = "{:.2f}".format(score/vote_times)
    
    #Update UI label
    rate_label['text'] = final_score
    
    #Update content record
    content_json["voted"] = vote_times
    content_json["score"] = float(score)
    
    a_file = open("content.json", "w")
    json.dump(content_json, a_file, indent = 4)
    a_file.close()


#----------UI Portion----------

root = tk.Tk()

canvas = tk.Canvas(root, height= HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg= "#FCFBF4", bd= 5)
frame.place(relheight=0.9, relwidth= 0.9, relx= 0.02, rely = 0.05)

button_get_content = tk.Button(root, text = " Get\nContent ", bg = "#e2eaf2", font=40, command=get_content)
button_get_content.place(relx = 0.92, rely = 0.02, relwidth= 0.08, relheight=0.1)

rate_label_title=tk.Label(root, text = 'Rates:', bg = "#e2eaf2", font=40)
rate_label_title.place(relx = 0.92, rely = 0.15, relwidth= 0.08, relheight=0.1)
rate_label=tk.Label(root, text = '0', bg = "#e2eaf2", font=40)
rate_label.place(relx = 0.92, rely = 0.22, relwidth= 0.08, relheight=0.1)

button_up2 = tk.Button(root, text = " Rate up 2 ", bg = "#ffbf00", command=lambda: get_score(2))
button_up2.place(relx = 0.25, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up1 = tk.Button(root, text = " Rate up 1 ", bg = "#ffbf00", command=lambda: get_score(1))
button_up1.place(relx = 0.38, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up2 = tk.Button(root, text = " Rate down 2 ", bg = "#ffbf00", command=lambda: get_score(-2))
button_up2.place(relx = 0.65, rely = 0.9, relwidth= 0.1, relheight=0.1)

button_up1 = tk.Button(root, text = " Rate down 1 ", bg = "#ffbf00", command=lambda: get_score(-1))
button_up1.place(relx = 0.78, rely = 0.9, relwidth= 0.1, relheight=0.1)

root.mainloop()

