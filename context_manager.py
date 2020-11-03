import contextlib

@contextlib.contextmanager
def file_open(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()

path = "cities_and_times.txt"
with file_open(path, "r") as f:
    res = []
    for line in f.readlines():
        print(line)
        res.append(line)
        res = sorted(res)
    # print(res)
    with file_open('orderedhomework.txt', "w") as f:
        for line in res:
            f.write(line)
            print(line)
print("Done")
