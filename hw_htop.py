from datetime import date
import psutil


def info_cpu():   
    res_cpu = {}
    date_t = psutil.cpu_times()
    res_cpu.update(user_time=date_t.user, system_time=date_t.system, time_notdo=date_t.idle, nice_time=date_t.nice )    

    date_s = psutil.cpu_stats()
    res_cpu.update(sum_switch=date_s.ctx_switches, sum_iter=date_s.interrupts, sun_softiter=date_s.soft_interrupts, sum_call=date_s.syscalls)
        
    date_per = psutil.cpu_percent(1, True)
    res_cpu.update(use_cpu1=date_per[0], use_cpu2=date_per[1], use_cpu3=date_per[2], use_cpu4=date_per[3],
                        use_cpu5=date_per[4], use_cpu6=date_per[5],use_cpu7=date_per[6], use_cpu8=date_per[7])
    return res_cpu

def info_memmory():
    virtual_mem = {}
    date_mem = psutil.virtual_memory()
    virtual_mem.update(total_memory=date_mem.total/1024**3, available_memory=date_mem.available/1024**3, used_memory=date_mem.used/1024**3)
    return dict(virtual_mem)

def info_disk():
    res_disk = {}
    date_disk = psutil.disk_usage('/')
    res_disk.update(total_disk=float(date_disk.total/(1024**3)), used_disk=float(date_disk.used/(1024**3)), 
                    free_disk=float(date_disk.free/(1024**3)), usedisk_percent=date_disk.percent)
    return res_disk

def info_baterry():
    res_battery = {}
    date_baterry = psutil.sensors_battery()
    res_battery.update(low_percent=date_baterry.percent, critical_low=int(date_baterry.secsleft/60), on_chager=date_baterry.power_plugged)
    return res_battery

def info_network():
    res_network = {}
    date_network = psutil.net_io_counters()
    res_network.update(send_bytes = date_network.bytes_sent, received_bytes = date_network.bytes_recv, error = date_network.errin)
    return res_network    

def show(cpu=None, memory=None, disk=None, baterry=None, network=None):
    cputime_temp = '| {user_time:^10} | {system_time:^11} | {time_notdo:^10} | {nice_time:^9} |'
    cpustats_temp = '| {sum_switch:^10} | {sum_iter:^11} | {sun_softiter:^12} | {sum_call:^9} |'
    cpupercent_temp = '| {use_cpu1:^5} | {use_cpu2:^5} | {use_cpu3:^5} | {use_cpu4:^5} | {use_cpu5:^5} | {use_cpu6:^5} | {use_cpu7:^5} | {use_cpu8:^5} |'
    memory_templage = '| {total_memory:^16.0f} | {available_memory:^16.1f} | {used_memory:^16.1f} |'
    disk_templage = '| {total_disk:^15.3f} | {used_disk:^15.3f} | {free_disk:^15.3f} | {usedisk_percent:^10} |'
    baterry_temp = ' Your baterry charge: {low_percent}%\n Time to critical low(min): {critical_low}\n Charge from sets: {on_chager} '
    network_temp = '| {send_bytes:^10} | {received_bytes:^14} | {error:5} |'

    print('\n{:^53}'.format('<<Information about user time>>'))
    print('| {:^10} | {:^11} | {:^10} | {:^9} |'.format('user time', 'system time', 'nothing do', 'nice time'))
    print(cputime_temp.format(**cpu))
    print(len(cputime_temp.format(**cpu)) * '-', end='\n\n')
    
    print('{:^55}'.format('<<Information about SWITCH>>'))
    print('| {:^10} | {:^11} | {:^12} | {:^9} |'.format('sum switch', 'sum iter', 'sum softiter', 'sum call'))
    print(cpustats_temp.format(**cpu)) 
    print(len(cpustats_temp.format(**cpu)) * '-', end='\n\n')
    
    print('{:^65}'.format("Information about utilization your CPU's"))
    for i in range(1, len(psutil.cpu_percent(1,True)) + 1):
        print('| CPU{}-%'.format(i), end="")
    print('|')
    print(cpupercent_temp.format(**cpu)) 
    print(len(cpupercent_temp.format(**cpu)) * '-', end='\n\n')
    
    print('{:^58}'.format('Information about memory RAM'))
    print('| {:^16} | {:^16} | {:^16} |'.format('total memory GB', 'available GB', 'used memory GB'))
    print(memory_templage.format(**memory))
    print(len(memory_templage.format(**memory)) * '-', end='\n\n')

    print('{:^68}'.format('Information adout hard-disk'))
    print('| {:^15} | {:^15} | {:^15} | {:^10} |'.format('total disk GB', 'used disk GB', 'free disk GB', 'usedisk(%)'))
    print(disk_templage.format(**disk))
    print(len(disk_templage.format(**disk)) * '-',end='\n\n')

    print('<<{:^30}>>'.format('Information about your baterry charge! '))
    print(baterry_temp.format(**baterry), end='\n\n')
    
    print('{:^39}'.format('<<Information network condition>>'))
    print('| {} | {} | {} |'.format('send butes', 'received bytes', 'ERROR'))
    print(network_temp.format(**network), end='\n\n')

def main():
    date_cpu = info_cpu()
    date_memory = info_memmory()
    date_disk = info_disk()
    date_baterry = info_baterry()
    date_network = info_network()
    
    show(cpu=date_cpu ,memory=date_memory, disk=date_disk, baterry=date_baterry, network=date_network)


if __name__ == '__main__':
    main()    
