import os


def overlay(background_path, foreground_path, result_path):
    os.system(
        'magick composite -blend 30 ' + foreground_path + ' ' + background_path + ' ' + result_path)


if __name__ == "__main__":
    """
    Need 3 dirs:
    - background
    - foreground
    - results
    """
    file_list = os.listdir('./foreground')
    foreground_number_files = len(os.listdir('./foreground'))
    background_number_files = len(os.listdir('./background'))

    assert foreground_number_files == background_number_files, "foreground and background dir contains not a equal files"

    for file in file_list:
        name_parts = file.split('.')
        background_path = './background/' + name_parts[0] + '.png'
        foreground_path = './foreground/' + name_parts[0] + '.bmp'
        result_path = './results/' + name_parts[0] + '.png'
        overlay(background_path, foreground_path, result_path)
        print('Written '+ name_parts[0] +' to '+ result_path)

