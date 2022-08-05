import threading

from time import sleep


def main():
    for i in range(1, 100):
        print(i)
        sleep(1)


if __name__ == '__main__':
    for _ in range(10):
        thread = threading.Thread(target=main)
        thread.start()
