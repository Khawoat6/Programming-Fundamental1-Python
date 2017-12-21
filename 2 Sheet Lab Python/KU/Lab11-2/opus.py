# -*- coding: utf-8 -*-
# OPUS Document Generator for Computer Engineering Project
# Department of Computer Engineering
# Faculty of Engineering at Siracha
# Kasetsart University, Siracha Campus.
#
# Licensing Information:
# The OPUS project was developed by Vacharapat Mettanant
# Started in 2013


import datetime
import sys
import os

class ControllerParser:
    def __init__(self, filename):
        self.f = open(filename,'r')
    def close(self):
        self.f.close()
    def hasMoreCommand(self):
        while True:
            self.command = self.f.readline()

            if not self.command:
                return False
            else:
                state = 'normal'
                commentid = -1
                for i in range(len(self.command)):
                    if state == 'normal':
                        if self.command[i] == '\\':
                            state = 'code'
                        elif self.command[i] == '%':
                            commentid = i
                            state = 'comment'
                    elif state == 'code':
                        state = 'normal'
                if commentid >= 0:
                    self.command = self.command[:commentid]
                self.command = self.command.strip()
                if len(self.command)>0:
                    self.command = self.command.split()
                    return True
    def commandString(self):
        result = ''
        for s in self.command:
            result = result + s + ' '
        return result
        
class CodeWriter:
    def __init__(self, filename, information):
        self.f = open(filename,'w')
        self.info = information
        self.translator = TexTranslator(information)
        
    def close(self):
        self.f.close()
        
    def write(self, s):
        self.f.write(self.thaicode(s))
        
    def writeLine(self, s):
        self.f.write(self.thaicode(s) + '\n')
    
    def translateAndWrite(self, s):
        self.write(self.translator.translate(s))
    
    def translateAndWriteLine(self, s):
        self.writeLine(self.translator.translate(s))
        
    def thaicode(self,s):
        result = ''
        thstart=[]
        thstop=[]
        state='en'
        for i in range(len(s)):
            c = s[i]
            if ord(c)>=128:
                if state=='en':
                    thstart.append(i)
                    state='th'
            else:
                if state=='th':
                    thstop.append(i)
                    state='en'
        if state=='th':
            thstop.append(len(s))
        laststop=0
        for i in range(len(thstart)):
            result = result + s[laststop:thstart[i]]
            result = result + '{\\thi '      
            result = result + s[thstart[i]:thstop[i]]
            result = result + '}'
            laststop = thstop[i]
        result = result + s[laststop:]
        return result
    
    def writeReport(self):
        self.writeHeader()
        self.writeReportMainCover()
        self.writeReportInsideCover()
        self.writeApprovalForm()
        self.writeAbstractTH()
        self.writeAbstractEN()
        self.writeAcknowledgement()
        self.writeTableOfContents()
        self.writeChapters()
        self.writeReferences()
        self.writeAppendices()
        self.writeEnding()
    
    def writeProposal(self):
        self.writeHeader()
        self.writeProposalCover()
        self.writeChapters()
        self.writeReferences()
        self.writeEnding()
        
    def writeHeader(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('%%        OPUS Document Ganerator')
        self.writeLine('%%        Project ' + information['TYPE'] + ': ' + information['DOCUMENT'])
        self.writeLine('%%')
        self.writeLine('%%        Computer Engineering Project')
        self.writeLine('%%        Department of Computer Engineering')    
        self.writeLine('%%        Faculty of Engineering at Siracha')  
        self.writeLine('%%        Kasetsart University, Siracha Campus')  
        self.writeLine('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\documentclass[12pt,a4paper,oneside]{book}')
        self.writeLine('\\usepackage{fontspec}')
        self.writeLine('\\usepackage{xunicode}')
        self.writeLine('\\usepackage{xltxtra}')
        self.writeLine('\\usepackage{graphicx}')
        self.writeLine('\\usepackage{tabularx}')
        self.writeLine('\\usepackage{lastpage}')
        self.writeLine('\\usepackage{titlesec}')
        self.writeLine('\\usepackage{fancyvrb}')
        self.writeLine('\\usepackage{hyperref}')
        self.writeLine('\\usepackage{multicol}')
        self.writeLine('\\usepackage[font=large, labelfont=bf]{caption}')
        self.writeLine('\\titleformat{\\chapter}[display]{\\Huge\\bfseries\\centering}{\\chaptertitlename\\ \\thechapter}{20pt}{}')
        self.writeLine('')
        self.writeLine('\\defaultfontfeatures{Scale=1.23}')
        self.writeLine('\\XeTeXlinebreaklocale "th_TH"')
        self.writeLine('')
        self.writeLine('\\newcommand{\\thi}{\\fontspec[Scale=1.23]{TH Sarabun New}}')
        self.writeLine('\\newcommand\\thisYear{\\advance\\year by 543 \\the\\year\\advance\\year by -543}')
        self.writeLine('\\renewcommand{\\contentsname}{สารบัญ}')
        self.writeLine('\\renewcommand{\\listtablename}{สารบัญตาราง}')
        self.writeLine('\\renewcommand{\\listfigurename}{สารบัญภาพ}')
        self.writeLine('\\renewcommand{\\chaptername}{บทที่}')
        self.writeLine('\\renewcommand{\\figurename}{ภาพที่}')
        self.writeLine('\\renewcommand{\\tablename}{ตารางที่}')
        self.writeLine('\\renewcommand{\\appendixname}{ภาคผนวก}')
        self.writeLine('\\renewcommand{\\bibname}{เอกสารและสิ่งอ้างอิง}')
        self.writeLine('')
        self.writeLine('\\linespread{1.2}')
        self.writeLine('\\setlength{\\textwidth}{5.8in}')
        self.writeLine('\\setlength{\\topmargin}{-0.5in}')
        self.writeLine('\\setlength{\\oddsidemargin}{0.5in}')
        self.writeLine('\\setlength{\\parskip}{0.2in}')
        self.writeLine('\\setlength{\\parindent}{0.5in}')
        self.writeLine('\\setlength{\\textheight}{9.0in}')
        self.writeLine('\\setlength{\\footskip}{0.5in}')
        self.writeLine('')
        self.writeLine('%%%%%%%%%%%%%%%%%%% Document Start %%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\begin{document}')
        self.writeLine('\\pagestyle{myheadings}')
        self.writeLine('\\pagenumbering{gobble}')      
        self.writeLine('{\\fontsize{14pt}{16pt}\\selectfont') # ขนาดตัวอักษรปรกติสำหรับ Report
        self.writeLine('')
    
    def writeNote(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('%%        OPUS Document Ganerator')
        self.writeLine('%%        Project Note: ' + information['PROJECT'])
        self.writeLine('%%')
        self.writeLine('%%        Computer Engineering Project')
        self.writeLine('%%        Department of Computer Engineering')    
        self.writeLine('%%        Faculty of Engineering at Siracha')  
        self.writeLine('%%        Kasetsart University, Siracha Campus')  
        self.writeLine('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\documentclass[12pt,a4paper,oneside]{article}')
        self.writeLine('\\usepackage{fontspec}')
        self.writeLine('\\usepackage{xunicode}')
        self.writeLine('\\usepackage{xltxtra}')
        self.writeLine('\\usepackage{graphicx}')
        self.writeLine('\\usepackage{tabularx}')
        self.writeLine('\\usepackage{lastpage}')
        self.writeLine('\\usepackage{titlesec}')
        self.writeLine('\\usepackage{fancyvrb}')
        self.writeLine('\\usepackage{hyperref}')
        self.writeLine('\\usepackage{multicol}')
        self.writeLine('\\usepackage[font=large, labelfont=bf]{caption}')
        self.writeLine('')
        self.writeLine('\\defaultfontfeatures{Scale=1.23}')
        self.writeLine('\\XeTeXlinebreaklocale "th_TH"')
        self.writeLine('')
        self.writeLine('\\newcommand{\\thi}{\\fontspec[Scale=1.23]{TH Sarabun New}}')
        self.writeLine('\\newcommand\\thisYear{\\advance\\year by 543 \\the\\year\\advance\\year by -543}')
        self.writeLine('\\renewcommand{\\figurename}{ภาพที่}')
        self.writeLine('\\renewcommand{\\tablename}{ตารางที่}')
        self.writeLine('')
        self.writeLine('\\linespread{1.2}')
        self.writeLine('\\setlength{\\textwidth}{6.5in}')
        self.writeLine('\\setlength{\\topmargin}{-0.5in}')
        self.writeLine('\\setlength{\\oddsidemargin}{0in}')
        self.writeLine('\\setlength{\\parskip}{0.2in}')
        self.writeLine('\\setlength{\\parindent}{0in}')
        self.writeLine('\\setlength{\\textheight}{9.0in}')
        self.writeLine('\\setlength{\\footskip}{0.5in}')
        self.writeLine('')
        self.writeLine('%%%%%%%%%%%%%%%%%%% Document Start %%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\begin{document}')
        self.writeLine('\\pagestyle{myheadings}')
        self.writeLine('\\pagenumbering{arabic}')      
        self.writeLine('{\\fontsize{12pt}{13pt}\\selectfont') # ขนาดตัวอักษรปรกติสำหรับ Note
        self.writeLine('')

        f = open(self.info['SOURCE'], 'r')
        s = f.readline()
        while s:
            self.translateAndWrite(s)
            s = f.readline()
        f.close()
        self.writeLine('\n')
        self.writeLine('}')
        self.writeLine('\\end{document}')
        
    def writeProposalCover(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%%%%% Cover %%%%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\begin{center}')
        self.writeLine('{\\fontsize{30pt}{32pt}\\selectfont\\bfseries ข้อเสนอโครงงานวิศวกรรมคอมพิวเตอร์}')
        self.writeLine('')
        self.write('{\\bfseries ')
        self.writeLine('เรื่อง')
        self.writeLine('')
        self.writeLine(information['NAMETH'])
        self.writeLine('')
        self.writeLine(information['NAMEEN'])
        self.writeLine('\\vfill')
        self.writeLine('โดย')
        self.writeLine('')
        self.write(information['AUTHORTH'][0])
        for author in information['AUTHORTH'][1:]:
            self.writeLine('\\\\')
            self.write(author)
        self.writeLine('')
        self.writeLine('\\vfill')
        self.writeLine('ในที่ปรึกษาของ')
        self.writeLine('')
        self.writeLine('อาจารย์' + information['ADVISORTH'].split(',')[0])
        self.writeLine('')
        self.writeLine('สาขาวิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ศรีราชา\\\\')
        self.writeLine('มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตศรีราชา\\\\')
        self.writeLine('พ.ศ. \\thisYear')
        self.writeLine('}')
        self.writeLine('\\end{center}')
        self.writeLine('')
        
    def writeReportMainCover(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%% Main Cover %%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\begin{center}')
        self.writeLine('\\includegraphics[scale=0.25]{ku_black.jpg}')
        self.writeLine('')
        self.writeLine('{\\fontsize{35pt}{37pt}\\selectfont\\bfseries โครงงานวิศวกรรมคอมพิวเตอร์}')
        self.writeLine('')
        self.writeLine('\\vspace{0.3in}')
        self.writeLine('{\\fontsize{20pt}{22pt}\\selectfont\\bfseries ' + information['NAMETH'])
        self.writeLine('')
        self.writeLine(information['NAMEEN'] + '}')
        self.writeLine('\\vfill')
        self.write('{\\fontsize{20pt}{22pt}\\selectfont\\bfseries ')
        for authorName in information['AUTHORTH']:
            self.writeLine(authorName + '\\\\')
        self.writeLine('}')
        self.writeLine('\\vfill')
        self.writeLine('{\\fontsize{20pt}{22pt}\\selectfont\\bfseries สาขาวิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ศรีราชา\\\\')
        self.writeLine('มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตศรีราชา\\\\')
        self.writeLine('พ.ศ. \\thisYear}\\\\')
        self.writeLine('\\end{center}')
        self.writeLine('')
    
    def writeReportInsideCover(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%% Inside Cover %%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\begin{center}')
        self.writeLine('โครงงานวิศวกรรมคอมพิวเตอร์')
        self.writeLine('')
        self.writeLine('เรื่อง')
        self.writeLine('')
        self.writeLine(information['NAMETH'])
        self.writeLine('')
        self.writeLine(information['NAMEEN'])
        self.writeLine('\\vfill')
        self.writeLine('โดย')
        self.writeLine('')
        self.write(information['AUTHORTH'][0])
        for author in information['AUTHORTH'][1:]:
            self.writeLine('\\\\')
            self.write(author)
        self.writeLine('')
        self.writeLine('\\vfill')
        self.writeLine('เสนอ')
        self.writeLine('')
        self.writeLine('สาขาวิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ศรีราชา\\\\')
        self.writeLine('มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตศรีราชา\\\\')
        self.writeLine('เพื่อความสมบูรณ์แห่งปริญญาวิศวกรรมศาสตรบัณฑิต (วิศวกรรมคอมพิวเตอร์)\\\\')
        self.writeLine('พ.ศ. \\thisYear')
        self.writeLine('\\end{center}')
        self.writeLine('')
   
    def writeApprovalForm(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%% Approval Form %%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\begin{center}')
        self.writeLine('\\textbf{ปริญญาวิศวกรรมศาสตรบัณฑิต (วิศวกรรมคอมพิวเตอร์)}')
        self.writeLine('')
        self.writeLine('\\textbf{สาขาวิชาวิศกรรมคอมพิวเตอร์ \\hfill คณะวิศวกรรมศาสตร์ศรีราชา}')
        self.writeLine('\\end{center}')
        self.writeLine('\\vfill')
        self.writeLine('\\begin{tabular}{ll}')
        self.writeLine('\\textbf เรื่อง & ' + information['NAMETH'] + ' \\\\')
        self.writeLine('& ' + information['NAMEEN'] + ' \\\\')
        self.writeLine('\\\\')
        self.write('\\textbf นามผู้จัดทำ & ' + information['AUTHORTH'][0])
        for author in information['AUTHORTH'][1:]:
            self.writeLine('\\\\')
            self.write('& ' + author)
        self.writeLine('')
        self.writeLine('\\end{tabular}')
        self.writeLine('\\vfill')
        self.writeLine('\\begin{center}')
        self.writeLine('\\begin{tabularx}{\\textwidth}{lX}')
        self.writeLine('\\textbf ได้รับพิจารณาเห็นชอบโดย & \\\\')
        self.writeLine('\\\\')
        self.writeLine('อาจารย์ที่ปรึกษาโครงงานหลัก & \\dotfill\\ \\\\')
        self.writeLine('& \\centerline{(อาจารย์' + information['ADVISORTH'].split(',')[0] +')} \\\\')
        self.writeLine('กรรมการโครงงานหลัก & \\dotfill\\ \\\\')
        self.writeLine('& \\centerline{(อาจารย์' + information['COMMITTEE1TH'] +')} \\\\')
        self.writeLine('กรรมการโครงงานรอง & \\dotfill\\ \\\\')
        self.writeLine('& \\centerline{(อาจารย์' + information['COMMITTEE2TH'] +')} \\\\')
        self.writeLine('\\end{tabularx}')
        self.writeLine('')
        self.writeLine('\\begin{tabularx}{\\textwidth}{Xc}')
        self.writeLine('& \\textbf{สาขาวิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ศรีราชา}\\\\')
        self.writeLine('& \\textbf{มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตศรีราชา รับรองแล้ว}\\\\')
        self.writeLine('& \\\\')
        self.writeLine('& \\dotfill\\ \\\\')
        self.writeLine('& (อาจารย์' + information['HEADDEPARTMENTTH'] +') \\\\')
        self.writeLine('& หัวหน้าสาขาวิชาวิศวกรรมคอมพิวเตอร์ \\\\')
        self.writeLine('& \\\\')
        self.writeLine('& วันที่ \\dotfill\\ \\\\')
        self.writeLine('\\end{tabularx}')
        self.writeLine('\\end{center}')
        self.writeLine('')
        
    def writeAbstractTH(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%% Abstract TH %%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\begin{quote}')
        for author in information['AUTHORTH']:
            self.write(author + ', ')
        self.write('\\thisYear: ')
        self.write(information['NAMETH'] + ', ')
        self.write('ปริญญาวิศวกรรมศาสตรบัณฑิต (วิศวกรรมคอมพิวเตอร์) สาขาวิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ศรีราชา, ')
        self.write('อาจารย์ที่ปรึกษาโครงงานหลัก: อาจารย์')
        self.write(information['ADVISORTH'] + ' ')
        self.writeLine('\\pageref{LastPage} หน้า')
        self.writeLine('\\end{quote}')
        self.writeLine('\\vspace{0.2in}')
        self.writeLine('\\begin{center}')
        self.writeLine('\\textbf{\\Huge บทคัดย่อ}')
        self.writeLine('\\end{center}')
        self.writeLine('\\vspace{0.3in}')
        self.writeLine('')
        self.writeLine('')
        self.write('\\hspace{-0.5in}')
        f = open(information['ABSTRACTTH'], 'r')
        s = f.readline()
        while s:
            self.translateAndWrite(s)
            s = f.readline()
        f.close()
        self.writeLine('\n')
        
              
    def writeAbstractEN(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%% Abstract EN %%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\begin{quote}')
        for author in information['AUTHOREN']:
            self.write(author + ', ')
        self.write('\\the\\year: ')
        self.write(information['NAMEEN'] + ', ')
        self.write('Bachelor of Engineering (Computer Engineering), Department of Computer Engineering, Faculty of Engineering at Siracha, ')
        self.write('Project Advisor: ')
        self.write(information['ADVISOREN'] + ' ')
        self.writeLine('\\pageref{LastPage} pages')
        self.writeLine('\\end{quote}')
        self.writeLine('\\vspace{0.2in}')
        self.writeLine('\\begin{center}')
        self.writeLine('\\textbf{\\Huge Abstract}')
        self.writeLine('\\end{center}')
        self.writeLine('\\vspace{0.3in}')
        self.writeLine('')
        self.writeLine('')
        self.write('\\hspace{-0.5in}')
        f = open(information['ABSTRACTEN'], 'r')
        s = f.readline()
        while s:
            self.translateAndWrite(s)
            s = f.readline()
        f.close()
        self.writeLine('\n')
        
    def writeAcknowledgement(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%% Acknowledgement %%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\chapter*{กิตติกรรมประกาศ}')
        self.writeLine('')
        f = open(information['ACKNOWLEDGEMENT'], 'r')
        s = f.readline()
        while s:
            self.translateAndWrite(s)
            s = f.readline()
        f.close()
        self.writeLine('\n')
        self.writeLine('\\begin{flushright}')
        for author in information['AUTHORTH']:
            self.writeLine(author + '\\\\')
        monthNum = datetime.datetime.now().month
        monthNames = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
        self.write(monthNames[monthNum - 1] + ' ')
        self.writeLine('\\thisYear')
        self.writeLine('\\end{flushright}')
        self.writeLine('')
        
    def writeTableOfContents(self):
        self.writeLine('%%%%%%%%%%%%%%%%%% Table of Contents %%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\pagenumbering{roman}')
        self.writeLine('\\tableofcontents')
        self.writeLine('\\listoftables')
        self.writeLine('\\listoffigures')
        self.writeLine('')
        
    def writeChapters(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%%% Contents %%%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\pagenumbering{arabic}')
        for chapter in information['CHAPTER']:
            self.writeChapter(chapter)
            
    def writeChapter(self, chapter):
        self.writeLine('%%%%%%%%%%%%%%%%% ' + chapter[0] + ' %%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\chapter{' + chapter[0] + '}')
        self.writeLine('')
        f = open(chapter[1], 'r')
        s = f.readline()
        while s:
            self.translateAndWrite(s)
            s = f.readline()
        f.close()
        self.writeLine('\n')
    
    def writeReferences(self):
        information = self.info
        bibfile = open(information['REFERENCE'], 'r')
        newbibfile = open(information['DOCUMENT'] + '_' + information['REFERENCE'], 'w')
        s = bibfile.readline()
        while s:
            newbibfile.write(self.thaicode(s))
            s = bibfile.readline()
        self.writeLine('%%%%%%%%%%%%%%%%%%%%% References %%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\newpage')
        self.writeLine('\\addcontentsline{toc}{chapter}{เอกสารและสิ่งอ้างอิง}')
        self.writeLine('\\bibliographystyle{plain}')
        self.writeLine('\\bibliography{' + information['DOCUMENT'] + '_' + information['REFERENCE'].split('.')[0] + '}')
        self.writeLine('')

                
    def writeAppendices(self):
        information = self.info
        self.writeLine('%%%%%%%%%%%%%%%%%%%%% Appendices %%%%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('\\appendix')
        for appendix in information['APPENDIX']:
            self.writeChapter(appendix)
        
    def writeEnding(self):
        self.writeLine('%%%%%%%%%%%%%%%%%%%% Document Ending %%%%%%%%%%%%%%%%%%%%%')
        self.writeLine('}')
        self.writeLine('\\end{document}')

class LatexCaller:
    def __init__(self, projectName, bibFile):
        self.projectName = projectName
        self.bibFile = bibFile
        
    def callXelatex(self, options):
        os.system('xelatex ' + self.projectName + '.tex')
        os.system('bibtex ' + self.projectName)
        os.system('xelatex ' + self.projectName + '.tex')
        os.system('xelatex ' + self.projectName + '.tex')
        supportingFiles = ['log', 'lot', 'lof', 'toc', 'tex', 'aux', 'bbl', 'blg', 'bib']
        for f in supportingFiles:
            if f not in options:
                if f == 'bib':
                    os.system('rm '+ self.projectName + '_' + self.bibFile)
                else:
                    os.system('rm ' + self.projectName + '.' + f)
  
class TexTranslator:
    def __init__(self, information):
        self.state = ['text']
        self.info = information
        
    def reset(self):
        self.state = ['text']
    
    def executeCommand(self):
        result = ''
        self.command = self.command.strip()
        if self.state[-1] == 'math':
            if self.command == 'end':
                result = '\\]\n'
                self.state.pop()
            else:
                result = '[[' + self.command + ']]'
        
        else:
            if self.command.startswith('title'):
                section = self.command[5:].strip()
                args = section.split('|')
                title = ''
                date = ''
                author = ''
                translator = TexTranslator(self.info)
                if args[0].startswith(':'):
                    title = translator.translate(args[0][1:].strip())
                for arg in args[1:]:
                    if arg.startswith('date'):
                        arg = arg[4:].strip()
                        if arg.startswith('='):
                            date = translator.translate(arg[1:].strip())
                    elif arg.startswith('author'):
                        arg = arg[6:].strip()
                        if arg.startswith('='):
                            author = translator.translate(arg[1:].strip())
                
                result =  '\\title{' + title + '}\n'
                if not (date == ''):
                    result = result + '\\date{' + date + '}\n'
                if not (author == ''):
                    result = result + '\\author{' + author + '}\n'
                result = result + '\\maketitle\n'
                
                
                    
            elif self.command.startswith('section'):
                section = self.command[7:].strip()
                label = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]
                    section = section[endLabel+1:].strip()
                if section[0] == ':':
                    nameTranslator = TexTranslator(self.info)
                    name = nameTranslator.translate(section[1:])
                    result = '\\section{' + name + '}\n'
                if not (label == ''):
                    result = result + '\\label{' + label + '}\n'
            elif self.command.startswith('subsection'):
                section = self.command[10:].strip()
                label = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]
                    section = section[endLabel+1:].strip()
                if section[0] == ':':
                    nameTranslator = TexTranslator(self.info)
                    name = nameTranslator.translate(section[1:])
                    result = '\\subsection{' + name + '}\n'
                if not (label == ''):
                    result = result + '\\label{' + label + '}\n'
            elif self.command.startswith('subsubsection'):
                section = self.command[13:].strip()
                label = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]
                    section = section[endLabel+1:].strip()
                if section[0] == ':':
                    nameTranslator = TexTranslator(self.info)
                    name = nameTranslator.translate(section[1:])
                    result = '\\subsubsection{' + name + '}\n'
                if not (label == ''):
                    result = result + '\\label{' + label + '}\n'
            elif self.command.startswith('ref'):
                section = self.command[3:].strip()
                label = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]           
                    result = result + '\\ref{' + label + '}'
            elif self.command.startswith('cite'):
                section = self.command[4:].strip()
                label = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]           
                    result = result + '\\cite{' + label + '}'
            elif self.command.startswith('image'):
                args = self.command.split('|')
                image = args[0]
                section = image[5:].strip()
                label = ''
                filename = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]
                    section = section[endLabel+1:].strip()
                if section[0] == ':':
                    filename = section[1:].strip()
                width = '1.0'
                caption = ''
                for arg in args[1:]:
                    if arg.startswith('width'):
                        section = arg[5:].strip()
                        if section[0] == '=':
                            width = section[1:]
                    elif arg.startswith('caption'):
                        section = arg[7:].strip()
                        if section[0] == '=':
                            caption = section[1:]
                if not (caption == ''):
                    result = '\\begin{figure}\n\\centering\n'
                result = result + '\\includegraphics[width=' + width + '\\textwidth]{' + filename + '}\n'
                if not (caption == ''):
                    result = result + '\\caption{' + caption + '}\n'
                if not (label == ''):
                    result = result + '\\label{' + label + '}\n'
                if not (caption == ''):
                    result = result + '\\end{figure}\n'
            
            elif self.command.startswith('bibliography'):
                section = self.command[12:].strip()
                if section[0] == ':':
                    filename = section[1:].strip()
                    information = self.info
                    bibfile = open(filename, 'r')
                    s = bibfile.readline()
                    writer = CodeWriter(information['PROJECT'] + '_' + 'reference.bib', {})
                    while s:
                        writer.writeLine(s)
                        s = bibfile.readline()
                    result = '%%%%%%%%%%%%%%%%%%%%% References %%%%%%%%%%%%%%%%%%%%%%%\n'      
                    result = result + '\\bibliographystyle{plain}\n'
                    result = result + '\\bibliography{' + information['PROJECT'] + '_' + 'reference' + '}\n'
                    
                
            elif self.command == 'name-th':
                result = self.info['NAMETH']
            elif self.command == 'name-en':
                result = self.info['NAMEEN']
            
            elif self.command.startswith('figure'):
                section = self.command[6:].strip()
                label = ''
                caption = ''
                if section[0] == '(':
                    endLabel = section.find(')')
                    label = section[1:endLabel]
                    section = section[endLabel+1:].strip()
                if section[0] == ':':
                    caption = section[1:]
                result = '\\begin{figure}\n\\centering\n'
                self.state.append('figure|' + label + '|' + caption)
            
            elif self.command == 'math':
                result = '\\['
                self.state.append('math')
            
            elif self.command.startswith('code'):
                args = self.command.split('|')
                mathEnable = False
                frame = False
                numbers = False
                for arg in args[1:]:
                    arg = arg.strip()
                    if arg.startswith('math'):
                        arg = arg[4:].strip()
                        if arg.startswith('=') and arg[1:].strip() == 'true':
                            mathEnable = True
                    elif arg.startswith('frame'):
                        arg = arg[5:].strip()
                        if arg.startswith('=') and arg[1:].strip() == 'true':
                            frame = True
                    elif arg.startswith('numbers'):
                        arg = arg[7:].strip()
                        if arg.startswith('=') and arg[1:].strip() == 'true':
                            numbers = True
                                                
                result = '\\begin{Verbatim}[fontfamily=tt'
                if frame:
                    result = result + ', frame=single'
                if numbers:
                    result = result + ', numbers=left'
                if mathEnable:
                    result = result + ', commandchars=\\\\\\{\\}, codes={\\catcode`$=3\\catcode`^=7\\catcode`_=8}'
                result = result + ']'
                self.state.append('code')
            
            elif self.command.startswith('table'):
                section = self.command[5:]
                format = ''
                label = ''
                caption = ''
                if section[0] == '[':
                    endFormat = section.find(']')
                    format = section[1:endFormat]
                    if len(section)>endFormat:
                        section = section[endFormat+1:].strip()
                if len(section)>0:
                    if section[0] == '(':
                        endLabel = section.find(')')
                        label = section[1:endLabel]
                        section = section[endLabel+1:].strip()
                    if section[0] == ':':
                        caption = section[1:]
                
                if not(caption == ''):
                    result = '\\begin{table}\n\\centering\n'
                    result = result + '\\caption{' + caption + '}\n'
                    if not (label == ''):
                        result = result + '\\label{' + label + '}\n'
                result = result + '\\begin{tabular}{' + format + '}'
                if not(caption == ''):
                    self.state.append('table')
                else:
                    self.state.append('tabular')
            
            elif self.command == 'list':
                result = '\\begin{enumerate}'
                self.state.append('list')
            elif self.command == 'ulist':
                result = '\\begin{itemize}'
                self.state.append('ulist')
            
            elif self.command == 'end':
                if self.state[-1].startswith('figure'):
                    args = self.state[-1].split('|')
                    label = args[1]
                    caption = args[2]
                    if not (caption == ''):
                        result = result + '\\caption{' + caption + '}\n'
                    if not (label == ''):
                        result = result + '\\label{' + label +'}\n'
                    result = result + '\\end{figure}\n'
                    self.state.pop()
                
                elif self.state[-1] == 'table':
                    result = '\\end{tabular}\n\\end{table}'
                    self.state.pop()
                
                elif self.state[-1] == 'tabular':
                    result = '\\end{tabular}'
                    self.state.pop()
                
                elif self.state[-1] == 'list':
                    result = '\\end{enumerate}'
                    self.state.pop()
                
                elif self.state[-1] == 'ulist':
                    result = '\\end{itemize}'
                    self.state.pop()
                    
        return result
                
        
        
    def translate(self, s):
        opusSpecialCharactors = ['*', '`', ':']
        result = ''
        for i in range(len(s)):
            c = s[i]
            if c == '"' and (i==0 or s[i-1] == ' '):
                c = '``'
            elif c == "'" and (i==0 or s[i-1] == ' '):
                c = '`'
                
            if self.state[-1] == 'backslash':
                if s[i] in opusSpecialCharactors:
                    result = result + c
                else:
                    result = result + '\\' + c
                self.state.pop()
                if s[i] == '[':
                    self.state.append('math')
                
            elif self.state[-1] == 'comment':
                if s[i] == '\n':
                    self.state.pop()
            
            elif self.state[-1] == 'openSquareBracket':
                if s[i] == '[':
                    self.state.append('command')
                    self.command = ''
                else:
                    self.state.pop()
                    result = result + '[' + c
            
            elif self.state[-1] == 'command':
                if s[i] == ']':
                    self.state.append('endCommand')
                elif s[i] == '[':
                    self.state.append('openSquareBracketInCommand')
                    self.command = self.command + c
                else:
                    self.command = self.command + c
            
            elif self.state[-1] == 'openSquareBracketInCommand':
                if s[i] == '[':
                    self.state.append('openSquareBracketInCommand')
                elif s[i] == ']':
                    self.state.pop()
                self.command = self.command + c
            
            elif self.state[-1] == 'endCommand':
                if s[i] == ']':
                    self.state.pop()
                    self.state.pop()
                    self.state.pop()
                    result = result + self.executeCommand()
                else:
                    self.state.pop()
                    self.command = self.command + ']' + c                   
                    
            elif self.state[-1] == 'text':
                if s[i] == '\\':
                    self.state.append('backslash')
                elif s[i] == '*':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\textbf{'
                        self.state.append('bold')
                    else:
                        result = result + c
                elif s[i] == '_':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\emph{'
                        self.state.append('emph')
                    else:
                        result = result + c
                elif s[i] == '%':
                    self.state.append('comment')
                elif s[i] == '`':
                    result = result + '{\\ttfamily\\verb`'
                    self.state.append('inlinecode')
                elif s[i] == '$':
                    result = result + '$'
                    self.state.append('inlinemath')
                elif s[i] == '[':
                    self.state.append('openSquareBracket')
                else:
                    result = result + c
            
            elif self.state[-1] in ['list', 'ulist']:
                if s[i] == '\\':
                    self.state.append('backslash')
                elif s[i] == '*':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\textbf{'
                        self.state.append('bold')
                    else:
                        result = result + c
                elif s[i] == '_':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\emph{'
                        self.state.append('emph')
                    else:
                        result = result + c
                elif s[i] == '%':
                    self.state.append('comment')
                elif s[i] == '`':
                    result = result + '{\\ttfamily\\verb`'
                    self.state.append('inlinecode')
                elif s[i] == '$':
                    result = result + '$'
                    self.state.append('inlinemath')
                elif s[i] == '[':
                    self.state.append('openSquareBracket')
                elif s[i] == '#':
                    result = result + '\\item '
                else:
                    result = result + c
            
            elif self.state[-1] in ['table', 'tabular']:
                if s[i] == '\\':
                    self.state.append('backslash')
                elif s[i] == '*':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\textbf{'
                        self.state.append('bold')
                    else:
                        result = result + c
                elif s[i] == '_':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\emph{'
                        self.state.append('emph')
                    else:
                        result = result + c
                elif s[i] == '%':
                    self.state.append('comment')
                elif s[i] == '`':
                    result = result + '{\\ttfamily\\verb`'
                    self.state.append('inlinecode')
                elif s[i] == '$':
                    result = result + '$'
                    self.state.append('inlinemath')
                elif s[i] == '[':
                    self.state.append('openSquareBracket')
                else:
                    result = result + c
            
            elif self.state[-1].startswith('figure'):
                if s[i] == '\\':
                    self.state.append('backslash')
                elif s[i] == '*':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\textbf{'
                        self.state.append('bold')
                    else:
                        result = result + c
                elif s[i] == '_':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\emph{'
                        self.state.append('emph')
                    else:
                        result = result + c
                elif s[i] == '%':
                    self.state.append('comment')
                elif s[i] == '`':
                    result = result + '{\\ttfamily\\verb`'
                    self.state.append('inlinecode')
                elif s[i] == '$':
                    result = result + '$'
                    self.state.append('inlinemath')
                elif s[i] == '[':
                    self.state.append('openSquareBracket')
                else:
                    result = result + c
            
            elif self.state[-1] == 'code':
                if s.find('[[end]]') == i:
                    result = result + '\\end{Verbatim}'
                    self.state.append('endCode')
                else:
                    result = result + s[i]
            elif self.state[-1] == 'endCode':
                if s.find('[[end]]') == i-6:
                    self.state.pop()
                    self.state.pop()
            
            elif self.state[-1] == 'bold':
                if s[i] == '\\':
                    self.state.append('backslash')
                elif s[i] == '*':
                    result = result + '}'
                    self.state.pop()
                elif s[i] == '_':
                    if i == 0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\emph{'
                        self.state.append('emph')
                    else:
                        result = result + c
                elif s[i] == '%':
                    self.state.append('comment')
                elif s[i] == '`':
                    result = result + '{\\ttfamily\\verb`'
                    self.state.append('inlinecode')
                elif s[i] == '$':
                    result = result + '$'
                    self.state.append('inlinemath')
                else:
                    result = result + c
                    
            elif self.state[-1] == 'emph':
                if s[i] == '\\':
                    self.state.append('backslash')
                elif s[i] == '*':
                    if i==0 or not (s[i-1].isalpha() or s[i-1].isdigit()):
                        result = result + '\\textbf{'
                        self.state.append('bold')
                    else:
                        result = result + c
                elif s[i] == '_':
                    result = result + '}'
                    self.state.pop()  
                elif s[i] == '%':
                    self.state.append('comment')
                elif s[i] == '`':
                    result = result + '{\\ttfamily\\verb`'
                    self.state.append('inlinecode')
                elif s[i] == '$':
                    result = result + '$'
                    self.state.append('inlinemath')
                else:
                    result = result + c
            
            elif self.state[-1] == 'inlinecode':
                if s[i] == '`':
                    result = result + '`}'
                    self.state.pop()
                else:
                    result = result + s[i]
            
            elif self.state[-1] == 'inlinemath':
                if s[i] == '\\':
                    self.state.append('inlinemathbackslash')
                elif s[i] == '$':
                    result = result + c
                    self.state.pop()
                else:
                    result = result + c
            
            elif self.state[-1] == 'inlinemathbackslash':
                result = result + '\\' + c
                self.state.pop()
            
            elif self.state[-1] == 'math':
                if s[i] == '\\':
                    self.state.append('mathbackslash')
                elif s[i] == '[':
                    self.state.append('openSquareBracket')
                else:
                    result = result + c
            
            elif self.state[-1] == 'mathbackslash':
                result = result + '\\' + c
                self.state.pop()
                
                if s[i] == ']':
                    self.state.pop()
            
        return result
            

source = sys.argv[1]
if source.endswith('.opus.project'):
    
    parser = ControllerParser(source)

    information = {}
    information['AUTHORTH'] = []
    information['AUTHOREN'] = []
    information['CHAPTER'] = []
    information['APPENDIX'] = []
    inADocument = False
    while(parser.hasMoreCommand()):
        command = parser.commandString()
        if command.startswith('document('):
            if not inADocument:
                information = {}
                projectName = command.split(':')[0].replace('document(','').replace(')','').strip()
                projectType = command.split(':')[1].strip()
                information['DOCUMENT'] = projectName
                information['TYPE'] = projectType
                information['AUTHORTH'] = []
                information['AUTHOREN'] = []
                information['CHAPTER'] = []
                information['APPENDIX'] = []
                inADocument = True
                
        elif command.startswith('end.'):       
            if inADocument:
                outputfile = information['DOCUMENT'] + '.tex'
                codeWriter = CodeWriter(outputfile, information)
    
                if information['TYPE']=='report':
                    codeWriter.writeReport()
                elif information['TYPE']=='proposal':
                    codeWriter.writeProposal()
                codeWriter.close()
                inADocument = False
                command = LatexCaller(information['DOCUMENT'], information['REFERENCE'])
                command.callXelatex([])
            
        elif command.startswith('name-th:'):
            if inADocument:
                information['NAMETH'] = command.replace('name-th:','').replace('\\:',':').strip()
        elif command.startswith('name-en:'):
            if inADocument:
                information['NAMEEN'] = command.replace('name-en:','').replace('\\:',':').strip()
        elif command.startswith('author-th:'):
            if inADocument:
                information['AUTHORTH'].append(command.replace('author-th:','').replace('\\:',':').strip())
        elif command.startswith('author-en:'):
            if inADocument:
                information['AUTHOREN'].append(command.replace('author-en:','').replace('\\:',':').strip())
        elif command.startswith('advisor-th:'):
            if inADocument:
                information['ADVISORTH'] = command.split('|')[0].replace('advisor-th:','').replace('\\:',':').strip() + ', ' + command.split('|')[1].replace('degree:','').strip()
        elif command.startswith('advisor-en:'):
            if inADocument:
                information['ADVISOREN'] = command.split('|')[0].replace('advisor-en:','').replace('\\:',':').strip() + ', ' + command.split('|')[1].replace('degree:','').strip()
        elif command.startswith('committee1-th:'):
            if inADocument:
                information['COMMITTEE1TH'] = command.replace('committee1-th:','').replace('\\:',':').strip()
        elif command.startswith('committee1-en:'):
            if inADocument:
                information['COMMITTEE1EN'] = command.replace('committee1-en:','').replace('\\:',':').strip()
        elif command.startswith('committee2-th:'):
            if inADocument:
                information['COMMITTEE2TH'] = command.replace('committee2-th:','').replace('\\:',':').strip()
        elif command.startswith('committee2-en:'):
            if inADocument:
                information['COMMITTEE2EN'] = command.replace('committee2-en:','').replace('\\:',':').strip()
        elif command.startswith('headdepartment-th:'):
            if inADocument:
                information['HEADDEPARTMENTTH'] = command.replace('headdepartment-th:','').replace('\\:',':').strip()
        elif command.startswith('headdepartment-en:'):
            if inADocument:
                information['HEADDEPARTMENTEN'] = command.replace('headdepartment-en:','').replace('\\:',':').strip()
            
        elif command.startswith('abstract-th:'):
            if inADocument:
                information['ABSTRACTTH'] = command.replace('abstract-th:','').replace('\\:',':').strip()   
        elif command.startswith('abstract-en:'):
            if inADocument:
                information['ABSTRACTEN'] = command.replace('abstract-en:','').replace('\\:',':').strip() 
        elif command.startswith('acknowledgement:'):
            if inADocument:
                information['ACKNOWLEDGEMENT'] = command.replace('acknowledgement:','').replace('\\:',':').strip()  
        elif command.startswith('reference:'):
            if inADocument:
                information['REFERENCE'] = command.replace('reference:','').replace('\\:',':').strip()  
        elif command.startswith('chapter('):
            if inADocument:
                chaptername = command.replace('chapter(', '').replace(')', '').split(':')[0].strip()
                chapterfile = command.replace('chapter(', '').replace(')', '').split(':')[1].strip()
                information['CHAPTER'].append((chaptername, chapterfile))
        elif command.startswith('appendix('):
            if inADocument:
                appendixname = command.replace('appendix(', '').replace(')', '').split(':')[0].strip()
                appendixfile = command.replace('appendix(', '').replace(')', '').split(':')[1].strip()
                information['APPENDIX'].append((appendixname, appendixfile))
    
    parser.close()
    
elif source.endswith('.opus'):
    projectname = source[:-5]
    outputfile = projectname + '.tex'
    codeWriter = CodeWriter(outputfile, {'SOURCE':source, 'PROJECT':projectname})
    codeWriter.writeNote()
    codeWriter.close()
    command = LatexCaller(projectname, 'reference.bib')
    command.callXelatex([])
