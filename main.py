import requests
from rich.console import Console
import random
import string
import threading

console = Console()

def isValid(id):
    r = requests.get(f"https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={id}",)
    return all(code not in r.text for code in ["Not Found", "Bad Request"])

def generate():
    while True:
        id = "".join(random.choices(string.ascii_letters + string.digits + "_" + "-", k=11))
        if isValid(id):
            console.print(f"[green]Found: [magenta]{id}[/][/]")

for i in range(100):
    thread = threading.Thread(target=generate)
    thread.start()
