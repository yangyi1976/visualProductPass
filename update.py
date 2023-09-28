import json
import time,os
import requests
from PyQt5.QtWidgets import QMessageBox

from updateDialog import UpdateDlg
def get_remote_version(url):
    """获取远程数据"""
    header = {'Content-type': 'application/json'}
    request = requests.get(url=url, headers=header)  # 请求处理
    remoteVer = request.json()  # 读取结果
    return remoteVer

def read_local_version(self):
    if not os.path.exists("version.json" ):
        QMessageBox.information(self, "错误", "本地版本信息丢失，" )
        return {}

    with open("%s/version.json", mode='r', encoding='utf-8') as j:
        return json.load(j)


def create_file(url, file_name):
    """下载并创建文件"""
    try:
        # if not os.path.exists(directory):
        #     os.mkdir(directory)
        # 更新替换文件前需停止待更新程序
        os.system('taskkill /f /t /im %s.exe' % file_name)
        if not url:
            return "url is null"
        f = get_data_by_url(url)
        updateDlg.close()
    except IOError:
        return "cannot open url"
    except Exception as e:
        return "fail"
    return "success"


def run_exe(file_name):
    """启动程序"""
    os.system('start "" "%s/%s.exe"' %  file_name)


def get_data_by_url(url):
    """获取远程数据"""
    temp_size=0
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }  # 头部信息
    r = requests.get(url, stream=True)
    context_length = int(r.headers['Content-Length'])  # downdload data length
    with open("file_path", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                temp_size += len(chunk)
                percent = (temp_size /context_length) * 100
                updateDlg.ui.progressBar.setValue(int(percent)) #diisplay download process
            f.flush()
        f.close()
    return f

def write_version_json(data):
    """更新写入版本文件"""
    with open('version.json', 'w') as f:
        json.dump(data, f)


def write_log(text):
    """记录日志"""
    with open('update.log' , mode='a', encoding='utf-8') as f:
        logtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(logtime + "\t" + text + "\n")



def run():
    while True:
        try:
            online_json = json.loads(get_remote_version("http://xxx/HboUpdateVersion.json"))
            local_json = read_local_version()
            if online_json == local_json:
                # sleep 1 hour
                time.sleep(3600)
                continue
            for program_name in online_json:
                if local_json.get(program_name):
                    if online_json.get(program_name).get("version") > local_json.get(program_name).get("version"):
                        write_log("更新：%s 版本：%s->%s" % (
                            program_name, local_json.get(program_name).get("version"),
                            online_json.get(program_name).get("version")))
                        write_log("更新地址：%s" % online_json.get(program_name).get("url"))
                        write_log("更新结果：%s" % create_file(online_json.get(program_name).get("url"), program_name))
                        if online_json.get(program_name).get("is_run"):
                            run_exe(program_name)
                else:
                    write_log(
                        "更新：%s 版本: %s" % (program_name, online_json.get(program_name).get("version")))
                    write_log("更新地址：%s" % online_json.get(program_name).get("url"))
                    write_log("更新结果：%s" % create_file(online_json.get(program_name).get("url"), program_name))
                    if online_json.get(program_name).get("is_run"):
                        run_exe(program_name)
            write_version_json(data=online_json)
        except Exception:
            write_log("更新失败")
    # sleep 1 hour
    time.sleep(3600)

if __name__ == '__main__':
    updateDlg=UpdateDlg()
    updateDlg.show()
    run()