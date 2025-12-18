# 19) Book Library System (Simple) 
# Given: 
# books = { 
# 101: {"title": "Python Basics", "qty": 4}, 
# 102: {"title": "React Guide", "qty": 2}, 
# } 

# Scenario: A student borrows book 101. 
# Task: Reduce the quantity, but only if available. 
# Approach: Check qty>0 then decrement, otherwise report unavailable.


books = { 
    101: {"title": "Python Basics", "qty": 4}, 
    102: {"title": "React Guide", "qty": 2}, 
} 

book_id_to_borrow = 101
if book_id_to_borrow in books:
    if books[book_id_to_borrow]["qty"] > 0:
        books[book_id_to_borrow]["qty"] -= 1
        print(f'Borrowed "{books[book_id_to_borrow]["title"]}". Remaining qty: {books[book_id_to_borrow]["qty"]}')
    else:
        print(f'Sorry, "{books[book_id_to_borrow]["title"]}" is currently unavailable.')