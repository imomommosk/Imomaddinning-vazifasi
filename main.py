def kattason(x, y, z):
    return max(x, y, z)


def text_list(*text_list):
    title_list = []
    for text in text_list:
        title_list.append(text.title())
    return title_list