import wmi
import psutil
import platform

HARDWARE = wmi.connect()


def bytes_conversion(value):
    """字节换算,默认转化成MB"""
    conversion = int(value) / (1024 * 1024)
    return str(conversion)


def get_cpu_msg():
    """获取当前电脑CPU信息"""
    cpu_msg = {}
    cpu = HARDWARE.Win32_Processor()
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
    disk = HARDWARE.Win32_DiskDrive()
    for i in disk:
        total_size = float(bytes_conversion(value=i.Size)) / 1024 / 1024
        disk_msg['磁盘产品'] = i.Model + i.Manufacturer
        disk_msg['磁盘总容量'] = '{:.3f}T'.format(total_size)
    return disk_msg


def get_network():
    """获取当前电脑网卡信息"""
    network_msg = {}
    network = HARDWARE.Win32_NetworkAdapterConfiguration(IPFilterSecurityEnabled=False)
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
    memory = HARDWARE.Win32_PhysicalMemory()
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
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    current_Hz = f'{cpu_freq.current / 1000 :.2f}GHz'
    max_Hz = f'{cpu_freq.max / 1000 :.2f}GHz'
    min_Hz = f'{cpu_freq.min / 1000 :.2f}GHz'
    percent = f'{cpu_percent}%'
    cpu_msg['使用率'] = percent
    cpu_msg['当前频率'] = current_Hz
    cpu_msg['最大频率'] = max_Hz
    cpu_msg['最小频率'] = min_Hz
    return cpu_msg


def real_get_memory():
    """实时读取当前电脑内存消耗情况"""
    memory_msg = {}
    real_memory_msg = psutil.virtual_memory()
    memory_msg['容量'] = '{:.3f}GB'.format(float(bytes_conversion(real_memory_msg.total)) / 1024)
    memory_msg['空闲'] = '{:.3f}GB'.format(float(bytes_conversion(real_memory_msg.free)) / 1024)
    memory_msg['使用率'] = '{}%'.format(real_memory_msg.percent)
    memory_msg['占用'] = '{:.3f}GB'.format(float(bytes_conversion(real_memory_msg.used)) / 1024)
    return memory_msg


def real_get_disk(path='./'):
    # 默认当前路径的磁盘大小
    """实时获取当前电脑磁盘使用情况"""
    disk_msg = {}
    disk_partition = psutil.disk_partitions(all=True)
    for partition in disk_partition:
        disk_msg[partition.device.replace('\\', '')] = partition.fstype

    for k, v in disk_msg.items():
        real_disk_msg = psutil.disk_usage(k)
        total_size = '{:.3f}GB'.format(float(bytes_conversion(real_disk_msg.total)) / 1024)
        used = '{:.3f}GB'.format(float(bytes_conversion(real_disk_msg.used)) / 1024)
        free = '{:.3f}GB'.format(float(bytes_conversion(real_disk_msg.free)) / 1024)
        percent = real_disk_msg.percent
        disk_msg[k] = '总容量:{}, 已使用:{}, 未使用:{}, 使用率:{}%'.format(total_size, used, free, percent)
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



