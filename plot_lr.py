import csv

import matplotlib.pyplot as plt
import numpy as np


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list


def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / N


def get_data_csv(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        headers = next(csv_reader, None)
        dictionary = {}
        for h in headers:
            dictionary[h] = []

        for row in csv_reader:
            for h, v in zip(headers, row):
                dictionary[h].append(np.float(v))

    dict_keys = getList(dictionary)
    return headers, dictionary, dict_keys


def main():
    headers_no_probe, dict_no_probe, dict_no_probe_keys = get_data_csv("run-training-probe-none-exponential-tag-Losses_loss.csv")
    headers_probe, dict_probe, dict_probe_keys = get_data_csv("lr_with_probe.csv")

    for i in range(2, len(headers_no_probe), 2):
        fig = plt.figure()
        plt.tight_layout()
        ax = plt.subplot(111)


        # no_probe
        xdata = dict_no_probe.get(dict_no_probe_keys[1])
        xdata = running_mean(xdata, 400)

        plt.plot(xdata, running_mean(dict_no_probe.get(dict_no_probe_keys[i]), 400), color='orange',
                label="Zonder FCD data")
        """
        # probe
        xdata = dict_probe.get(dict_probe_keys[1])
        xdata = running_mean(xdata, 120)
        plt.plot(xdata, running_mean(dict_probe.get(dict_probe_keys[i]), 120), "-b",
                label="Met FCD data")
"""
        # custom plot
        """
        chartBox = ax.get_position()        
        ax.set_position([chartBox.x0, chartBox.y0, chartBox.width * 0.6, chartBox.height])
        ax.legend(loc='upper center', bbox_to_anchor=(1.0, 0.8), shadow=True, ncol=1)
        """
        plt.yscale("log")
        plt.legend(loc='best')
        plt.ylabel("Loss (log schaal)")
        plt.xlabel("Training stap")
        plt.title("Bepalen leersnelheid (1)")
        fig.savefig("./plots/" + "Loss_lr_test" + ".png", dpi=fig.dpi)


if __name__ == "__main__":
    main()
