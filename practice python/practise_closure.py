# 联系闭包
from collections.abc import Sized


def outer(str):
    def inner(innerstr):
        print(f"{str}{innerstr}{str}")

    return inner

fn1 = outer("chaos")
fn1("AAA")

fn2 = outer("chaos")
fn2("ccc")
a = [1,2,3]
b = [4,5,6]
print(a+[6])
a = list()
Sized