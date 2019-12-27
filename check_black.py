from PIL import Image
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import csv
"""
img = Image.open("probe.jpg")
img = img.convert("RGBA")
datas = img.getdata()
"test commit"
newData = []
for item in datas:
    print(str(item[0]) + " "  + str(item[1]) + " "  + str(item[2]))
    if not item[0] == 0 and item[1] == 0 and item[2] == 0:
        print("not black: "  + str(item[0]) + " "  + str(item[1]) + " "  + str(item[2]) + " " )
"""
def main():
    rows = ['dice', 'FP', 'TP']
    columns = ('bspline', 'rigid')
    cell_text = [[2, 3],
                 [5, 6],
                 [5, 9]]
    fig, ax = plt.subplots()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    x = PrettyTable()
    x.field_names = ["registration", "dice", "true negative", "false positive"]
    x.add_row(["bspline", 4, 5, 5])
    x.add_row(["rigid", 3, 7, 5])
    x_string = x.get_string()
    print(x)
    with open('test.txt','w') as file:
        file.write(x_string)
    
if __name__ == '__main__':
    main()