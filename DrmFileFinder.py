#### -*- coding: utf-8 -*-

from contextlib import closing
from time import time
from tkinter import *
import tkinter.ttk
import multiprocessing
import clipboard
import sys
import os

import multi_search as ms
import searchController as sc

global gSearch_keyword # 키워드 변수
global platform_base_path # platform 에 베이스 경로
global gCorpus_file_path

def drmFileFinder():
    print(u"=====================")
    print(u"         DRM file Finder!         ")
    print(u"=====================")

    # 검색 결과 담을 곳
    result = []

    # 현재 폴더 위치
    print(os.getcwd())
    global platform_base_path
    # platform_base_path = u"C:\\Users\\Administrator\\test"
    file_name = "CorpusPath.dat"

    # keyword = u'지도'
    global gSearch_keyword
    keyword = gSearch_keyword
    try:
        # CorpusPath.dat 파일이 있는 절대 경로포함 파일 위치
        openfile = platform_base_path + '\\' + file_name
        with open(openfile, "r", encoding = "utf-8") as f:
            temp = f.readline()
            file_path = temp.strip()
            print(u"Filepath : " + file_path)
    except:
        print(u"CorpusPath.dat 파일이 없습니다. 관리자에게 문의 바랍니다.")
        return result

    global gCorpus_file_path
    # file_path = u"C:\\User\\Administrator\\Documents\\test"
    # print(file_path)
    try :
        print("====file list ====")
        file_list = []
        file_tepes = ('.dat')
        for f in os.listdir(file_path):
            if f.startswith('~$'):
                continue
            if f.endswith(file_types):
                print(f)
                file_list.append(file_path + "\\" + f)
        print("===========")
        print("Finding....")
        print("--------------")
        start_time = time()

        # 파일 하나하나 열어서 검색
        for fa in file_list:
            ret = sc.get_file_tet(keyword,fa)
            result.append(ret)
        print("--------------")
        end_time = time()
        print("==== end!!!")
        return result

        # window 띄우기
        root = Tk()
        root.title(u"검색기 [Beta]")
        root.resizable(False, False) # 사이즈 고정

        label1 = Label(root, text = '검색할 단어를 입력하세요')
        labe1.grid(row=1, column=0)

        # 검색창
        entry1 = Entry(root, width=70, border=1, borderwidth=3, relief = 'solid')
        entry1.grid(ow=2, column=0)

        # 우선 선언만 함
        frame = Frame(root)
        scrollbar = Scrollbar(frame)
        listbox = Listbox(frame, yscrollcommand = scrollbar,set, width = 70, height=0)
        var = StringVar()
        message = Message(root, width=300, relief="solid", textvariable = var)

        values=["리스트1","리스트2","리스트3"]
        combobox = tkinter.ttk.Combobox(root, height=15, value=values, state='readonly'

        def combo_click(event):
             global platform_base_path
             str = combobox.get()
             if(str = "리스트1"):
                 platform_base_path = "\\ url"
             else:
                 platform_base_path = ""
                 print("선택한 플래폼 : " + platform_base_path)

        combobox.set("list 선택")
        combobox.grid(row=0, column=0)
        combobox.bind('<<ComboboxSelected>>', combo_click)

        # 선택한 리스트 클립보드 복사
        def click_item(event):
            value = listbox.curselection()
            print(u"클립보드 복사 : " + (listbox.get(value[0], value[0]))[0])
            clipboard.copy((listbox.get(value[0], value[0])[0]))
            var.set("클립보드에 복사되었습니다.")
            temp = gCorpus_file_path.replace(platform_base_path + "\\","")
            tempSplit = temp.split("\\")
            # tempSplit[0] 검색한 폴더명
            existdir = platform_base_path + "\\" + tempSplit[0]
            os.startfile(existdir)

    # 검색키 입력 시 이벤트
    def clickEvent(event):
        global gSearch_keyword
        gSearch_keyword = entry1.get()

        result = []
        result = drmFileFinder()

        index = 1
        if len(result) == 0:
            print(u"검색할 파일이 없습니다. 관리자에게 문의 바랍니다.")
         else:
             listbox.delete(0, listbox.size())
             for value in result:
                 if(value[0] != "NotExist"):
                     gCorpus_file_path
                     file_name = value[0].replace(gCorpus_file_path + "\\", "").replace(".dat","")
                     listbox.insert(index, file_name)
                     index = index +1
             value = listbox.size()
             if(value !=0):
                 listbox.grid(row=3, column=0)
                 scrollbar.grid(row=3, column=1)
                 scrollbar["command"]=listbox.yview
                 listbox.bind('<ButtonRelease-1>', click_item)
                 var.set("list 선택 시 파일명 복사 및 파일 위치의 폴더를 엽니다.") # 메세지 텍스트
             else
                 var.set("파일에 해당 키워드가 존재하지 않습니다.") # 메세지 텍스트
             frame.grid(row=4, column=0)
             message.grid(row=5, column=0)
    entry1.bind("<Return>", clickEvent)
    mainloop()

    # multi process를 돌리면 process수만큼 __mp_main__ 로 호출됨
    # pyinstaller 를 하면 __main__으로 호출되어 무한 루프에 빠짐
    if __name__ == "__main__":
        multiprocessing.freeze_support() # for multiprocessing other process on windows
        print(u"=============")
        print(u"     Finder v 0.9")
        print(u"=============")