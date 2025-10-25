#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hello Worldと四則演算のデモンストレーション
"""


def hello_world():
    """Hello Worldを表示する"""
    print("Hello World!")
    print("こんにちは、世界!")


def add(a, b):
    """加算"""
    return a + b


def subtract(a, b):
    """減算"""
    return a - b


def multiply(a, b):
    """乗算"""
    return a * b


def divide(a, b):
    """除算"""
    if b == 0:
        raise ValueError("0で除算することはできません")
    return a / b


def main():
    """メイン関数"""
    # Hello World
    hello_world()
    print()

    # 四則演算のデモ
    print("=== 四則演算のデモ ===")
    num1 = 10
    num2 = 3

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} × {num2} = {multiply(num1, num2)}")
    print(f"{num1} ÷ {num2} = {divide(num1, num2):.2f}")

    # 追加の例
    print()
    print("=== より複雑な計算 ===")
    a, b, c = 15, 4, 2
    result = add(multiply(a, b), divide(c, b))
    print(f"({a} × {b}) + ({c} ÷ {b}) = {result:.2f}")


if __name__ == "__main__":
    main()
