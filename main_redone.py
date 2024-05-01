import random
import customtkinter as ctk
def main():
    ctk.set_default_color_theme('dark-blue')
    ctk.set_appearance_mode('dark')
    Root = ctk.CTk()
    Root.geometry("700x130")
    Root.title("Random number generator")
    my_font = ctk.CTkFont(family="", size=40)
    # main_frame = ctk.CTkFrame(master=Root, width=500, height=500).pack(fill="both",pady=10,padx=10)
    u=0
    course_label = ctk.CTkLabel(master=Root, text="random numbers", font=my_font)
    course_label.pack(pady=12,padx=10)
    def increment():
        randomlist = random.sample(range(1, 100), 10)
        course_label.configure(text = randomlist)
    button1= ctk.CTkButton(master=Root, text="generate", command=increment).pack(pady=12,padx=10)

    Root.mainloop()
if __name__ == "__main__":
    main()