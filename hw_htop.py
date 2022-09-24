import psutil


class Cpu:
    
    
    def get_info(self): # It's function return information about your CPU 
        self.res_cpu = {}
        date_t = psutil.cpu_times() # It's modul output information about worktime 
        self.res_cpu.update(
                    user_time=date_t.user, 
                    system_time=date_t.system,
                    time_nothin_do=date_t.idle, 
                    nice_time=date_t.nice
                        )    

        date_s = psutil.cpu_stats() # It's modul output statistic CPU
        self.res_cpu.update(
                        sum_switch=date_s.ctx_switches,       # number of context switches
                        sum_iter=date_s.interrupts,           # number of interrupts
                        sun_softiter=date_s.soft_interrupts,  # number soft interrupts
                        sum_call=date_s.syscalls              # number system calls
                        )
            
        date_per = psutil.cpu_percent(1, True) # It's modul output percent load CPUs
        self.res_cpu.update(
                        use_cpu1=date_per[0], use_cpu2=date_per[1],     # The numbers CPU(№)
                        use_cpu3=date_per[2], use_cpu4=date_per[3],
                        use_cpu5=date_per[4], use_cpu6=date_per[5],
                        use_cpu7=date_per[6], use_cpu8=date_per[7]
                        )


    def __str__(self):
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
        str1 = ('\n{:^53}'.format('<<Information about user time>>'))
        str2 = (
            '| {:^10} | {:^11} | {:^10} | {:^9} |'.format(
                                                            'user time',
                                                            'system time',
                                                            'nothing do',
                                                            'nice time'
                                                            )
                                                            )
        str3 = (cputime_temp.format(**self.res_cpu))
        str4 = (len(cputime_temp.format(**self.res_cpu)) * '-')
        str41 = ('\n')

        str5 = ('{:^55}'.format('<<Information about SWITCH>>'))
        str6 = (
            '| {:^10} | {:^11} | {:^12} | {:^9} |'.format(
                                                            'sum switch',
                                                            'sum iter',
                                                            'sum softiter',
                                                            'sum call'
                                                            )
                                                            )
        str7 = (cpustats_temp.format(**self.res_cpu)) 
        str8 = (len(cpustats_temp.format(**self.res_cpu)) * '-')
        str81 = ('\n')

        str9 = ('{:^65}'.format("Information about utilization your CPU's"))

        str10 = (
                '| CPU{0}-%| CPU{1}-%| CPU{2}-%| CPU{3}-%|'
                ' CPU{4}-%| CPU{5}-%| CPU{6}-%| CPU{7}-%|\n'
                .format(
                        *range(
                            1, len(psutil.cpu_percent(1,True)) + 1
            )
        )
    )

        str12 = (cpupercent_temp.format(**self.res_cpu)) 
        str13 = (len(cpupercent_temp.format(**self.res_cpu)) * '-')
        
        return (f'{str1}\n'
                f'{str2}\n'
                f'{str3}\n'
                f'{str4}\n'
                f'{str41}'
                f'{str5}\n'
                f'{str6}\n'
                f'{str7}\n'
                f'{str8}\n'
                f'{str81}'
                f'{str9}\n'
                f'{str10}'
                f'{str12}\n'
                f'{str13}\n'
                )
        

class VirtualMemory:


    def get_info(self): # It's function return statistic about used system(virtual) memory
        virtual_mem = {}
        date_mem = psutil.virtual_memory() 
        virtual_mem.update(
                            total_memory=date_mem.total/1024**3,           # all memory
                            available_memory=date_mem.available/1024**3,   # free memory
                            used_memory=date_mem.used/1024**3              # used memory
                            )
        self.res_memory = dict(virtual_mem)                    


    def __str__(self):
        memory_templage = (
                           '| {total_memory:^16.0f} '
                           '| {available_memory:^16.1f} '
                           '| {used_memory:^16.1f} |'
                            )
        str_mem1 = ('{:^58}'.format('Information about memory RAM'))
        str_mem2 = (
        '| {:^16} | {:^16} | {:^16} |'.format(
                                               'total memory GB',
                                               'available GB',
                                               'used memory GB'
                                                )
                                                )
        str_mem3 = (memory_templage.format(**self.res_memory))
        str_mem4 = (len(memory_templage.format(**self.res_memory)) * '-')
        str_mem5 = '\n'
        return (f'{str_mem1}\n'
                f'{str_mem2}\n'
                f'{str_mem3}\n'
                f'{str_mem4}\n'
                f'{str_mem5}') 


class Disk:


    def get_info(self): # It's function return infomation about disk (HDDR or SSD)
        self.res_disk = {}
        date_disk = psutil.disk_usage('/')
        self.res_disk.update(
                        total_disk=float(date_disk.total/(1024**3)),  # total disk GB
                        used_disk=float(date_disk.used/(1024**3)),    # used disk GB
                        free_disk=float(date_disk.free/(1024**3)),    # free disk GB 
                        usedisk_percent=date_disk.percent             # percent use disk
                        )


    def __str__(self):
        disk_templage = (
                     '| {total_disk:^15.3f} | {used_disk:^16.3f}'
                     '| {free_disk:^15.3f} | {usedisk_percent:^10} |'
                      )
        str1_disk = ('{:^68}'.format('Information adout hard-disk'))
        str2_disk = (
        '| {:^15} | {:^15} | {:^15} | {:^10} |'.format(
                                                        'total disk GB',
                                                        'used disk GB',
                                                        'free disk GB',
                                                        'usedisk(%)'
                                                        )
                                                        )       
        str3_disk = (disk_templage.format(**self.res_disk))
        str4_disk = (len(disk_templage.format(**self.res_disk)) * '-')
        return (f'{str1_disk}\n'
                f'{str2_disk}\n'
                f'{str3_disk}\n'
                f'{str4_disk}\n')              


class InfoBaterry():


    def get_info(self): # It's function return information about baterry and chager
        self.res_battery = {}
        date_baterry = psutil.sensors_battery() # output baterry statistic
        self.res_battery.update(
                            low_percent=date_baterry.percent,              # low percent beterry
                            critical_low=int(date_baterry.secsleft/60),    # time to critical low in minutes
                            on_chager=date_baterry.power_plugged           # status chager: ON/OFF (True/False)
                            )


    def __str__(self):
        baterry_temp = (
                        ' Your baterry charge: {low_percent}%\n'
                        ' Time to critical low(min): {critical_low}\n'
                        ' Charge from sets: {on_chager} '
                        )
        str1_beterry = ('<<{:^30}>>'.format('Information about your baterry charge! '))
        str2_baterry = (baterry_temp.format(**self.res_battery))
        return (f'{str1_beterry}\n'
                f'{str2_baterry}\n'
                )


class NetworkInfo():


    def get_info(self): # It's function return information about network statistic
        self.res_network = {}
        date_network = psutil.net_io_counters() # methot output network statistic
        self.res_network.update(
                            send_bytes = date_network.bytes_sent,      # send bytes  
                            received_bytes = date_network.bytes_recv,  # received bytes
                            error = date_network.errin                 # error network system
                            )  


    def __str__(self):
        network_temp = (
                    '| {send_bytes:^10} '
                    '| {received_bytes:^14} '
                    '| {error:5} |'
                    )
        str1_network = ('{:^39}'.format('<<Information network condition>>'))
        str2_network = (
            '| {} | {} | {} |'.format(
                                       'send butes',
                                       'received bytes',
                                       'ERROR'
                                        )
                                        )
        str3_network = (network_temp.format(**self.res_network))
        str4_network = (len(network_temp.format(**self.res_network)) * '-')
        return (f'{str1_network}\n'
                f'{str2_network}\n'
                f'{str3_network}\n'
                f'{str4_network}')


class UserInfo:


    def get_info(self): # Function return information about system user/users
        self.res_user = {}
        date_user = psutil.users() # output user information
        self.res_user.update(
                        user_name=date_user[0].name,         # user name
                        type_cmd=date_user[0].terminal,      # type cmd using
                        star_time=date_user[0].started/60**2 # time from start
                        )   
    

    def __str__(self):
        user_temp = (
                 '| {user_name:^10} '
                 '| {type_cmd:^10} '
                 '| {star_time:^6.0f} min |'
                 )
        str1_user = ('{:^40}'.format('<<Information about user>>'))
        str2_user = (
            '| {:^10} | {:^10} | {:^10} |'.format(
                                                    'user name',
                                                    'type cmd', 
                                                    'start time'
                                                    )
                                                    )
        str3_user = (user_temp.format(**self.res_user))
        str4_user = (len(user_temp.format(**self.res_user)) * '-')
        return (f'{str1_user}\n'
                f'{str2_user}\n'
                f'{str3_user}\n'
                f'{str4_user}\n')


class SwapInfo:


    def get_info(self): # It's function return information about SWAP memory
        self.res_swap = {}
        date_swaps = psutil.swap_memory()
        self.res_swap.update(
                        total=date_swaps.total,    # total swap memory
                        used=date_swaps.used,      # used swap memory
                        free=date_swaps.free,      # free wap memory
                        percent=date_swaps.percent # percent used swap memory
                        )    
    

    def __str__(self):
        swap_temp = '| {total:^5} | {used:^5} | {free:^5} | {percent:^7} |'
        str1_swap = ('{:^20}'.format('<<This information about SWAP memory>>'))
        str2_swap = (
            '| {:^5} | {:^5} | {:^5} | {:^7} |'.format(
                                                        'total',
                                                        'used',
                                                        'free',
                                                        'percent'
                                                        )
                                                        )
        str3_swap = (swap_temp.format(**self.res_swap))
        str4_swap = (len(swap_temp.format(**self.res_swap)) * '-')
        return (f'{str1_swap}\n'
                f'{str2_swap}\n'
                f'{str3_swap}\n'
                f'{str4_swap}\n')     


def main():
    cpu= Cpu()
    cpu.get_info()
    print(cpu)


    memory = VirtualMemory()
    memory.get_info()
    print(memory)


    disk = Disk()
    disk.get_info()
    print(disk)

    baterry = InfoBaterry()
    baterry.get_info()
    print(baterry)
    

    network = NetworkInfo()
    network.get_info()
    print(network)

    
    user = UserInfo()
    user.get_info()
    print(user)


    swap = SwapInfo()
    swap.get_info()
    print(swap)


if __name__ == "__main__":
    main()
    