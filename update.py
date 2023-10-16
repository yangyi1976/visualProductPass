import json
import sys
import time, os
import requests
from PyQt5.QtWidgets import QMessageBox, QApplication

from updateDialog import UpdateDlg


def get_remote_version(url):
    """获取远程数据"""
    try:
        header = {'Content-type': 'application/json'}
        request = requests.get(url=url, headers=header)  # 请求处理
        remoteVer = request.json()  # 读取结果
        return remoteVer
    except requests.RequestException as e:
        raise Exception("连接更新服务器异常！%s" % str(e))


def read_local_version():
    if not os.path.exists("version.json"):
        msgbox = QMessageBox(QMessageBox.Critical, "错误", "本地版本文件丢失，")
        msgbox.exec()
        raise Exception("本地版本文件丢失")
    with open("version.json", mode='r', encoding='utf-8') as j:
        return json.load(j)


def create_file(url, file_name,directory):
    """下载并创建文件"""
    temp_size = 0
    createOk=False
    try:
        if directory !="":
            if not os.path.exists(directory):
                os.mkdir(directory)
            file = directory + "\\" + file_name
        else:
            file = file_name
        # 更新替换文件前需停止待更新程序

        if file_name=="main.exe":
            os.system('taskkill /f /t /im %s' % file_name)
        if not url:
            return "function:create_file(url,file_name) >>url is null"
        url=url+"?filename=%s" %file_name
        r = get_data_by_url(url)
        context_length = int(r.headers['Content-Length'])  # downdload data length
        updateDlg.show()
        with open(file, "wb+") as f:
            updateDlg.ui.lbFileName.setText(file_name)
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    temp_size += len(chunk)
                    percent = (temp_size / context_length) * 100
                    updateDlg.ui.progressBar.setValue(int(percent))  # diisplay download process
                f.flush()
            # f.close()
        updateDlg.close()
    except IOError:
        return "cannot open url",createOk
    except Exception as e:
        return "download file fail>>%s" % str(e),createOk
    createOk=True
    return "success",createOk


def run_exe(file_name):
    """启动程序"""
    os.system('start "" "%s"' % file_name)


def get_data_by_url(url):
    """获取远程数据"""
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }  # 头部信息
    r = requests.get(url, stream=True)
    return r


def write_version_json(data):
    """更新写入版本文件"""
    with open('version.json', 'w') as f:
        json.dump(data, f,indent=4)       #indent=4 格式化，缩进4


def write_log(text):
    """记录日志"""
    with open('update.log', mode='a', encoding='utf-8') as f:
        logtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(logtime + "\t" + text + "\n")


def run():
    while True:
        try:
            local_json = read_local_version()
            url=local_json.get("update_url")
            online_json = get_remote_version(url+"?filename=version.json")

            if online_json == local_json:
                # sleep 1 hour
                time.sleep(3600)
                continue
            for item in online_json:
                if local_json.get(item) and item!='update_url':  #item is update app file name
                    if online_json.get(item).get("version") > local_json.get(item).get("version"):
                        msg,updateOk=create_file(online_json.get('update_url'), item,online_json.get(item).get("dir"))
                        write_log("更新：%s 版本：%s->%s" % (item, local_json.get(item).get("version"),
                                                            online_json.get(item).get("version")))
                        write_log("更新结果：%s" % msg)
                        if updateOk is False:
                            return
                        if online_json.get(item).get("is_run")=="true":
                            run_exe(item)

                elif item=='update_url':    #item is 'update url'
                    if online_json.get(item)  != local_json.get(item) :
                        write_log("更新update地址：%s" % online_json.get(item))
                else:          # add new item
                    write_log(
                        "新增文件：%s ；版本: %s" % (item, online_json.get(item).get("version")))
                    msg, updateOk = create_file(online_json.get('update_url'), item,online_json.get(item).get("dir"))
                    write_log("新增结果：%s" % msg)
                    if updateOk is False:
                        return
                    if online_json.get(item).get("is_run")=="true":
                        run_exe(item)
            write_version_json(data=online_json)
            msgbox = QMessageBox(QMessageBox.Information, "系统更新", "系统升级成功，")
            msgbox.exec()
        except Exception as e:
            write_log("更新失败:"+str(e))
            msgbox = QMessageBox(QMessageBox.Information, "系统更新", "系统更新失败，%s" % str(e))
            msgbox.exec()
            raise e
        # sleep 1 hour
        time.sleep(3600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    updateDlg = UpdateDlg()
    run()

    sys.exit(app.exec_())

