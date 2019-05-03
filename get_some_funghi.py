import requests
from lxml import html

urls = ["http://www.mushroom.world/mushrooms/edible?page=0",
        "http://www.mushroom.world/mushrooms/edible?page=1",
        "http://www.mushroom.world/mushrooms/edible?page=2",
        "http://www.mushroom.world/mushrooms/edible?page=3",
        "http://www.mushroom.world/mushrooms/edible?page=4",
        "http://www.mushroom.world/mushrooms/edible?page=5",
        "http://www.mushroom.world/mushrooms/edible?page=6",
        "http://www.mushroom.world/mushrooms/edible?page=7",
        "http://www.mushroom.world/mushrooms/inedible?page=0",
        "http://www.mushroom.world/mushrooms/inedible?page=1",
        "http://www.mushroom.world/mushrooms/inedible?page=2",
        "http://www.mushroom.world/mushrooms/inedible?page=3",
        "http://www.mushroom.world/mushrooms/inedible?page=4",
        "http://www.mushroom.world/mushrooms/inedible?page=5",
        "http://www.mushroom.world/mushrooms/inedible?page=6",
        "http://www.mushroom.world/mushrooms/inedible?page=7",
        "http://www.mushroom.world/mushrooms/poisonous?page=0",
        "http://www.mushroom.world/mushrooms/poisonous?page=1",
        "http://www.mushroom.world/mushrooms/poisonous?page=2",
        "http://www.mushroom.world/mushrooms/poisonous?page=3"]

for url in urls:
    page = requests.get(url)
    tree = html.fromstring(page.content)
    funghi_images_list = tree.xpath("//a[@class='swipebox']")
    count = 0
    name = ""
    for funghi_image in funghi_images_list:
        if "inedible" in url:
            category = "i"
        elif "poisonous" in url:
            category = "p"
        else:
            category = "e"

        if funghi_image.get("title") == name:
            count += 1
        else:
            count = 0

        funghi_image_url = "http://www.mushroom.world" + funghi_image.get("href")[3:]
        img_data = requests.get(funghi_image_url).content
        name = funghi_image.get("title")
        filename = '{}_{}_{}.jpg'.format(category, name ,count)
        print(filename)

        with open(filename, 'wb') as handler:
            handler.write(img_data)
