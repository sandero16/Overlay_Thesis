from PIL import Image

def iterate(name, color):
    img = Image.open(name)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            #constract if statement for your purpose
            if (color == "new"):
                newData.append((34, 255, 0, 1000))
            else:
                newData.append((255, 0, 0, 1000))
    img.putdata(newData)

    newName = name
    #save new image
    img.save(newName, "PNG")
    return newName