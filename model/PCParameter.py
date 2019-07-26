import wmi
import psutil
import platform


def bytes_conversion(value):
    """字节换算,默认转化成MB"""
    conversion = value / (1024 * 1024)
    return str(conversion)


def get_cpu_msg():
    """获取当前电脑CPU信息"""
    cpu_msg = {}
    y = wmi.WMI()
    cpu = y.Win32_Processor()
    for i in cpu:
        cpu_msg["名称"] = i.Name
        cpu_msg["核心数"] = i.NumberOfCores
        cpu_msg["位数"] = i.DataWidth
        cpu_msg['最大速度'] = i.MaxClockSpeed
        cpu_msg['缓存数'] = i.ProcessorType
        cpu_msg['一级缓存数'] = i.L2CacheSize
        cpu_msg['二级缓存数'] = i.L3CacheSize
        cpu_msg["系统位数"] = i.SystemCreationClassName
        cpu_msg["电脑名称"] = i.SystemName
    return cpu_msg


def get_disk_msg():
    """获取当前电脑disk信息"""
    disk_msg = {}
    y = wmi.WMI()
    disk = y.Win32_DiskDrive()
    for i in disk:
        disk_msg['品牌'] = i.Caption.rstrip()
        disk_msg['型号'] = y.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip()
        disk_msg['容量'] = bytes_conversion(int(i.Size) / 1024 / 1024)[:-14] + 'TB'
    return disk_msg


def get_network():
    """获取当前电脑网卡信息"""
    network_msg = {}
    y = wmi.WMI()
    network = y.Win32_NetworkAdapterConfiguration(IPEnabled=1)
    for i in network:
        network_msg['ip地址'] = i.IPAddress[0]
        network_msg['子网掩码'] = i.IPSubnet[0]
        network_msg['MAC地址'] = i.MACAddress
        network_msg['网关地址'] = i.DHCPServer
        network_msg['DNS地址'] = i.DNSServerSearchOrder
        network_msg['网卡类别'] = i.Description
    return network_msg


def get_memory():
    """获取当前电脑内存信息"""
    memory_msg = {}
    y = wmi.WMI()
    memory = y.Win32_PhysicalMemory()
    for i in memory:
        memory_msg['条数'] = i.BankLabel.split(' ')[1]
        memory_msg['容量'] = bytes_conversion(int(i.Capacity) / 1024) + 'GB'
        memory_msg['位数'] = i.DataWidth
        memory_msg['型号'] = i.PartNumber.strip()
        memory_msg['频率'] = str(i.Speed) + 'MHz'
        memory_msg['厂家'] = i.Manufacturer
    return memory_msg


def real_get_cpu_msg():
    """实时获取当前电脑cpu使用情况"""
    cpu_msg = {}
    y = str(psutil.cpu_percent(interval=1,percpu=True)).split(',')[2]
    k = str(psutil.cpu_freq(percpu=True)).split('(')[1].split(')')[0].split('=')[1].split(',')[0]
    p = str(psutil.cpu_times_percent(interval=1,percpu=True))[1:-1].split('(')[1].split(')')[0]
    cpu_msg['使用率'] = y + '%'
    cpu_msg['当前频率'] = k + 'Hz'
    cpu_msg['用户占用率'] = p.split('=')[1].split(',')[0] + '%'
    cpu_msg['系统占用率'] = p.split('=')[2].split(',')[0] + '%'
    cpu_msg['空闲值'] = p.split('=')[3].split(',')[0] + '%'
    return cpu_msg


def real_get_memory():
    """实时读取当前电脑内存消耗情况"""
    memory_msg = {}
    y = str(psutil.virtual_memory()).split('(')[1].split(')')[0].split('=')
    memory_msg['容量'] = bytes_conversion(int(y[1].split((','))[0]) / 1024)[:-13] + 'GB'
    memory_msg['空闲'] = bytes_conversion(int(y[2].split(',')[0]) / 1024)[:-13] + 'GB'
    memory_msg['使用率'] = y[3].split(',')[0] + '%'
    memory_msg['占用'] = bytes_conversion(int(y[4].split(',')[0]) / 1024)[:-13] + 'GB'
    return memory_msg


def real_get_disk(path='./'):
    # 默认当前路径的磁盘大小
    """实时获取当前电脑磁盘使用情况"""
    disk_msg = {}
    y = str(psutil.disk_usage(path)).split('(')[1].split(')')[0].split('=')
    disk_msg['容量'] = bytes_conversion(int(y[1].split(',')[0]) / 1024 )[:-13] + 'GB'
    disk_msg['已使用量'] = bytes_conversion(int(y[2].split(',')[0]) / 1024)[:-13] + 'GB'
    disk_msg['剩余量'] = bytes_conversion(int(y[3].split(',')[0]) / 1024)[:-11] + 'GB'
    disk_msg['使用率'] = y[4] + '%'
    return disk_msg


def real_get_network():
    """实时读取网卡使用情况"""
    network_msg = {}
    network = psutil.net_io_counters()
    network_msg['网卡最大上行'] = bytes_conversion(network.packets_sent)[:-12] + 'MB'
    network_msg['网卡最大下行'] = bytes_conversion(network.packets_recv)[:-12] + 'MB'
    return network_msg


def real_get_system():
    """读取当前电脑系统"""
    system_msg = {}
    system_msg['电脑名称'] = platform.node()
    system_msg['操作系统'] = platform.platform()
    system_msg['操作系统位数'] = platform.architecture()
    system_msg['计算机类型'] = platform.machine()
    return system_msg


def merge_config_info():
    """实时合并当前电脑下的所有参数"""
    MSG = []
    MSG.append(real_get_cpu_msg())
    MSG.append(real_get_system())
    MSG.append(real_get_disk())
    MSG.append(real_get_memory())
    MSG.append(real_get_network())
    return MSG


def merge_config_msg():
    """固定合并当前电脑下的所有参数"""
    MSG = []
    MSG.append(get_cpu_msg())
    MSG.append(real_get_system())
    MSG.append(get_network())
    MSG.append(get_disk_msg())
    MSG.append(get_memory())
    return MSG


def output_python_version():
    """输出python版本号"""
    version = platform.python_version()
    return version


if __name__ == '__main__':
    # print(merge_config_info())
    print(merge_config_msg())
