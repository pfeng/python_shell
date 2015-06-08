# -*- coding:gbk -*-
import os
import time
import subprocess
import shutil

# ���ݿ�
db = '127.0.0.1:1521/orcl'

# �û�
user = 'home_school'

# �����û�
owner = 'home_school'

# ����
psw = '123456'

# ���ݱ���·��
save_path = 'E:/databak'

# ����Ŀ¼��ַ
yun_path = 'D:/�ٶ���'

# ѹ��������
zip_psw = 'abcd'


def proc():
    """
    ����Oracle���������7z����ѹ������
    ��Ҫ��ǰ��Oracle��7zipѹ��������뻷������
    """
    print '��ʼ����Oracle�����ļ�......'
    time_str = time.strftime('%Y%m%d')

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    file_name = save_path + '/' + time_str + '.dmp'
    log_name = save_path + '/' + time_str + '.log'
    bak_command = 'exp ' + user + '/' + psw + '@' + db + ' file=' + file_name + ' log=' + log_name + ' owner=' + owner

    subprocess.call(bak_command, shell=True)

    print '��ʼ����ѹ��Oracle�����ļ�......'

    zip_file_name = save_path + '/' + time_str + '.7z'
    zip_source = save_path + '/' + time_str + '.*'
    zip_command = '7z a ' + zip_file_name + ' ' + zip_source + ' -x!*.7z' + ' -p' + zip_psw

    subprocess.call(zip_command, shell=True)

    print '��ʼ�Ʊ����ļ�......'
	
    os.remove(file_name)
    os.remove(log_name)
    shutil.copy(zip_file_name,yun_path)
	
    print '���ݱ��ݹ�����ɣ�'



if __name__ == '__main__':
    proc()