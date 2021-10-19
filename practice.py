# jumin = "960105-1169711"

# # print("성별: " + jumin[7])
# # print("연: " + jumin[0:2])

# domain = "http://google.com" # [7:12]
# # my_str = domain[7:]
# my_str = domain.replace("http://", "")
# # domain = 
# indexDot = my_str.index(".")
# my_str = my_str[0:indexDot]
# print(indexDot)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(password)

# print("{0}의 비밀번호는 {1}입니다.".format(domain, password))

# # print()


# num_list = [3, 4, 5, 2, 1]
# mix_list = ["조세호", 20, True]

# num_list.extend(mix_list)
# print(num_list)

# cabinet = {"A-3": "유재석", "B-100": "김태호"}
# print(cabinet)
# print(cabinet.items())
# del cabinet["A-3"]
# print(cabinet)


# from random import * 

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(lst)
# print(sample(lst, 1))
# print(sample(lst, 3))


# users = range(1, 21)
# users = list(users)
# print(users, type(users))


# absent = [2, 5]
# for student in range(1, 5) :
#     if student in absent:
#         continue
#     print("{0}번, 책 읽어봐".format(student))


# student = [1, 2, 3, 4, 5]
# print(student)
# student = [i + 100 for i in student]
# print(student)

# student = ["Iron man", "Thor", "I am groot"]
# student = [str(len("{0}".format(i))) for i in student]
# print(student)

# from functools import total_ordering
# from random import randrange

# passenger = range(1, 51)
# totalPass = 0
# for i in passenger:
#     spendTime = randrange(5, 51)
#     # if 5 <= spendTime & spendTime <= 15:
#     # if spendTime >= 5 & spendTime <= 15:
#     if spendTime >= 5 and spendTime <= 15:
#         print("[o] {0} 번째 손님 (소요시간 {1}분)".format(i, spendTime))
#         totalPass += 1
#     else:
#         print("[ ] {0} 번째 손님 (소요시간 {1}분)".format(i, spendTime))
# print("총 탑승 총객: {0}분".format(totalPass))


# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 확인되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money

# a, b = 2, 3
# print("a: ", a)
# print("b: ", b)

# # deposit(1000, 5000)


# def withdraw_night(balance, money):
#     commission =  100
#     return commission

# def profile(name, age, *language, hobby):
#     print("이름: {0} \t 나이: {1}\t".format(name, age), end= " ")
#     for lang in language:
#         print(lang, end=" ")
#     print("취미: {0}".format(hobby))

# profile("유재석", 20, "파이썬", "자바", hobby="농구")

# # def profile(name):
# #     print("이름:@ {0}".format(name))

# profile("김태호")

# def profile(name, age)

# def std_weight(height, sex):
#     if sex=="남자":
#         return height * height * 22
#     elif sex=="여자":
#         return height * height * 21

# height = 175
# sex = "남자"
# weight = round(std_weight(height / 100, sex), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, sex, weight))

# "ㅇㅇㅇ".zfill(2)


# print("{0:+,}".format(500000000))

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학: 0", file=score_file)
# print("영어: 53", file=score_file)
# score_file.close


# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
# lists = score_file.readlines()
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()



# lists = score_file.readlines()
# for list in lists:
#     print(list, end="")
# score_file.close


from os import name, rmdir
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박면수", "나이":30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.readline())

# weeks = range(1, 51)
# for i in weeks:
#     study_file = open(("{0}주차.txt".format(i)), "w", encoding="utf8")
#     study_file.write(str("{0}주차 주간보고서 입니다.".format(i)))

# weeks = range(1, 51)
# for i in range(1, 51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as study_file:
#         study_file.write(str(i) + "주차 주간보고서 입니다.")


# test = "test\
# ddd"

# print(test)

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


# gangnam = House("강남", "아파트", "매매", "10억", "2010년")
# mapho = House("마포", "오피스텔", "전세", "5억", "2007년")
# songpa = House("송파", "빌라", "월세", "500/50", "2000년")

# house_lists = []
# house_lists.append(gangnam)
# house_lists.append(mapho)
# house_lists.append(songpa)

# print("총 {0}대의 매물이 있습니다.".format(len(house_lists)))
# for house in house_lists:
    # house.show_detail()


# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self) -> str:
#         return self.msg

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         elif order > 10:
#             raise SoldOutError("재료가 소진되어 더 이상 주문을 받지 않습니다.")
#         elif chicken < order:
#             raise SoldOutError("재료가 소진되어 더 이상 주문을 받지 않습니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#     except ValueError:
#         print("잘못된 값을 입력하였습니다")
#     except SoldOutError as err:
#         print("재료가 소진되어 더 이상 주문을 받지 않습니다.")
#         break



# from random import *
# import theater_module as mv
# from theater_module import price_soldier as ps

# mv.price(4)
# ps(3)

# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# import glob
# # print(glob.glob("*.py"))

import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(rmdir, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir)

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))


import datetime
today = datetime.date.today()
td = datetime.timedelta(days=100)

print("우리가 만난지 100일은", today+td)


import byme
byme.sign()

