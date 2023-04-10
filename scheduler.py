from copy import copy

quanta = 3
context_switch_time = 1

cpu_scheduling = []
scheduling_starts = []
scheduling_ends = []

cpu_scheduling_pname = []
colors = []


def scheduler(process_list):
    ready_queue = process_list.copy()
    timeline = 0

    while not is_queue_empty(ready_queue):
        process = ready_queue[0]

        scheduling_starts.append(timeline)

        save_process_state_in_scheduling(process)

        ready_queue.remove(process)
        if process.burst_time > quanta:
            process.burst_time -= quanta
            ready_queue.append(process)
            timeline += quanta
            scheduling_ends.append(timeline)
        elif process.burst_time <= quanta:
            timeline += process.burst_time
            process.burst_time = 0
            scheduling_ends.append(timeline)

        timeline += context_switch_time

    set_all_times(process_list)

    for process in cpu_scheduling:
        cpu_scheduling_pname.append(f'P{process.pid}')
        colors.append(process.color)


def is_queue_empty(ready_queue):
    if (len(ready_queue) == 0):
        return True
    return False


def save_process_state_in_scheduling(process):
    actual_state = copy(process)
    cpu_scheduling.append(actual_state)


def last_process_occurrence_in_scheduling(pid):
    for i in reversed(range(len(cpu_scheduling))):
        if cpu_scheduling[i].pid == pid:
            return i


def first_process_occurrence_in_scheduling(pid):
    for i in range(len(cpu_scheduling)):
        if cpu_scheduling[i].pid == pid:
            return i


def set_all_times(process_list):
    completion_times(process_list)
    waiting_times(process_list)
    response_times(process_list)
    return_times(process_list)


def completion_times(process_list):
    for process in process_list:
        i = last_process_occurrence_in_scheduling(process.pid)
        ct = scheduling_ends[i]
        process.set_completion_time(ct)
        process.set_turnaround_time(tt=ct)


def waiting_times(process_list):
    for process in process_list:
        wt = process.turnaround_time - process.initial_burst_time
        process.set_waiting_time(wt)


def response_times(process_list):
    for process in process_list:
        i = first_process_occurrence_in_scheduling(process.pid)
        rt = scheduling_starts[i]
        process.set_response_time(rt)


def return_times(process_list):
    for process in process_list:
        rt = process.completion_time - process.response_time
        process.set_return_time(rt)