import csv
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from datetime import *
import os
import os.path
import psutil
import shutil
import time


root = Tk()
root.configure(bg='light yellow')
root.title('VMT BestFit Visu Offset updater_HU v1.00')
label = Label(root, text='Válaszd ki az ofszetfájlt(.txt formátum)',
              font=('Arial', 13, 'bold'), bg='light yellow')
label.pack()
exact_time = datetime.now()
final_logfilevar = exact_time.strftime('%Y-%d-%m_%H_%M_%S') + '.txt'

path_list_W177 = ["D:\BestFit\AuditTypes_Left\\010_W177_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\010_W177_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\010_W177_FA_RE.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\010_W177_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\010_W177_KH_RE.xml",
                  "D:\BestFit\AuditTypes_RT\\010_W177_ND_RT.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\011_W177_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\011_W177_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes\Type_W177\\11_W177_KV_LBR_Links.xml",
                  "D:\BestFit\AuditTypes\Type_W177\\11_W177_KV_LBR_Rechts.xml",
                  "D:\BestFit\AuditTypes_MH\\010_W177_MH.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\020_W177_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\020_W177_AMG_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\020_W177_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\021_W177_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\021_W177_AMG_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes\Type_W177_AMG\\12_W177_KV_LBR_Links_AMG.xml",
                  "D:\BestFit\AuditTypes\Type_W177_AMG\\12_W177_KV_LBR_Rechts_AMG.xml"
                  ]

path_list_C118 = ["D:\BestFit\AuditTypes_Left\\100_C118_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\100_C118_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\100_C118_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\100_C118_FA_RE.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\100_C118_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\100_C118_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\100_C118_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\101_C118_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\101_C118_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes\Type_C118\\21_C118_KV_LBR_Links.xml",
                  "D:\BestFit\AuditTypes\Type_C118\\21_C118_KV_LBR_Rechts.xml",
                  "D:\BestFit\AuditTypes_MH\\120_C118_AMG_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\121_C118_AMG_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\121_C118_AMG_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes\Type_C118_AMG\\22_C118_KV_LBR_Links_AMG.xml",
                  "D:\BestFit\AuditTypes\Type_C118_AMG\\22_C118_KV_LBR_Rechts_AMG.xml",
                  "D:\BestFit\AuditTypes_KH_Left\120_C118_AMG_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\120_C118_AMG_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\120_C118_AMG_MH.xml"                  
                 ]

path_list_X118 = ["D:\BestFit\AuditTypes_Left\\140_X118_FD_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\140_X118_FD_RE.xml",
                  "D:\BestFit\AuditTypes_Left\\140_X118_FA_LI.xml",
                  "D:\BestFit\AuditTypes_Right\\140_X118_FA_RE.xml",
                  "D:\BestFit\AuditTypes\\140_X118_ND_RT.xml",
                  "D:\BestFit\AuditTypes_KH_Left\\140_X118_KH_LI.xml",
                  "D:\BestFit\AuditTypes_KH_Right\\140_X118_KH_RE.xml",
                  "D:\BestFit\AuditTypes_MH\\140_X118_MH.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Left\\141_X118_STS_vo_li.xml",
                  "D:\BestFit\AuditTypes_STS_vo_Right\\141_X118_STS_vo_re.xml",
                  "D:\BestFit\AuditTypes\Type_X118\\31_X118_KV_LBR_Links.xml",
                  "D:\BestFit\AuditTypes\Type_X118\\31_X118_KV_LBR_Rechts.xml"
                  "D:\BestFit\AuditTypes_MH\\160_X118_AMG_MH.xml"
                  "D:\BestFit\AuditTypes_STS_vo_Left\\161_X118_AMG_STS_vo_li.xml"
                  "D:\BestFit\AuditTypes_STS_vo_Right\\161_X118_AMG_STS_vo_re.xml"
                  "D:\BestFit\AuditTypes\Type_X118_AMG\\32_X118_KV_LBR_Links_AMG.xml"
                  "D:\BestFit\AuditTypes\Type_X118_AMG\\32_X118_KV_LBR_Rechts_AMG.xml"
                  "D:\BestFit\AuditTypes_KH_Left\160_X118_AMG_KH_LI.xml"
                  "D:\BestFit\AuditTypes_KH_Right\160_X118_AMG_KH_RE.xml"
                  ]

existing_path_W177 = []
existing_path_C118 = []
existing_path_X118 = []
backup_pathlist = []
pointnames_got = []
values_got = []
xml_origdata = {}
csv_origdata = {}


def check_fileexists_W177():
    for file in path_list_W177:
        if os.path.exists(file):
            existing_path_W177.append(file)
            backup_pathlist.append(file)
        else:
            pass


def check_fileexists_C118():
    for file in path_list_C118:
        if os.path.exists(file):
            existing_path_C118.append(file)
            backup_pathlist.append(file)
        else:
            pass


def check_fileexists_X118():
    for file in path_list_X118:
        if os.path.exists(file):
            existing_path_X118.append(file)
            backup_pathlist.append(file)
        else:
            pass


def create_xml_backup():
    for file_path_W177 in existing_path_W177:
        shutil.copy2(str(file_path_W177), "D:\\BestFit\\BackupBestFit\\AbgleichBackup")

    for file_path_C118 in existing_path_C118:
        shutil.copy2(str(file_path_C118), "D:\\BestFit\\BackupBestFit\\AbgleichBackup")

    for file_path_X118 in existing_path_X118:
        shutil.copy2(str(file_path_X118), "D:\\BestFit\\BackupBestFit\\AbgleichBackup")

    backup_created = Label(root, bg='light yellow', fg='green', font=('Arial', 10, 'italic'),
                           text='Automatikus biztonsági mentés elkészült D:\BestFit\BackupBestFit\AbgleichBackup')
    backup_created.pack(anchor='s', pady=10)


def restore_xml_backup():
    ask_question = messagebox.askquestion('Figyelmeztetés', 'Valóban visszatöltöd a biztonsági másolatot?')
    if ask_question == 'yes':
        backup_files = os.listdir("D:\\BestFit\\BackupBestFit\\AbgleichBackup")

        for file_path, backup_path in zip(backup_files, backup_pathlist):
            shutil.copy2("D:\\BestFit\\BackupBestFit\\AbgleichBackup" + file_path, backup_path)

        open_button_W177["state"] = "normal"
        open_button_W177['font'] = ('Arial', 29, 'bold')
        open_button_W177["text"] = "Open W177 file"
        open_button_W177["bd"] = 10
        open_button_C118["state"] = "normal"
        open_button_C118["text"] = "Open C118 file"
        open_button_C118['font'] = ('Arial', 30, 'bold')
        open_button_C118["bd"] = 10
        open_button_X118["state"] = "normal"
        open_button_X118["text"] = "Open X118 file"
        open_button_X118['font'] = ('Arial', 30, 'bold')
        open_button_X118["bd"] = 10
        backup_button['state'] = 'disabled'
        messagebox.showinfo("Sikeres helyreállítás", "Biztonsági mentés sikeresen visszatöltve. MINDEN offset az eredeti értékre állítva!")


def start_program_W177():
    while True:
        csv_rawdata = []
        rawdata_chars = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_file(), 'r') as csv_file:
                reader = csv.reader(csv_file)
                for n in reader:
                    csv_rawdata.append(n)
        except TypeError:
            break

        try:
            for n in csv_rawdata:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    rawdata_chars.append(strg_replace)

                # Converting unwanted characters to readable/necessary ones
            for n in rawdata_chars:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                csv_origdata[name_puff] = value_puff

        except Exception:
            messagebox.showerror('Érvénytelen fájl', 'Kérlek válaszd ki a típusnak megfelelö fájlt')
            break

        if "W177" in str(csv_file):
            for file_path in existing_path_W177:
                setmeasurement_pointc118(file_path)
            open_button_W177["text"] = "W177 offszetelve"
            open_button_W177['font'] = ('Arial', 20, 'italic')
            open_button_W177["state"] = "disabled"
            backup_button['state'] = 'normal'

            break

        else:
            messagebox.showerror('Érvénytelen', 'Kérlek válaszd ki a típusnak megfelelö fájlt')


def start_program_C118():
    while True:
        csv_rawdata = []
        rawdata_chars = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_file(), 'r') as csv_file:

                reader = csv.reader(csv_file)
                for n in reader:
                    csv_rawdata.append(n)
        except Exception:
            break

        try:
            for n in csv_rawdata:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    rawdata_chars.append(strg_replace)

                # Converting unwanted characters to readable/necessary ones
            for n in rawdata_chars:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                csv_origdata[name_puff] = value_puff

        except Exception:
            messagebox.showerror('Érvénytelen fájl', 'Kérlek válaszd ki a típusnak megfelelö fájlt')
            break

        if "C118" in str(csv_file):
            for file_path in existing_path_C118:
                setmeasurement_pointc118(file_path)
            open_button_C118["text"] = "C118 offszetelve"
            open_button_C118['font'] = ('Arial', 20, 'italic')
            open_button_C118["state"] = "disabled"
            backup_button['state'] = 'normal'
            break
        else:
            messagebox.showerror('Érvénytelen fájl', 'Kérlek válaszd ki a típusnak megfelelö fájlt')


def start_program_X118():
    while True:
        csv_raw_data = []
        raw_data_chars = []
        final_list = []
        list_tostrg = ''
        try:
            with open(open_file(), 'r') as csv_file:

                reader = csv.reader(csv_file)
                for n in reader:
                    csv_raw_data.append(n)
        except Exception:
            break

        try:
            for n in csv_raw_data:
                for character in n:
                    list_tostrg += character
                    strg_replace = list_tostrg.replace(";", ".", 1)
                    list_tostrg = ""
                    raw_data_chars.append(strg_replace)

            for n in raw_data_chars:
                list_tostrg += n
                strg_replace2 = list_tostrg.replace(";", "=")
                final_list.append(strg_replace2)
                list_tostrg = ""

            for item in final_list:
                getindex = item.index("=")
                name_puff = item[:getindex]
                value_puff = item[getindex + 1:]
                csv_origdata[name_puff] = value_puff

        except Exception:
            messagebox.showerror('Érvénytelen fájl', 'Kérlek válaszd ki a típusnak megfelelö fájlt')
            break

        if "X118" in str(csv_file):
            for file_path in existing_path_X118:
                setmeasurement_pointc118(file_path)
            open_button_X118["text"] = "X118 offsetelve"
            open_button_X118['font'] = ('Arial', 20, 'italic')
            open_button_X118["state"] = "disabled"
            backup_button['state'] = 'normal'
            break

        else:
            messagebox.showerror('Érvénytelen fájl', 'Kérlek válaszd ki a típusnak megfelelö fájlt')


def ask_include():
    ask_includexml = messagebox.askquestion("Figyelmeztetés", "Érvényesítetted (include) az XML fájlt ?")
    if ask_includexml == "yes":
       return "yes" 
    else:
       return "no"
             
 
def kill_visu_start_bf():
    visu = "BestFitVisu.exe"
    
    for proc in psutil.process_iter():
        if proc.name() == visu:
            proc.kill()
            
    while True:    
        for proc in psutil.process_iter():
            if proc.name() == visu:
                messagebox.showerror("Figyelmeztetés", "Kérlek várj amíg a BestFitVisu.exe bezár") 
                time.sleep(3)
            else:
                os.startfile("D://BestFit//BestFit.exe")
                break
              

def exit_program():
    if ask_include() == "yes":
       kill_visu_start_bf()
       root.destroy()
       exit()
    else:
        messagebox.showinfo("Figyelmeztetés", "Kérlek érvényesítsd az XML fájt.")    
        

def open_file():
    filepath = filedialog.askopenfilename(title='Válaszd ki a  .txt fájlt', filetypes=(("txt files", "*.txt"),
                                                                                   ("all files", "*.*")))
    if filepath:
        return str(filepath)


def value_popup(pname, pvalue):
    return messagebox.showinfo('Érték magas', f'FIGYELEM! Több mint 1.00mm offset: {pname}:{pvalue},'
                                                f' kérlek ellenörizd, hogy helyes-e')


def setmeasurement_pointc118(document):
    tree = ET.parse(document)
    root = tree.getroot()
    for element in root.findall('.//Container'):
        if 'ValueConfig' in element.get('name') or 'ValueEvalConf' in element.get('name'):

            for subelement in element:

                get_tagName = subelement.get('name')
                get_pointname = subelement.get('value')

                if get_tagName == 'MeasurementPosition':
                    pointnames_got.append(get_pointname)

                if get_tagName == 'Offset':
                    values_got.append(get_pointname)

    for element in pointnames_got:
        if len(pointnames_got) > 0:
            xml_origdata[element] = values_got[0]
            values_got.pop(0)

    calculated_keyvalues = {key: float(csv_origdata.get(key, 0)) + float(xml_origdata.get(key, 0))
                            for key in xml_origdata
                            }

    final_list = [round(item, 2) for item in calculated_keyvalues.values()]
    final_strlist = [str(e) for e in final_list]
    final_keylist = [e for e in calculated_keyvalues.keys()]
    curr_date = date.today()
    currtext = 'Offset_update_log_' + str(curr_date) + '.txt'

    for element in root.iter('Double'):
        get_tagName = element.get('name')
        get_pointValue = element.get('value')

        if get_tagName == 'Offset' and len(final_strlist) > 0:
            element.set('value', str(final_strlist[0]))

            result = float(get_pointValue) - float(element.get('value'))
            if abs(result) > 1:
                value_popup(final_keylist[0], result)
                
            with open(currtext, 'a+') as logfile:
                logfile.write(f'\nOffset {final_keylist[0]} updated from {get_pointValue} to {element.get("value")}'
                              f' in:\n {document}\n')
                
            with open(final_logfilevar, 'a+') as logfile_2:
                logfile_2.write(f'\nOffset {final_keylist[0]} updated from {get_pointValue} to {element.get("value")}'
                                f'in:\n {document} \n')

            final_strlist.pop(0)
            final_keylist.pop(0)

    with open(currtext, 'r+') as log:
        read = log.read()
        log.truncate(0)

    messagebox.showinfo('Log notification', f' {read} ')
    pointnames_got.clear()
    values_got.clear()
    xml_origdata.clear()
    tree.write(document)


def on_enter_W177(e):
    if open_button_W177['state'] == 'normal':
        open_button_W177['background'] = 'light green'


def on_leave_W177(e):
    open_button_W177['background'] = 'SystemButtonFace'


def on_enter_C118(e):
    if open_button_C118['state'] == 'normal':
        open_button_C118['background'] = 'light green'


def on_leave_C118(e):
    open_button_C118['background'] = 'SystemButtonFace'


def on_enter_X118(e):
    if open_button_X118['state'] == 'normal':
        open_button_X118['background'] = 'light green'


def on_leave_X118(e):
    open_button_X118['background'] = 'SystemButtonFace'


def on_enter_exit(e):
    exit_button['background'] = '#F06868'


def on_leave_exit(e):
    exit_button['background'] = 'SystemButtonFace'


def on_enter_backup(e):
    if backup_button['state'] == 'normal':
        backup_button['background'] = 'light green'


def on_leave_backup(e):
    backup_button['background'] = 'SystemButtonFace'


check_fileexists_W177()
check_fileexists_C118()
check_fileexists_X118()


frame1 = Frame(root, bg='black')
frame1.pack()
open_button_W177 = Button(frame1, text='W117 fájl megnyitás', font=('Arial', 29, 'bold'), bd='10',
                          command=start_program_W177, )
open_button_W177.pack(padx=2, pady=2)
open_button_W177.bind("<Enter>", on_enter_W177)
open_button_W177.bind("<Leave>", on_leave_W177)

frame2 = Frame(root, bg='black')
frame2.pack()
open_button_C118 = Button(frame2, text='C118 fájl megnyitás', font=('Arial', 30, 'bold'), bd='10',
                          command=start_program_C118)
open_button_C118.pack(padx=2, pady=1)
open_button_C118.bind("<Enter>", on_enter_C118)
open_button_C118.bind("<Leave>", on_leave_C118)

frame3 = Frame(root, bg='black')
frame3.pack()
open_button_X118 = Button(frame3, text='X118 fájl megnyitás', font=('Arial', 30, 'bold'), bd='10',
                          command=start_program_X118)
open_button_X118.pack(padx=2, pady=2)
open_button_X118.bind("<Enter>", on_enter_X118)
open_button_X118.bind("<Leave>", on_leave_X118)
create_xml_backup()
backup_button = Button(root, text='Bizt.mentés betöltés', font=('Arial', 15), command=restore_xml_backup,
                       state='disabled')
backup_button.pack()
backup_button.bind("<Enter>", on_enter_backup)
backup_button.bind("<Leave>", on_leave_backup)

exit_button = Button(root, text="Kilépés", font=("Arial", 15), command=exit_program)
exit_button.pack(pady=30)
exit_button.bind("<Enter>", on_enter_exit)
exit_button.bind("<Leave>", on_leave_exit)

watermark = Label(root, text='<<<Created by ZMESTER>>>',
                  font=('Arial', 10, 'italic'), bg='light yellow')
watermark.pack(anchor='s')
watermark2 = Label(root, text='371_Kecskemet_Rohbau_Einführung', font=('Arial', 10), bg='light yellow')
watermark2.pack(anchor='s')


root.mainloop()
