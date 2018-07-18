# code in module1
# if __name__ == "__main__": を追加すると、直接実行したときは普通に実行されるが、
# モジュールとして呼び出されたときは実行されなくなる。
if __name__ == "__main__":
    print("Hello!")


def cubed(x):
    return x ** 3
