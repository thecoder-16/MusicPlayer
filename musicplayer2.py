from tkinter import *
import pygame
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.title('Music Player')

root.geometry('400x556')

# Pygame Mixer
pygame.mixer.init()

# Functioning of main music window

def ready():
    root = tk.Toplevel()
    root.title('Music Player')

    root.geometry('500x300')
    global loops
    loops = 0

    def repeat_once():
        global loops
        loops = 2

    def repeat():
        global loops
        loops = -1

    # Add song function

    def add_song():
        songs = filedialog.askopenfilenames(initialdir='Downloads/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))

        # removing directory name and extension
        for song in songs:

            lst = list(song)

            lst1 = lst[25:]
            k = ' '.join([str(elem) for elem in lst1])
            print(k)
            song_box.insert(END, song)

    # Playing sound

    def play():
        song = song_box.get(ACTIVE)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops)

    # Stop Song
    def stop():
        pygame.mixer.music.stop()
        song_box.selection_clear(ACTIVE)
    # Global Pause
    global paused

    paused = False

    # Pause & Unpause

    def pause(is_paused):
       global paused
       paused = is_paused

       if paused:
           pygame.mixer.music.unpause()
           paused = False
       else:
           pygame.mixer.music.pause()
           paused = True

    # Next Song

    def next():
        nxt = song_box.curselection()
        nxt = nxt[0] + 1
        song = song_box.get(nxt)


        if (song == '') == False:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops)
            song_box.selection_clear(0, END)
            song_box.activate(nxt)
            song_box.selection_set(nxt, last=None)
        elif (song == '') == True:
            nxt = song_box.curselection()

            nxt = nxt[0] - (song_box.size()-1)

            song = song_box.get(nxt)
            if (song == '') == False:
                pygame.mixer.music.load(song)

                pygame.mixer.music.play(loops)
                song_box.selection_clear(0, END)
                song_box.activate(nxt)
                song_box.selection_set(nxt, last=None)

    # Deleting a song from the playlist

    def del_song():
        song_box.delete(ANCHOR)
        pygame.mixer.music.stop()

    # Deleting all songs from the playlist

    def del_all_songs():
        song_box.delete(0, END)
        pygame.mixer.music.stop()

    # Back to song

    def rev():
        rev = song_box.curselection()
        rev = rev[0] - 1
        if rev >= 0:
            song = song_box.get(rev)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops)
            song_box.selection_clear(0, END)
            song_box.activate(rev)
            song_box.selection_set(rev, last=None)

    # creating song window

    song_box = Listbox(root, bg='black', fg="white", width=60)
    song_box.pack(pady=20)

    # control buttons images

    back_img = tk.PhotoImage(file=r'Buttons_img/prev1.png')
    forward_img = tk.PhotoImage(file=r'Buttons_img/skip1.png')
    play_img = tk.PhotoImage(file=r'Buttons_img/play10.png')
    pause_img = tk.PhotoImage(file=r'Buttons_img/pause3.png')
    stop_img = tk.PhotoImage(file=r'Buttons_img/stop1.png')

    # Create control frames
    frame = Frame(root)
    frame.pack()

    # button forming
    back = Button(frame, image=back_img, borderwidth=0, command=rev)
    forward = Button(frame, image=forward_img, borderwidth=0, command=next)
    play_btn = Button(frame, image=play_img, borderwidth=0, command=play)
    pause_btn = Button(frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
    stop_btn = Button(frame, image=stop_img, borderwidth=0, command=stop)

    # Setting of buttons
    back.grid(row=0, column=0, padx=10)
    forward.grid(row=0, column=1, padx=10)
    play_btn.grid(row=0, column=2, padx=10)
    pause_btn.grid(row=0, column=3, padx=10)
    stop_btn.grid(row=0, column=4,  padx=10)

    # Creating Menu
    menu = Menu(root)
    root.config(menu=menu)

    # Add add song menu
    add_song_menu = Menu(menu)
    menu.add_cascade(label="Add songs", menu=add_song_menu)

    # Adding songs
    add_song_menu.add_command(label="Add one song to playlist", command=add_song)

    # Creating Delete Songs Menu
    del_song_menu = Menu(menu)
    menu.add_cascade(label="Remove Songs", menu=del_song_menu)

    # Creating commands for removing songs from the playlist
    del_song_menu.add_command(label="Remove a song", command=del_song)
    del_song_menu.add_command(label="Remove all songs", command=del_all_songs)

    # Creating Repeat song menu
    repeat_song = Menu(menu)
    menu.add_cascade(label="Repeat song", menu=repeat_song)

    # Creating commands for repeat
    repeat_song.add_command(label='Repeat song once', command=repeat_once)
    repeat_song.add_command(label='Repeat song forever', command=repeat)
    root.mainloop()

# Commands for startup window
canvas = Canvas(root, width = 400, height = 556)
canvas.pack()
bg_image = PhotoImage(file=r'Buttons_img\1894988.png')

# Adding image to startup window
canvas.create_image(5, 10, anchor=NW, image=bg_image)
canvas.create_text(200, 100, fill="Red", font="Times 20 ", text="WELCOME TO MUSIC PLAYER")

# Adding ready to play button
button1 = Button(text="Ready to Play", command=ready, anchor=W)
button1. configure(width=10, activebackground="#FFFF00", relief=FLAT)
button1_window = canvas. create_window(280, 450, anchor=NW, window=button1)


root.mainloop()
