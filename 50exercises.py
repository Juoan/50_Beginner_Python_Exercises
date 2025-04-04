# 1.
get_str = str(input("Nhap 1 chuoi bat ki: "))
print(f"Do dai chuoi cua ban la: {len(get_str)}")

# 2.
get_str = str(input("Nhap 1 chuoi bat ki: "))

freq_dict = {}

for char in get_str:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

print(freq_dict)

# 3.
get_str = str(input("Nhap 1 chuoi bat ki: "))
if len(get_str) <= 2:
    print("Empty String!")
else:
    print(get_str[:2] + get_str[-2:])

# 4.
get_str = str(input("Nhap 1 chuoi bat ki: "))

first_char = get_str[0]
output = first_char

for char in get_str[1:]:
    if char == first_char:
        output += "$"
    else:
        output += char

print(output)
# 5.
get_str = str(input("Nhap 1 chuoi bat ki: "))
get_str2 = str(input("Nhap them 1 chuoi bat ki: "))
print(get_str2[:2] + get_str[2:] + " " + get_str[:2] + get_str2[2:])

# 6.
get_str = str(input("Nhap 1 chuoi bat ki: "))
if len(get_str) >= 3:
  if get_str[-3:] == "ing":
    print(get_str + "ly")
  else:
    print(get_str + "ing")
else:
  print(get_str)

# 7.
get_str = (input("Nhap 1 chuoi bat ki: "))

not_index = get_str.find('not')
poor_index = get_str.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
    get_str = get_str[:not_index] + 'good' + get_str[poor_index + 4:]

print(get_str)

# 8.
def find_longest_word(words):
    longest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word, max_length

words_list = (input("Nhap 1 chuoi bat ki: ")).split()
longest, length = find_longest_word(words_list)
print("Longest word:", longest)
print("Length:", length)

# 9.
get_str = str(input("Nhap 1 chuoi bat ki: "))
get_int = int(input("Ban muon loai bo ki tu thu (Vd: 1, 2, ...): "))

output = ""

for i in range(len(get_str)):
    if i == get_int:
      output += ""
    else:
      output += get_str[i]

print(output)

# 10.
get_str = str(input("Nhap 1 chuoi bat ki: "))
first_lett = get_str[0]
last_lett = get_str[-1]
print(last_lett + get_str[1:-1] + first_lett)

# 11.
get_str = str(input("Nhap 1 chuoi bat ki: "))
even_index_word = ""
for i in range(len(get_str)):
  if i % 2 == 0:
    even_index_word += get_str[i]
print(even_index_word)

# 12.
get_str = str(input("Nhap 1 chuoi bat ki: "))

split_str = get_str.split()
freq_dict = {}

for string in split_str:
    if string in freq_dict:
        freq_dict[string] += 1
    else:
        freq_dict[string] = 1

print(freq_dict)

# 13.
get_str = str(input("Nhap 1 input bat ki: "))
print(get_str.upper())
print(get_str.lower())

# 14.
get_str = input("nhap input ngan cach bang dau phay: ").split(",")

cleaned_words = []
for word in get_str:
    cleaned_words.append(word.strip())

unique_words = []
for word in cleaned_words:
    if word not in unique_words:
        unique_words.append(word)

print(", ".join(sorted(unique_words)))

# 15.
def add_HTML_tags(x, y):
  return f"'<{x}>" + y + f"</{x}>'"

print(add_HTML_tags('i', 'Python'))
print(add_HTML_tags('b', 'Python Tutorial'))

# 16.
def insert_middle_str(get_str, mid_str):
    mid_index = len(get_str) // 2
    return get_str[:mid_index] + mid_str + get_str[mid_index:]

get_str = input("Nhập một chuỗi bất kỳ: ")
mid_str = input("Nhập một chuỗi để đặt vào giữa: ")
print(insert_middle_str(get_str, mid_str))

# 17.
def insert_end(get_str):
    if len(get_str) < 2:
        return "Chuỗi phải có ít nhất 2 ký tự"
    while len(get_str) < 2:
      return get_str[-2:] * 4

get_str = input("Nhập một chuỗi bất kỳ: ")
print(insert_end(get_str))

# 18.
def first_three(get_str):
    if len(get_str) <= 3:
        return get_str
    while len(get_str) > 3:
      return get_str[:3]

get_str = input("Nhập một chuỗi bất kỳ: ")
print(first_three(get_str))

# 19.
get_str = input("Nhập một chuỗi bất kỳ: ")
get_spec_char = input("Kí tự đặc biệt bạn ngăn cách: ")

mod_str = ""

for char in get_str:
  if char != get_spec_char:
    mod_str += char
  else:
    break

print(mod_str)
#print(get_str.split(get_spec_char)[0])

# 20.
def reversed_str(get_str):
    if len(get_str) % 4 == 0:
        return get_str[::-1]

get_str = input("Nhập một chuỗi bất kỳ: ")
print(reversed_str(get_str))

# 21.
def convert_upper_str(get_str):
    count = 0
    for char in get_str[:4]:
        if char == char.upper():
           count += 1
           if count >= 2:
              return get_str.upper()

get_str = input("Nhập một chuỗi bất kỳ: ")
print(convert_upper_str(get_str))

# 22.
get_str = input("Nhập 1 chuỗi bất kì: ")

sorted_upp_str = []
sorted_low_str = []
sorted_num = []
sorted_special_char = []

for char in get_str:
    if char.isdigit():
        sorted_num.append(char)
    elif char.isupper():
        sorted_upp_str.append(char)
    elif char.islower():
        sorted_low_str.append(char)
    else:
        sorted_special_char.append(char)

sorted_str = sorted(sorted_special_char) + sorted(sorted_num) + sorted(sorted_upp_str) + sorted(sorted_low_str)

print("".join(sorted_str))

# 23.
string = "Hello World! \n Hello Everyone!"

print(string.replace("\n", ""))

# 24.
get_str = input("Nhập 1 chuỗi bất kì: ")
get_char = input("Kí tự bạn muốn kiểm tra: ")

if get_str[:len(get_char)] == get_char:
  print("Chuỗi bắt đầu bằng kí tự bạn kiểm tra")
else:
  print("Chuỗi không bắt đầu bằng kí tự bạn kiểm tra")

# 25.
get_str = input("Nhập 1 mật mã bất kì: ")
get_shift = input("Shift = ")

encrypted_str = ""

for char in get_str:
    encrypted_str += chr(ord(char) + int(get_shift))

print(encrypted_str)

# 26.
import textwrap

text = """Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant indentation."""

formatted_text = textwrap.fill(text, width=50)

print(formatted_text)

# 27.
text = """
    Python is an interpreted, high-level programming language.
    It is designed to be easy to read and simple to implement.
    Python emphasizes code readability and productivity.
"""

clean_text = textwrap.dedent(text)

print(clean_text)

# 28.
lines = []

print("Enter your multi-line input (enter 'done' when finished):")

while True:
    line = input()
    
    if line.lower() == 'done':
        break
    lines.append(line)

get_prefix = input("Nhập kí tự bạn muốn: ")

print("\nYour multi-line output:\n")
for line in lines:
    print(get_prefix + line)
  
#29. 
lines = []

print("Enter your multi-line input (enter 'done' when finished):")

while True:
    line = input()
    
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nYour multi-line output:\na")
for line in lines:
    print("\t" + line)

# 30.
get_num = float(input("Nhập 1 số bất kì: "))
print("Kết quả sau khi làm tròn đến 2 số thập phân: {:.2f}".format(get_num))

# 31.
get_num = float(input("Nhập 1 số bất kì: "))
print("Kết quả sau khi làm tròn đến 2 số thập phân: {:+.2f}".format(get_num))

# 32.
get_num = float(input("Nhập 1 số bất kì: "))
print(f"Kết quả sau khi làm tròn: {round(get_num)}")

# 33.
get_num = input("Nhập 1 số: ")
spec_width = int(input("Nhập chiều rộng: "))

if spec_width > len(get_num):
  print( "0" * (spec_width - len(get_num)) + get_num)
else:
  print(get_num)
  # get_num.zfill(spec_width)

# 34.
get_num = input("Nhập 1 số bất kì: ")
get_width = int(input("Nhập chiều rộng: "))

if len(get_num) < get_width:
    print(get_num + "*" * (get_width - len(get_num)))
else:
    print(get_num)

# 35.
get_num = int(input("Nhập 1 số: "))
print("{:,}".format(get_num))

# 36.
get_num = float(input("Nhập 1 số thập phân: "))
print(f"{get_num*100:.2f}%")

# 37.
get_num = input("Nhập 1 số bất kì: ")
width = 10

print(get_num.ljust(width) + get_num.center(width) + get_num.rjust(width))

# 38.
get_str = input("Nhập 1 chuỗi bất kì: ")
get_substr = input("Nhập 1 chuỗi con cần đếm: ")

count = get_str.count(get_substr)

print(f"'{get_substr}' xuất hiện {count} lần.")

# 39.
get_str = input("Nhập 1 chuỗi bất kì: ")
print(get_str[::-1])

# 40.
get_str = input("Nhập 1 chuỗi bất kì: ").split()
print(" ".join(get_str[::-1]))

# 41.
get_str = input("Nhập 1 chuỗi bất kì: ")
get_chars = input("Nhập các kí tự bạn muốn loại bỏ: ")

mod_str = ""

for char in get_str:
    if char not in get_chars:
        mod_str += char

print(mod_str)

# 42.
get_str = input("Nhập 1 chuỗi bất kì: ")

repeated_char = {}

for char in get_str:
  if char in repeated_char:
    repeated_char[char] += 1
  else:
    repeated_char[char] = 1

for char, count in repeated_char.items():
    if count > 1:
        print(f"{char} {count}")

# 43.
rec_length = 5
rec_width = 4

cyl_radius = 5
cyl_height = 5

print(f"Diện tích hcn = {rec_width*rec_length} m²")
print(f"Thể tích hình trụ = {3.14*cyl_radius*cyl_radius*cyl_height} m³")

# 44.
get_str = input("Nhập 1 chuỗi bất kì: ")

for i in range(len(get_str)):
    print(f"Current character {get_str[i]} position at {i}")

# 45.
import string

get_str = input("Nhập 1 chuỗi bất kì: ")

alphabet_set = set(string.ascii_lowercase)

for char in get_str.lower():
    if char in alphabet_set:
        alphabet_set.remove(char)

if len(alphabet_set) == 0:
    print("Chuỗi chứa tất cả các kí tự trong bảng chữ cái")
else:
    print(f"Chuỗi chỉ chứa {len(get_str)} chữ cái")

# 46.
get_str = input("Nhập 1 chuỗi bất kì: ").split()
print(get_str)

# 47.
get_str = input("Nhập 1 chuỗi bất kì: ")
lwc_num = int(input("Bạn muốn chuỗi được ghi thường đến thứ tự số: "))

fixed_str = get_str[:lwc_num].lower() + get_str[lwc_num:]

print(fixed_str)

# 48.
get_str = input("Nhập 1 chuỗi bất kì: ")

swapped_str = ""

for char in get_str:
    if char == ".":
        swapped_str += ","
    elif char == ",":
        swapped_str += "."
    else:
        swapped_str += char

print(swapped_str)

# 49.
get_str = input("Nhập 1 chuỗi bất kì: ")

vowels = {"u", "e", "a", "o", "i"}
is_vowel = [char for char in get_str if char in vowels]

print(f"Số lượng nguyên âm trong chuỗi là: {len(is_vowel)}")
print(f"Các nguyên âm trong chuỗi là: {"".join(is_vowel)}")

# 50.
get_str = input("Nhập 1 chuỗi bất kì: ")

char_count = {}

for char in get_str:
    char_count[char] = char_count.get(char, 0) + 1

for char in get_str:
    if char_count[char] == 1:
        print(f"Kí tự lặp 1 lần là: {char}")
        break
else:
    print("Không có kí tự nào không lặp lại.")
