import csv

import matplotlib.pyplot as plt


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


def get_data_csv(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        headers = next(csv_reader, None)
        dictionary = {}
        for h in headers:
            dictionary[h] = []

        for row in csv_reader:
            for h, v in zip(headers, row):
                dictionary[h].append(float(v))

    dict_keys = getList(dictionary)
    return headers, dictionary, dict_keys



def main():
    headers_no_probe, dict_no_probe, dict_no_probe_keys = get_data_csv("metrics_probe.csv")
    headers_probe, dict_probe, dict_probe_keys = get_data_csv("metrics.csv")

    for i in range(1, len(headers_no_probe) - 1, 2):
        fig = plt.figure()
        plt.tight_layout()
        ax = plt.subplot(111)
        # no_probe
        ax.plot(dict_no_probe.get(dict_no_probe_keys[0]), dict_no_probe.get(dict_no_probe_keys[i]), "-b",
                 label="training no probe")
        ax.plot(dict_no_probe.get(dict_no_probe_keys[0]), dict_no_probe.get(dict_no_probe_keys[i + 1]), "-r",
                 label="validatie no probe")
        # probe
        ax.plot(dict_probe.get(dict_probe_keys[0]), dict_probe.get(dict_probe_keys[i]), "-y",
                 label="training with probe")
        ax.plot(dict_probe.get(dict_probe_keys[0]), dict_probe.get(dict_probe_keys[i + 1]), "-m",
                 label="validatie with probe")

        #custom plot
        """
        chartBox = ax.get_position()        
        ax.set_position([chartBox.x0, chartBox.y0, chartBox.width * 0.6, chartBox.height])
        ax.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)
        """
        ax.legend(loc='best')
        plt.xlabel(dict_no_probe_keys[0])
        plt.title(headers_no_probe[i].split('_')[0])
        fig.savefig("./plots/" + headers_no_probe[i].split('_')[0] + ".png", dpi=fig.dpi)


if __name__ == "__main__":
    main()
