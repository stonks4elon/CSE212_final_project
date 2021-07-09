"""
Craig Wright
CSE 212
Spring 2021

Below is a simple program of a digital to-do list for Dory, a very forgetful fish who somehow landed an office job.
(The extensive modifications needed for a fish's office cubicle are beyond the scope of this text.)

Dory can never remember to do things in chronological order, so she just does what is on the top of her to-do list. Once
she completes an item, it needs to be removed from her list. But if Dory happens on some luck and remembers something
randomly, she needs to be able quickly add it to her to-do list so that it can be written down before her memory is
wiped clean again.

In this problem, there is an error that causes the to-do list to not update correctly. Edit the code so that the program
will function correctly.
"""


def add_task(checklist, task):
    checklist.append(task)  # TODO: you must append to the list


def complete_and_report_task(checklist):
    if len(checklist) > 0:  # TODO: make sure the list is greater than 0 before popping
        print(checklist.pop())


# Test cases:
to_do_list = ['Just keep swimming']
add_task(to_do_list, 'Just keep swimming')
add_task(to_do_list, 'Find Nemo!')
add_task(to_do_list, 'Just keep swimming')
add_task(to_do_list, 'Talk Marlin\'s ear off')
add_task(to_do_list, 'Just keep swimming')
add_task(to_do_list, 'Just keep swimming')
add_task(to_do_list, 'Help the kind orange fish find his son!')
add_task(to_do_list, 'Just keep swimming')
add_task(to_do_list, 'Learn to speak whale')
complete_and_report_task(to_do_list)  # Learn to speak whale
complete_and_report_task(to_do_list)  # Just keep swimming
complete_and_report_task(to_do_list)  # Help the kind orange fish find his son!
complete_and_report_task(to_do_list)  # Just keep swimming
add_task(to_do_list, 'Just keep swimming')
add_task(to_do_list, '42 Wallaby Way. Sydney')
add_task(to_do_list, 'Make friends with sharks')
complete_and_report_task(to_do_list)  # Make friends with sharks
add_task(to_do_list, 'Get stung by jelly fish')
complete_and_report_task(to_do_list)  # Get stung by jelly fish
complete_and_report_task(to_do_list)  # 42 Wallaby Way. Sydney
complete_and_report_task(to_do_list)  # Just keep swimming
complete_and_report_task(to_do_list)  # Just keep swimming
add_task(to_do_list, 'Ride on the backs of rasta sea turtles')
complete_and_report_task(to_do_list)  # Ride on the backs of rasta sea turtles
complete_and_report_task(to_do_list)  # Talk Marlin's ear off
complete_and_report_task(to_do_list)  # Just keep swimming
complete_and_report_task(to_do_list)  # Find Nemo!
complete_and_report_task(to_do_list)  # Just keep swimming
complete_and_report_task(to_do_list)  # Just keep swimming
complete_and_report_task(to_do_list)  # no output
