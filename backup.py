# -*- coding:gbk -*-
import os
import time
import subprocess
import shutil

# 数据库
db = '127.0.0.1:1521/orcl'

# 用户
user = 'home_school'

# 导出用户
owner = 'home_school'

# 密码
psw = '123456'

# 备份保存路径
save_path = 'E:/databak'

# 云盘目录地址
yun_path = 'D:/百度云'

# 压缩包密码
zip_psw = 'abcd'


def proc():
    """
    调用Oracle备份命令和7z加密压缩命令
    需要提前将Oracle和7zip压缩软件加入环境变量
    """
    print '开始导出Oracle备份文件......'
    time_str = time.strftime('%Y%m%d')

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    file_name = save_path + '/' + time_str + '.dmp'
    log_name = save_path + '/' + time_str + '.log'
    bak_command = 'exp ' + user + '/' + psw + '@' + db + ' file=' + file_name + ' log=' + log_name + ' owner=' + owner

    subprocess.call(bak_command, shell=True)

    print '开始加密压缩Oracle备份文件......'

    zip_file_name = save_path + '/' + time_str + '.7z'
    zip_source = save_path + '/' + time_str + '.*'
    zip_command = '7z a ' + zip_file_name + ' ' + zip_source + ' -x!*.7z' + ' -p' + zip_psw

    subprocess.call(zip_command, shell=True)

    print '开始云备份文件......'
	
    os.remove(file_name)
    os.remove(log_name)
    shutil.copy(zip_file_name,yun_path)
	
    print '数据备份工作完成！'



if __name__ == '__main__':
    proc()