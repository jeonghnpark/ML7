import csv


def save_to_file(fn,jobs):
    file = open(fn, 'w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'link'])

    for job in jobs:
        writer.writerow([job['title'], job['company'], job['link']])
        # print([job['title'], job['company'], job['link']])
    file.close()


if __name__ == "__main__":
    jobs = [{'title': 'this title', 'company': 'naver', 'link': 'naver.com'}]
    save_to_file(jobs)
