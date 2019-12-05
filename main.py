import os
import argparse

def overlay(background_path, foreground_path, result_path):
    os.system(
        'magick composite -blend 25 ' + foreground_path + ' ' + background_path + ' ' + result_path)

def gif(background_path, foreground_path, result_path):
    os.system(
        'magick convert -loop 0 -delay 100 ' + background_path + ' ' +  foreground_path + ' ' + result_path)

def main():
    """
        Need 3 dirs:
        - background
        - foreground
        - results
        """
    parser = argparse.ArgumentParser()

    parser.add_argument('--gif_mode', action='store_true', help='create gif, false is overlay')
    FLAGS, unparsed = parser.parse_known_args()

    file_list = os.listdir('./foreground')

    assert len(os.listdir('./foreground')) == len(
        os.listdir('./background')), "foreground and background dir contains not a equal number of files"

    for file in file_list:
        name_parts = file.split('.')
        background_path = './background/' + name_parts[0] + '.png'
        foreground_path = './foreground/' + name_parts[0] + '.bmp'

        if not FLAGS.gif_mode:
            result_path = './results/' + name_parts[0] + '.png'
            overlay(background_path, foreground_path, result_path)
            print('Overlay ' + name_parts[0] + ' to ' + result_path)
        else:
            result_path = './results/' + name_parts[0] + '.gif'
            gif(background_path, foreground_path, result_path)
            print('Gif ' + name_parts[0] + ' to ' + result_path)

if __name__ == "__main__":
    main()


