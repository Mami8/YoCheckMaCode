import os

def file_founder(path):
    try:
        all_files = os.listdir(path)
        pdfList = []
        docxList = []
        dirs = []
        others = []
        
        for i in all_files:
            full_path = os.path.join(path, i)
            if os.path.isfile(full_path):
        
                if os.path.splitext(full_path)[-1] == '.pdf':
                    pdfList.append(full_path)
        
                elif os.path.splitext(full_path)[-1] == '.docx':
                    docxList.append(full_path)
        
                elif os.path.isdir(full_path):
                    dirs.append(full_path)
                
                else:
                    others.append(full_path)
        
        if dirs ==  []:
            return pdfList, docxList, all_files, others,0
        
        else:
            for i in dirs:
                _pdfList, _docxList, _all_files, _others,iserror = file_founder(i)
                pdfList.append(_pdfList)
                docxList.append(_docxList)
                all_files.append(_all_files)
                others.append(_others)
                
        return pdfList, docxList, all_files, others, 0
    except Exception as e:
        print ("Filefounder failed: " + str(e))
        return None, None, None, None, 1





def iterate(keyword, files):
    targets = []
    if type(files) == list or type(files) == tuple:
        for i in files:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    targets.append(j)
            else:
                targets.append(i)
    else:
        targets = files
    try:
        for i in files:
            with open(i, 'r') as f:
                if keyword in f.read():
                    return i, 0
    except Exception as e:
        print (str(e))
        return e, 1
    return None, 0
