# გვაქვს n სართულიანი კიბე, ერთ მოქმედებაში შეგვიძლია ავიდეთ 1 ან 2 საფეხურით.
# დაწერეთ ფუნქცია რომელიც დაითვლის n სართულზე ასვლის ვარიანტების რაოდენობას.

#4
def stair_options(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return stair_options(n - 2) + stair_options(n - 1)
