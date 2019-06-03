import re


print('==============AssessmentResult 추출==============')
print('==============파일읽기==============')
rfile2 = open('c:/assess_log2.txt','r', encoding='UTF-8')
filedata = str(rfile2.readlines())
result = []
header = ""
result.append(header)
result2 = []
"""
AssessmentResult fillter
"""

rex = re.compile("(', ')[0-9][0-9]:[0-9][0-9]:[0-9][0-9]'\).*?(AssessmentResult)")
filedata = re.sub(rex, '\n\n&&&&&&AssessmentResult', filedata)
rex = re.compile("\['\\\\ufeff.*?(AssessmentResult)")
filedata = re.sub(rex, '\n\n&&&&&&AssessmentResult', filedata)
rex = re.compile("\['\\\\ufeff.*?(AssessmentResult)")
filedata = re.sub(rex, '\n\n&&&&&&AssessmentResult', filedata)
rex = re.compile("', '[0-9][0-9]:[0-9][0-9]:[0-9][0-9].*?(CONNECTION) \*\/\;\\\\n'\]")
filedata = re.sub(rex, '\n\n&&&&&&AssessmentResult', filedata)
AssessmentResult_list = filedata.split("&&&&&&")


for AssessmentResultData in AssessmentResult_list:
    
    TrackResult_list = AssessmentResultData.replace('TrackResult','&&&&&&TrackResult').split('&&&&&&')
    for TrackResultData in TrackResult_list:

        trackName=''
        if(0<TrackResultData.count('trackName')):
            trackName = re.search('(trackName).*?(,)',TrackResultData).group()
        

        if 0<TrackResultData.count('RuleResult'):
            RuleResult_list = TrackResultData.replace("RuleResult","&&&&&&RuleResult").split('&&&&&&')
            for idx,RuleResultData in enumerate(RuleResult_list):
                if(0<idx):
                    # print(idx,'====================RuleResultData==========================')
                    subjectGroupName = re.search('(subjectGroupName).*?(,)',TrackResultData).group()
                    Department = re.search('(department\:Department\().*?(\))',TrackResultData).group()
                    no = re.search('(no=).*?(,)',Department).group()
                    Departyear = re.search('(year=).*?(,)',Department).group()
                    name = re.search('(name=).*?(\))',Department).group()

                    
                    ExcelData_list = RuleResultData.replace('ExcelData','&&&&&&ExcelData').split('&&&&&&')
                    for idx,ExcelData in enumerate(ExcelData_list):
                        if(0<idx):
                            year = re.search('(year).*?(,)',ExcelData).group()
                            semester = re.search('(semester).*?(,)',ExcelData).group()
                            admissionYear = re.search('(admissionYear).*?(,)',ExcelData).group()
                            studentId = re.search('(studentId).*?(,)',ExcelData).group()
                            dept = re.search('(dept).*?(,)',ExcelData).group()
                            subjectNo = re.search('(subjectNo).*?(,)',ExcelData).group()
                            subjectName = re.search('(subjectName).*?(,)',ExcelData).group()
                            category = re.search('(category).*?(,)',ExcelData).group()
                            teaching = re.search('(teaching).*?(,)',ExcelData).group()
                            selectArea = re.search('(selectArea).*?(,)',ExcelData).group()
                            credit = re.search('(credit).*?(,)',ExcelData).group()
                            evaluationMethod = re.search('(evaluationMethod).*?(,)',ExcelData).group()
                            grade = re.search('(grade).*?(,)',ExcelData).group()
                            score = re.search('(score).*?(,)',ExcelData).group()
                            openDept = re.search('(openDept).*?(,)',ExcelData).group()
                            engineeringDesignSubject = re.search('(engineeringDesignSubject).*?(\))',ExcelData).group()
                            
                            temp=str((trackName,subjectGroupName,no,Departyear,name,year,semester,subjectNo,subjectName,category,teaching,selectArea,credit,evaluationMethod,grade,score,openDept,engineeringDesignSubject))
                            header = "trackName,subjectGroupName,no,Departyear,name,year,semester,subjectNo,subjectName,category,teaching,selectArea,credit,evaluationMethod,grade,score,openDept,engineeringDesignSubject)"+'\n'
                            temp = re.sub('(,).*?(=)',',',temp)
                            temp = re.sub('(\().*?(=)','',temp) + '\n'

                            result.append(temp)


wfile = open("c:/data.txt",'w', encoding='UTF-8')
wfile.writelines(result)

print('============== 끝==============')

