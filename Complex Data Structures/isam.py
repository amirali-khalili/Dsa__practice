# ساختار اولیه ISAM
def create_isam(data, index_step=3):
    data = sorted(data)  # داده‌ها مرتب میشن
    index = {}
    for i in range(0, len(data), index_step):
        index[data[i]] = i  # هر index_step یک کلید توی ایندکس
    return {"data": data, "index": index, "overflow": []}


# تابع جستجو
def search_isam(isam, key):
    index = isam["index"]
    data = isam["data"]
    overflow = isam["overflow"]

    # 1. پیدا کردن محدوده از طریق ایندکس
    keys = sorted(index.keys())
    pos = 0
    for k in keys:
        if key >= k:
            pos = index[k]
        else:
            break

    # 2. جستجو ترتیبی داخل دیتا
    for i in range(pos, min(pos+3, len(data))):
        if data[i] == key:
            return True

    # 3. جستجو در overflow
    if key in overflow:
        return True

    return False


# تابع درج
def insert_isam(isam, key):
    data = isam["data"]
    if key in data or key in isam["overflow"]:
        return  # تکراری وارد نمی‌کنیم

    # اگر وسط دیتا جا نمی‌شد میره تو overflow
    if key < data[-1]:
        isam["overflow"].append(key)
    else:
        data.append(key)
        data.sort()
# ساخت ایندکس
isam = create_isam([10, 20, 30, 40, 50, 60, 70], index_step=2)

print("ایندکس:", isam["index"])
print("داده:", isam["data"])

# جستجو
print("جستجو 30:", search_isam(isam, 30))
print("جستجو 25:", search_isam(isam, 25))

# درج
insert_isam(isam, 25)
print("Overflow:", isam["overflow"])
print("جستجو 25 بعد از درج:", search_isam(isam, 25))
