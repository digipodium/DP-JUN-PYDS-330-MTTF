# wap to generate a list of acronymns from a list of words using generators & *args


def acronym(*words):
    for word in words:
        yield ''.join([i[0].upper() for i in word.split()])

# ex call

for item in acronym('Project Manager','Software Engineer','Data Analyst'):
    print(item)


print(list(acronym('Project Manager','Software Engineer','Data Analyst','Team Lead',"Program tester")))