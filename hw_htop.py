import psutil
from functools import wraps
import json


def save(name_file):
    '''
    This is decorator saved result function in JSON file,
    you need write name file with .json !!!
    For example: 'func_result.json'
    '''
    def saving(func):
        @wraps(func)
        def save_to_json():
            res = func()
            date_json = []
            date_json.append(res)
            with open(f'{name_file}', 'w') as file:
                json.dump(date_json, file)
            return res

        return save_to_json

    return saving            

# It's script mini version application htop

def info_cpu(): # It's function return information about your CPU 
    res_cpu = {}
    date_t = psutil.cpu_times() # It's modul output information about worktime 
    res_cpu.update(
                   user_time=date_t.user, 
                   system_time=date_t.system,
                   time_nothin_do=date_t.idle, 
                   nice_time=date_t.nice
                    )    

    date_s = psutil.cpu_stats() # It's modul output statistic CPU
    res_cpu.update(
                    sum_switch=date_s.ctx_switches,       # number of context switches
                    sum_iter=date_s.interrupts,           # number of interrupts
                    sun_softiter=date_s.soft_interrupts,  # number soft interrupts
                    sum_call=date_s.syscalls              # number system calls
                    )
        
    date_per = psutil.cpu_percent(1, True) # It's modul output percent load CPUs
    res_cpu.update(
                    use_cpu1=date_per[0], use_cpu2=date_per[1],     # The numbers CPU(№)
                    use_cpu3=date_per[2], use_cpu4=date_per[3],
                    use_cpu5=date_per[4], use_cpu6=date_per[5],
                    use_cpu7=date_per[6], use_cpu8=date_per[7]
                    )
    return res_cpu


def info_memmory(): # It's function return statistic about used system(virtual) memory
    virtual_mem = {}
    date_mem = psutil.virtual_memory() 
    virtual_mem.update(
                        total_memory=date_mem.total/1024**3,           # all memory
                        available_memory=date_mem.available/1024**3,   # free memory
                        used_memory=date_mem.used/1024**3              # used memory
                        )
    return dict(virtual_mem)


def info_disk(): # It's function return infomation about disk (HDDR or SSD)
    res_disk = {}
    date_disk = psutil.disk_usage('/')
    res_disk.update(
                    total_disk=float(date_disk.total/(1024**3)),  # total disk GB
                    used_disk=float(date_disk.used/(1024**3)),    # used disk GB
                    free_disk=float(date_disk.free/(1024**3)),    # free disk GB 
                    usedisk_percent=date_disk.percent             # percent use disk
                    )
    return res_disk


def info_baterry(): # It's function return information about baterry and chager
    res_battery = {}
    date_baterry = psutil.sensors_battery() # output baterry statistic
    res_battery.update(
                        low_percent=date_baterry.percent,              # low percent beterry
                        critical_low=int(date_baterry.secsleft/60),    # time to critical low in minutes
                        on_chager=date_baterry.power_plugged           # status chager: ON/OFF (True/False)
                        )
    return res_battery


def info_network(): # It's function return information about network statistic
    res_network = {}
    date_network = psutil.net_io_counters() # methot output network statistic
    res_network.update(
                        send_bytes = date_network.bytes_sent,      # send bytes  
                        received_bytes = date_network.bytes_recv,  # received bytes
                        error = date_network.errin                 # error network system
                        )
    return res_network    


def info_user(): # Function return information about system user/users
    res_user = {}
    date_user = psutil.users() # output user information
    res_user.update(
                    user_name=date_user[0].name,         # user name
                    type_cmd=date_user[0].terminal,      # type cmd using
                    star_time=date_user[0].started/60**2 # time from start
                    )
    return res_user            


def info_swap(): # It's function return information about SWAP memory
    res_swap = {}
    date_swaps = psutil.swap_memory()
    res_swap.update(
                    total=date_swaps.total,    # total swap memory
                    used=date_swaps.used,      # used swap memory
                    free=date_swaps.free,      # free wap memory
                    percent=date_swaps.percent # percent used swap memory
                    )
    return res_swap                


def info_process(): # It's function print all worked process in system
    
    date_proc = []
    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        date_proc.append(proc.info)
    return date_proc


# It's function outputting all transferred functions
def show(                                    
        cpu=None, memory=None, 
        disk=None, baterry=None, 
        network=None, user=None, 
        swap=None, process = None
        ):

    cputime_temp = (
                    '| {user_time:^10} | {system_time:^11} '
                    '| {time_nothin_do:^10} | {nice_time:^9} |'
                    )

    cpustats_temp = (
                     '| {sum_switch:^10} | {sum_iter:^11} '
                     '| {sun_softiter:^12} | {sum_call:^9} |'
                     )

    cpupercent_temp = (
                       '| {use_cpu1:^5} | {use_cpu2:^5} '
                       '| {use_cpu3:^5} | {use_cpu4:^5} '
                       '| {use_cpu5:^5} | {use_cpu6:^5} '
                       '| {use_cpu7:^5} | {use_cpu8:^5} |'
                        )

    memory_templage = (
                        '| {total_memory:^16.0f} '
                        '| {available_memory:^16.1f} '
                        '| {used_memory:^16.1f} |'
                        )
 
    disk_templage = (
                     '| {total_disk:^15.3f} | {used_disk:^16.3f}'
                     '| {free_disk:^15.3f} | {usedisk_percent:^10} |'
                      )

    baterry_temp = (
                    ' Your baterry charge: {low_percent}%\n'
                    ' Time to critical low(min): {critical_low}\n'
                    ' Charge from sets: {on_chager} '
                    )

    network_temp = (
                    '| {send_bytes:^10} '
                    '| {received_bytes:^14} '
                    '| {error:5} |'
                    )

    user_temp = (
                 '| {user_name:^10} '
                 '| {type_cmd:^10} '
                 '| {star_time:^6.0f} min |'
                 )

    swap_temp = '| {total:^5} | {used:^5} | {free:^5} | {percent:^7} |'
    


    # print function info_cpu()
    print('\n{:^53}'.format('<<Information about user time>>'))
    print(
        '| {:^10} | {:^11} | {:^10} | {:^9} |'.format(
                                                        'user time',
                                                        'system time',
                                                        'nothing do',
                                                        'nice time'
                                                        )
                                                        )
    print(cputime_temp.format(**cpu))
    print(len(cputime_temp.format(**cpu)) * '-', end='\n\n')
    
    print('{:^55}'.format('<<Information about SWITCH>>'))
    print(
        '| {:^10} | {:^11} | {:^12} | {:^9} |'.format(
                                                        'sum switch',
                                                        'sum iter',
                                                        'sum softiter',
                                                        'sum call'
                                                        )
                                                        )
    print(cpustats_temp.format(**cpu)) 
    print(len(cpustats_temp.format(**cpu)) * '-', end='\n\n')
    
    print('{:^65}'.format("Information about utilization your CPU's"))

    for i in range(1, len(psutil.cpu_percent(1,True)) + 1):
        print('| CPU{}-%'.format(i), end="")
    print('|')

    print(cpupercent_temp.format(**cpu)) 
    print(len(cpupercent_temp.format(**cpu)) * '-', end='\n\n')
    
    # print function info_memory()
    print('{:^58}'.format('Information about memory RAM'))
    print(
        '| {:^16} | {:^16} | {:^16} |'.format(
                                               'total memory GB',
                                               'available GB',
                                               'used memory GB'
                                                )
                                                )
    print(memory_templage.format(**memory))
    print(len(memory_templage.format(**memory)) * '-', end='\n\n')

    # print function info_disk()
    print('{:^68}'.format('Information adout hard-disk'))
    print(
        '| {:^15} | {:^15} | {:^15} | {:^10} |'.format(
                                                        'total disk GB',
                                                        'used disk GB',
                                                        'free disk GB',
                                                        'usedisk(%)'
                                                        )
                                                        )       
    print(disk_templage.format(**disk))
    print(len(disk_templage.format(**disk)) * '-',end='\n\n')

    # print information info_beterry()
    print('<<{:^30}>>'.format('Information about your baterry charge! '))
    print(baterry_temp.format(**baterry), end='\n\n')
    
    print('{:^39}'.format('<<Information network condition>>'))
    print(
        '| {} | {} | {} |'.format(
                                   'send butes',
                                   'received bytes',
                                   'ERROR'
                                    )
                                    )
    print(network_temp.format(**network))
    print(len(network_temp.format(**network)) * '-', end='\n\n')
    
    # print information info_user()
    print('{:^40}'.format('<<Information about user>>'))
    print(
        '| {:^10} | {:^10} | {:^10} |'.format(
                                                'user name',
                                                'type cmd', 
                                                'start time'
                                                )
                                                )
    print(user_temp.format(**user))
    print(len(user_temp.format(**user)) * '-', end='\n\n')
   
   # print function info_swap()
    print('{:^20}'.format('<<This information about SWAP memory>>'))
    print(
        '| {:^5} | {:^5} | {:^5} | {:^7} |'.format(
                                                    'total',
                                                    'used',
                                                    'free',
                                                    'percent'
                                                    )
                                                    )
    print(swap_temp.format(**swap))
    print(len(swap_temp.format(**swap)) * '-', end='\n\n')

    print('{:^115}'.format('<< PROCESS WORCED IN YOUR SYSTEM >>'))
    print('_' * 115)
    for n in process:
        output_inf = 'PID {pid:>5} | process name: {name:>50} | user name : {username:>22} |'
        print(output_inf.format(**n))


def main():
    date_cpu = info_cpu()
    date_memory = info_memmory()
    date_disk = info_disk()
    date_baterry = info_baterry()
    date_network = info_network()
    date_user = info_user()
    date_swap = info_swap()
    date_process = info_process()
    
    
    # call the function show() with all methods(functions)
    show(
        cpu=date_cpu,
        memory=date_memory,
        disk=date_disk, 
        baterry=date_baterry, 
        network=date_network, 
        user=date_user,
        swap=date_swap,
        process=date_process
        )


if __name__ == '__main__': # script start
    main()    
    