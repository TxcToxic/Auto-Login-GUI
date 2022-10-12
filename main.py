import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import webbrowser
import requests


def ipCheck():
    try:
        ip = requests.get("https://ipinfo.io/json").json()["ip"]
    except:
        return False
    args = ip.split(".")
    if not f"{args[0]}.{args[1]}" == "0.0":
        return False
    else:
        return True


def proxmoxLogin():
    username = "******"
    password = "******"
    url = "http://proxmox.gtav-online-community.com/"
    driver = webdriver.Chrome("./bin/chromedriver.exe")
    driver.set_window_size(height=1000, width=1500)
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()
    time.sleep(.5)
    driver.find_element(By.XPATH, '//*[@id="textfield-1062-inputEl"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="textfield-1063-inputEl"]').send_keys(password)
    time.sleep(.1)
    driver.find_element(By.XPATH, '//*[@id="button-1067-btnInnerEl"]').click()
    time.sleep(.2)
    driver.find_element(By.XPATH, '//*[@id="button-1005-btnEl"]').click()
    messagebox.showinfo(title="IMPORTANT!", message="If you close this, the browser window will close automatically!")


def gocWebsiteOpen():
    webbrowser.open("https://gtav-online-community.com/", new=True)


def gocDbOpen():
    webbrowser.open("http://db.gtav-online-community.com/", new=True)


root = tk.Tk()
root.title("SRV - Login || -TOXIC-#1835")
root.minsize(height=300, width=350)
root.maxsize(height=500, width=550)
root.configure(bg="#000000")

tk.Label(root, text="SRV - Login", font=("Berlin Sans FB", 25), bg="#000000", fg="#5c009e").pack()
tk.Label(root, text='"SRV - Login" Tool by -TOXIC-#1835', font=("Arial", 6),
         fg="#ff0000", bg="#000000").pack(side="bottom")
if not ipCheck():
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    time.sleep(1)
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    time.sleep(1)
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    time.sleep(1)
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    time.sleep(1)
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    time.sleep(1)
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    time.sleep(1)
    tk.Label(root, text="OPTIONS ONLY FOR THE OWNER!", fg="#ff0000", bg="#000000", font=("Berlin Sans FB", 20)).pack()
    while True:
        messagebox.showerror(title="FATAL ERROR!", message="This tool is only for the owner of this tool!\n\n"
                                                           "Error 1")
#  tk.Label(root, text=f'Logged in with: {ip}', font=("Arial", 6),
#           fg="#ff0000", bg="#000000").pack(side="bottom")
tk.Button(root, text="Login -> Proxmox", borderwidth=0, font=("Berlin Sans FB", 12, "underline"), bg="#000000",
          fg="#5c009e", command=proxmoxLogin).pack()
tk.Button(root, text="Open -> GOC Website", borderwidth=0, font=("Berlin Sans FB", 12, "underline"), bg="#000000",
          fg="#5c009e", command=gocWebsiteOpen).pack()
tk.Button(root, text="Open -> GOC Database", borderwidth=0, font=("Berlin Sans FB", 12, "underline"), bg="#000000",
          fg="#5c009e", command=gocDbOpen).pack()

root.mainloop()
