import argparse
import urllib.request
import csv
import re


def downloadData(url):
    """Opens data"""
    response = urllib.request.urlopen(url)
    lines = [li.decode('utf-8') for li in response.readlines()]
    "Decodes data"
    csvData = list(csv.reader(lines))
    return csvData


def processData(csvData):
    """
    Searches for image files: .jpg, .gif, or .png using regular expression
    Prints # of hits, percentage-wise for images.
    Then,
    Finds most popular browser: Firefox, Chrome, Internet Explorer, or Safari
    """
    count = 0
    count1 = 0
    for row in csvData:
        img = len(re.findall(r".(jpg|gif|png)$", row[0], re.I))
        if img == 1:
            count += 1
        count1 += 1
    rate = str(count / count1 * 100)
    print("Image requests account for {}% of all requests.".format(rate))

    f = r"Firefox"
    countF = 0
    for row in csvData:
        cf = len(re.findall(f, row[2], re.I))
        if cf == 1:
            countF += 1
    c = r"Chrome"
    countC = 0
    for row in csvData:
        cc = len(re.findall(c, row[2], re.I))
        if cc == 1:
            countC += 1
    ie = r"Internet Explorer"
    countI = 0
    for row in csvData:
        ci = len(re.findall(ie, row[2], re.I))
        if ci == 1:
            countI += 1
    s = r"Safari"
    countS = 0
    for row in csvData:
        cs = len(re.findall(s, row[2], re.I))
        if cs == 1:
            countS += 1

    browser = {f: countF, c: countC, ie: countI, s: countS}
    highest = max(browser, key=browser.get)
    print("Most popular browser is {}.".format(highest))


def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str,
                        required=True)
    args = parser.parse_args()
    main(args.url)

file = processData(downloadData(args.url))
