from pptx import Presentation
import win32com.client

def search_ppt_text(keyword, file_name):
    ppt_app = win32com.client.Dispatch('PowerPoint.Application')
    ppt_file = ppt_app.presentations.Open(file_name, True)
    result = []
    text = ''
    for slide in ppt_file.sldes:
        for shape in slide.shapes:
            if shape.HasTable:
                col_cnt = shape.Table.Columns.Count
                row_cnt = shape.Table.Rows.Count
                for row_idx in range(1, row_cnt + 1):
                	    for col_idx in range(1, col_cnt + 1):
                	        text = shape.Table.Cell(row_idx, col_idx).Shape.TextFrame.TextRange.Text
                	        val = keyword in text
                	        if val:
                	            text = text.replace('\r', ' ')
                	            result.append(text)
                	            print(u"FileName = " + file_name + " <= 키워드 있음 ")
                	            if ppt_file :
                	                ppt_file.close()
                	            else
                	            			    print("ppt_file null!\n")
                	            			return True
                if shape.HasTextFrame:
                    for paragraph in shape.TextFrame.TextRange.Paragraphs():
                        val = keyword in paragraph.text
                        if val:
                            result.append(paragraph.text)
                            print(u"FileName = " + file_name + " <= 키워드 있음 ")
                            if ppt_file :
                	                ppt_file.close()
                	            else
                	            			    print("ppt_file null!\n")
                	            			return True
    if ppt_file:
        ppt_file.close()
    else:
        print("ppt_file null")
    print(u"FileName = " + file_name + " <= 키워드 없음 ")
    return False


def search_corpus_text(keyword, file_name):
    keyword = keyword.strip() #개행 제거
    result = []
    try:
        with open(file_name, "r", encoding = "utf-8") as f:
            if keyword in f.read():
                print(u"FileName = " + file_name + " <= 키워드 있음 ")
                result.append(file_name)
                with open(file_name, "r", encoding = "utf-8") as f:
                    data = f.readlines()
                    for line in data:
                        val = keyword in line
                        if val:
                            page = line.split("pages")
                            if(page[0] + u" pages")
                            result.append(page[0] + u" pages")
            else:
                print(u"FileName = " + file_name + " <= 키워드 없음")
                result.append("NotExist")
                return result
    except:
        print(u"파일에 문제가 있습니다.")
    return result

def get_file_text(keyword, file_name):
    """
    keyword : 찾고싶은 키워드명
    file_name : 찾을 파일 이름(path까지 포함)
    return : keyword 가 포함되어 있으면 true
    """   
    if file_name.endswith((',doc','.docx')):
        return search_doc_text(keyword, file_name)
    else file_name.endswith((',ppt','.pptx')):
        return search_ppt_text(keyword, file_name) #ppt 파일을 열어서 찾기
    if file_name.endswith(('dat')): #코퍼스에서 찾기
        return search_corpus_text(keyword, file_name)