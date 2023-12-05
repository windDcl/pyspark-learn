import datetime


def update_tb_table(a):
    # 假设tb是一个字典，其中key是id，value是一个包含status和update_time的列表
    tb = {
        1: {'status': 2, 'update_time': datetime.datetime(2023, 1, 1, 0, 0, 0)},
        2: {'status': 0, 'update_time': datetime.datetime(2023, 1, 1, 0, 0, 0)},
        # 可以根据实际情况初始化其他数据
    }

    for id, data in tb.items():
        current_status = data['status']
        current_update_time = data['update_time']

        if 20 < a < 30:
            new_status = 1
        elif a >= 30:
            new_status = 2
        else:
            new_status = 0

        if current_status != 0 and a <= 20:
            # 如果当前状态不为0且a<=20，表示需要恢复，更新update_time为当前时间，status=0
            tb[id] = {'status': 0, 'update_time': datetime.datetime.now()}
        else:
            tb[id] = {'status': new_status, 'update_time': datetime.datetime.now()}

    return tb


# 测试程序
a_value = 10  # 替换为实际的a值
updated_tb = update_tb_table(a_value)
print(updated_tb)
