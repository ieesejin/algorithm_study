# https://programmers.co.kr/learn/courses/30/lessons/42577


# No hash version
def solution(phone_book):
    answer = True
    phone_book.sort() # Since the elements are strings, they are sorted alphabetically

    for i in range(len(phone_book) - 1): # Last element could not be included in other elements
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break

    return answer


# Use hash version
def solution2(phone_book):
    answer = True
    hash = dict()

    for number in phone_book: # make hash map
        hash[number] = 1

    for number in phone_book:
        temp = ""
        for i in number: # increase it by one digit and look for it in the hash.
            temp += i
            if temp in hash and temp != number:
                answer = False
                return answer

    return answer


print(solution(["119", "97674223", "1195524421"])) # expected value: false
print(solution2(["119", "97674223", "1195524421"]))
