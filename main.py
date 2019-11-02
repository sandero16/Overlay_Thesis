import os


def overlay(background_path, foreground_path, result_path):
    os.system(
        'magick composite -blend 30 ' + foreground_path + ' ' + background_path + ' ' + result_path)

def main():
    """
        Need 3 dirs:
        - background
        - foreground
        - results
        """
    file_list = os.listdir('./foreground')

    assert len(os.listdir('./foreground')) == len(
        os.listdir('./background')), "foreground and background dir contains not a equal number of files"

    for file in file_list:
        name_parts = file.split('.')
        background_path = './background/' + name_parts[0] + '.png'
        foreground_path = './foreground/' + name_parts[0] + '.bmp'
        result_path = './results/' + name_parts[0] + '.png'
        overlay(background_path, foreground_path, result_path)
        print('Written ' + name_parts[0] + ' to ' + result_path)

if __name__ == "__main__":
    main()


