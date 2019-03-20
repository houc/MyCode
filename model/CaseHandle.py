def data_handle(data=None, case=None):
    """
    :param data: 传入从数据库中查询出来的结果后提取开始时间、结束时间、用例最短最短耗时，用例最长耗时
    :return: 列表的形式进行返回对应数据【开始时间、结束时间、用例最短最短耗时，用例最长耗时，总用例数、错误数、失败数、成功数】
    """
    case_messages = {}  # 封装进行集体打包
    sql_data = []  # 用例执行的时间
    member = []  # 用例负责人
    error = []  # 用例错误错
    fail = []  # 用例失败
    success = []  # 用例成功
    skip_data = [] # 跳过用例
    skip_reason = [] # 跳过用例原因

    # =======================================处理数据库中的数据============================================
    print(data)
    if case is not None:
        for skip in case.skipped:
            for da in skip:
                if "test_" in str(da):
                    module = str(da).split('.')[1].split(')')[0]
                    is_case = str(da).split(' ')[0]
                    skip_data.append([None, None, module, is_case, None, None, "跳过", None, "跳过用例原因:%s",
                                      None, None, None, None])
                else:
                    skip_reason.append(da)
    if data is not None:
        for first_data in range(len(data)):
            _data = data[first_data]
            for second_data in range(len(_data)):
                if first_data == 0:
                    if second_data == 12:
                        case_messages['start_time'] = _data[second_data]
                if second_data == 6:
                    if _data[second_data] == "错误":
                        error.append(_data[second_data])
                    elif _data[second_data] == "成功":
                        success.append(_data[second_data])
                    elif _data[second_data] == "失败":
                        fail.append(_data[second_data])
                if second_data == 9:
                    sql_data.append(float(_data[second_data][:-1]))
                if second_data == 11:
                    member.append(_data[second_data])
                if first_data == len(data) - 1:
                    if second_data == 12:
                        case_messages['end_time'] = _data[second_data]
        if sql_data and member:
            case_messages["short_time"] = min(sql_data)
            case_messages["long_time"] = max(sql_data)
            case_messages["member"] = list(set(member))

    # =======================================处理用例统计数据=============================================

    case_messages["testsRun"] = len(error) + len(fail) + len(success)
    case_messages["errors"] = len(error)
    case_messages["failures"] = len(fail)
    case_messages["success"] = len(success)
    if case_messages:
        return case_messages


