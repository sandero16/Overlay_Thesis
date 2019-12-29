import argparse
import datetime
import os

import ruamel.yaml


def add_date_to_all_files_in_folder():
    """
    Add string to all files of a given folder
    :param path to folder
    """
    for filename in os.listdir(p.input_directory):  # filename is a string
        if filename.endswith(".yaml"):  # notice the indent
            path = p.input_directory + "\\" + filename

            # Read YAML file
            with open(path) as stream:
                yaml = ruamel.yaml.YAML()
                data = yaml.load(stream)
                """
                data["date_range_from"] = datetime.date(2018, 10, 15)
                data["date_range_to"] = datetime.date(2019, 10, 15)
                """
                data["probe_layer"] = 'averagedtrf'
                
            # Write YAML file
            with open(path, "w") as stream:
                 yaml.dump(data, stream, default_flow_style=None, sort_keys=False)
                #yaml.dump(data, stream)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' Add string to all files of a given folder, use anaconda: min_roadtracer_inference')
    parser.add_argument("--input_directory", type=str, required=True)

    p = parser.parse_args()

    add_date_to_all_files_in_folder()
