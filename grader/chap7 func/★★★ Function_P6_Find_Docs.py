def read_data():
    #เก็บเป็นdictของ{book:keyword}
    docs = {}
    n = int(input().strip())
    for i in range(n):
        tokens = input().strip().split()
        doc_name = tokens[0]
        doc_keywords = tokens[1:]
        for kword in doc_keywords:
            if doc_name in docs.keys():
                docs[doc_name].add(kword)
            else:
                docs[doc_name] = {kword}

    return docs

def search(docs, condition, search_keywords):
 # คืนรายการของชื่อเอกสารตามรายการค าใน search_keywords(setlist -> set
 # condition เป็น 'and' ให้คืนรายการของชื่อเอกสารที่มีทุกค าใน search_keywords
 # condition เป็น 'or' ให้คืนรายการของชื่อเอกสารที่มีอย่างน้อย 1 ค าใน search_keywords
 # condition เป็นอย่างอื่น ให้คืน รายการว่าง ๆ
    search_keywords = set(search_keywords)
    out = []
    if condition == "and":
        for book in docs:
            if search_keywords.issubset(docs[book]):
                out.append(book)
    elif condition == "or":
        for book in docs:
            if search_keywords.intersection(docs[book]) != set():
                out.append(book)
    return out
        
#==== Program starts here =======================
docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )
#=================================================
