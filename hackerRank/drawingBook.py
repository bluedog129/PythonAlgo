n = 5
p = 3

def pageCount(n, p):
    page_in_book = p//2
    total_page = n//2

    from_front = page_in_book
    from_back = total_page-page_in_book

    return min(from_back,from_front)


print(pageCount(n, p))