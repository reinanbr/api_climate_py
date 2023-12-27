import psutil as ps, cpuinfo as ci

info_cpu = ci.get_cpu_info()
def cpu_info():
    return info_cpu


def memory_stats():
    mem_ps = ps.virtual_memory()
    mem_usage = mem_ps.used/(1024**3)
    mem_total = mem_ps.total/(1024**3)
    mem_active = mem_ps.active/(1024**3)
    mem_cached = mem_ps.cached/(1024**3)
    mem_inactive = mem_ps.inactive/(1024**3)
    mem_free = mem_ps.free/(1024**3)
    mem_percent = mem_ps.percent
    
    memory = {
        'usage':mem_usage,
        'total':mem_total,
        'active':mem_active,
        'cached':mem_cached,
        'inactive':mem_inactive,
        'free':mem_free,
        'percent':mem_percent
    }
    return memory



def cpu_stats():
    cpu_freq_ps = ps.cpu_freq()
    cpu_freq_used = cpu_freq_ps.current
    cpu_freq_max = cpu_freq_ps.max
    cpu_freq_min = cpu_freq_ps.min
    
    cpu_cores = ps.cpu_count()
    
    cpu_percent = ps.cpu_percent()
    
    cpu_times = ps.cpu_times()._asdict()
    
    return {'frequency':{'used':cpu_freq_used,
                         'max':cpu_freq_max,
                         'min':cpu_freq_min,
                         'percent':cpu_percent,
                         },
            'cores':cpu_cores,
            'times':cpu_times}

