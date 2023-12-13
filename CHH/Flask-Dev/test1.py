def is_charlish_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(word) < 2:
        if word in vowels or word == "n":
            return True
        return False
    
    for i in range(1, len(word)):
        switch(ưo)
    return False

# Đọc xâu đầu vào từ người dùng
input_word = input().strip()

# Kiểm tra xem xâu có thuộc ngôn ngữ Charlish hay không
if is_charlish_word(input_word):
    print("Yes")
else:
    print("No")
