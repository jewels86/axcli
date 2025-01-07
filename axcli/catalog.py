import click
import httpx
import json

CATALOG = "https://raw.githubusercontent.com/jewels86/Axinite/refs/heads/main/templates/catalog.txt"

@click.command("catalog")
def catalog():
    systems = {}
    r_catalog = httpx.get(CATALOG)
    content = r_catalog.text
    for line in content.splitlines():
        r = httpx.get(line)
        system = json.loads(r.text)
        systems[system["name"]] = system
    
    