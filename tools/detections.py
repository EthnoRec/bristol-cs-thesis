#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir, path


cities = {
    "india": "Mumbai",
    "brazil": "Belo Horizonte",
    "mexico": "Guadalajara"
}

countries = ("india", "brazil", "mexico")
genders = ("male", "female")
qualities = ("lq", "mq", "hq")

detections = "figures/results/detections"
image_size = ("2.2cm", "2.2cm")
images_n = 2


def includegraphics(image_path):
    return "\includegraphics[height=2.2cm,width=2.2cm]{"+image_path+"}"


def table_quality(attributes):
    files = listdir(path.join(*attributes))

    images = [includegraphics(path.join(*(attributes + (filename,))))
              for filename in files]
    return "\n".join(images[:images_n])+"\n"


def table_gender(attributes):
    cells = [table_quality(attributes + (quality,)) for quality in qualities]
    return "&\n".join(cells)+"\TBstrut \\\\ \n\n"


def table_country(attributes):
    rows = [table_gender(attributes + (gender,)) for gender in genders]
    rows = "\n".join(rows)

    location = "{}, {}".format(cities[attributes[-1]], attributes[-1].title())

    heading = "\midrule \\multicolumn{3}{c}{"+location
    heading += "} \TBstrut \\\\ \midrule \n"
    return heading + rows


def table(attributes):
    tcountries = [table_country(attributes + (country,))
                  for country in countries]
    return "\n".join(tcountries)


def main():
    # path
    attributes = ("figures", "results", "detections")
    print(table(attributes))


if __name__ == "__main__":
    main()
