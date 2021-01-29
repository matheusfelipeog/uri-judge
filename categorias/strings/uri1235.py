# -*- coding: utf-8 -*-


def decrypt(encrypted_text):
    middle = len(encrypted_text) // 2

    left_text = encrypted_text[:middle]
    right_text = encrypted_text[middle:]

    return reversed_text(left_text) + reversed_text(right_text)


def reversed_text(text):
    return ''.join(
        list(
            reversed(text)
        )
    )


n = int(input())

for _ in range(n):
    text_line = input()

    decrypted_text = decrypt(text_line)

    print(decrypted_text)
