#!/usr/bin/env python3
# This script helps generate the weekly schedule pages
# that are stored in the _modules folder.
# After updating the holidays and the other info
# it is assumed that this script will be run once to
# generate the main skeleton pages, and the rest of the
# schedule will be manually updated in the respective
# weekly .md files.

"""
the soft/hard deadlines in Spring 2022:
**PAs** are expected to be done before Tue 10PM and are due then
**CAs** are expected to be done before next Tue 10PM and are due then
**LAs** are expected to be done before next Wed 10PM and are due then
...which means:

Week 1:
no deadlines
LA01 are released

Week 2:
PA01 and PA02 are expected to be done Week 2 Tue 10PM
CA01 are expected to be done Week 2 Tue 10PM
LA01 are expected to be done Week 2 Wed 10PM
LA02 are released
Due at 10PM of Week 2 Sunday: PA01 and PA02, CA01, LA01

Week 3:
PA03 are expected to be done Tue 10PM
CA02 are expected to be done Tue 10PM
LA02 are expected to be done Wed 10PM
LA03 are released
Due at 10PM of Week 3 Sunday: PA03, CA02, LA02

and so on :-)
"""

months = {
    1: 31,
    2: 28, # unless it's a leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month_name = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

days = {
    1: "Sun",
    2: "Mon",
    3: "Tue",
    4: "Wed",
    5: "Thu",
    6: "Fri",
    7: "Sat"
}

due_dates = {}
for day in days.values():
    due_dates[day] = ": "

### WARNING: do not use colons in the topic title - it confuses Jekyll
topic = {
    1: "Introduction to Python 3",
    2: "Objects, Functions, and Expressions",
    3: "Making decisions in programs (Branching)",
    4: "Representing data (Types and Data Structures)",
    5: "Writing reusable, generalizable code (Functions)",
    6: "Repeating and iterating (Loops)",
    7: "Lists and Dictionaries",
    8: "More Advanced Functions and Strings",
    9: "Storing and Retrieving Data from Files",
    10: "Exploiting self-similarity (Recursion)",
}

### These notes are replaced with the specifics for each respective week below
class_time = "09:30am"
due_time = "11:59pm"

"""
class_days = ["Mon", "Wed"]
lab_day = "Tue"
lab_due = "Mon"
"""
class_days = ["Tue", "Thu"]
lab_day = "Wed"
lab_due = "Tue"


### NEW: Assign students to start upcoming week's PAs, CAs 
due_dates["Sun"] += f": Start: **PA**{{: .label .label-orange }}, **CA**{{: .label .label-blue }}\n"

### Add classes/labs to the schedule
due_dates[class_days[0]] += f": {class_time} **Class**{{: .label .label-purple }}\n"
due_dates[class_days[1]] += f": {class_time} **Class**{{: .label .label-purple }}+**Quiz**{{: .label .label-red }}\n"
due_dates[lab_day] += f": **Lab sections**{{: .label .label-purple }}\n"

### NEW: Deadline for LA checkpoints (end of day, 11:59pm when lab occurs)  
##due_dates[lab_day] += f": **{due_time}**  ⏰  Due: **LA Checkpoint**{{: .label .label-green }}\n"

### NEW: Deadline for prev week's LA 11:59pm (the day before lab day)
due_dates[lab_due] += f": **{due_time}**  ⏰  Due: **LA**{{: .label .label-green }}\n"

### NEW: Deadline for prev week's PAs, CAs, Reflection. Sunday 11:59pm
due_dates["Sat"] += f": **{due_time}**  ⏰  Due: **PA**{{: .label .label-orange }}, **CA**{{: .label .label-blue }}, **Reflection**{{: .label .label-yellow }}\n"


  
# Wed
### STAFF SCHEDULE: Instructors review labs for upcoming week

# Thu
### STAFF SCHEDULE: Assign staff to complete lab for following week

# Fri
### STAFF SCHEDULE: Staff reports to instructors any feedback on labs for following week

# Sat
### STAFF SCHEDULE: Instructors make labs visible on zyBooks. (Don't give edit privs to TA/LAs)



"""
due_dates_old = {
    "Mon" : ": _Finish reading and review Chapter X in zyBooks._\n"
            ": _Complete the PAs and CAs._\n"
            ": _Test your understanding with the Reading Quiz._\n"
#            ": [](#)\n"
            "   : **{due_time}** ⏰  Due: **PA**{: .label .label-orange }",
    class_days[0] : ": {class_time} **Class**{: .label .label-purple }\n" 
#            ": [](#)\n"
            "   : **{due_time}** ⏰  Due: **CA**{: .label .label-blue }",
    "Wed" : ": 09:00am **LA**{: .label .label-green }_are expected to be done_\n"
#           ": [](#)\n"
            "   : **{due_time}** ⏰  Due: **LA**{: .label .label-green }",
    class_days[1] : ": {class_time} **Class**{: .label .label-purple }\n"
#            ": [](#)\n"
            "   : **{due_time}** ⏰  Due: **LA Checkpoint**{: .label .label-green }",
    "Fri" : ": _Begin reading next week’s chapter._\n"
            ": _Work through its PAs and CAs._\n"
            ": _Finish the Weekly reflection._",
    "Sat" : ": _Async activities_ ☝️ ", 
    "Sun" : ": _By the end of Sunday: Ideally, you should be finished with PAs for Chapter Y and done with the CAs for its first 4-5 sections._\n"
            ": [](#)\n"
            "   : **{due_time}** ⏰  Due: **Reflection**{: .label .label-yellow }\n"
}
"""


holiday_prompt = ": **Holiday (no classes)**{: .label .label-red }"
admin_prompt = ': <p class="text-grey-dk-000 mb-0">'

### https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/academic-calendars 
holidays = {
    (1, 16) : "Martin Luther King Jr. Day", # January 16
    (2, 20) : "Presidents' Day", # February 20
    (5, 29) : "Memorial Day", # May 29
}

### https://registrar.sa.ucsb.edu/calendars/calendars-deadlines/registration-pass-dates
admin_dates = {
#    (2, 6) : "Deadline to Drop Courses",
#    (3, 17) : "Instruction Ends"
    (4, 28) : "Deadline to Drop Courses",
    (6, 9) : "Instruction Ends", # June 9
    (6, 16) : "Quarter Ends" # June 9
}

start_month = 4 # jan
start_sunday = 2 # apr 2 is first day of calendar 
start_week = 1
exclude_weekends = False #True
include_days_of_week = True # whether to include "Mon", "Tue" with the day
#include_days_of_week = False # whether to include "Mon", "Tue" with the day
end_month = 6 # 
end_day = 16 # the last day of the Final Exams (quarter ends)

num_days = 7
num_weeks = 11 # stop before this week
if exclude_weekends:
    num_days = 5


month = start_month
cur_day = start_sunday
week = start_week

while week < num_weeks: # loop through the weeks
    # write week-##.md
    filename = "week-" + str(week).zfill(2) + ".md" # pad with zeros
    print("Writing", filename)
    md_file = open(filename, "w")
    md_file.write("---\n")
    md_file.write(f"title: Week {str(week)}\n") 
    md_file.write(f"topic: {topic[week]}\n")
    md_file.write("---\n")

    for day in range(1, num_days+1):
        if cur_day > months[month]:
            cur_day = cur_day - months[month] # e.g., 10/31->11/1
            month += 1
        date_str = month_name[month] + " " + str(cur_day)+ "\n"
        if include_days_of_week:
            date_str = days[day] + ", " + date_str
        md_file.write(date_str)
        if holidays.get((month, cur_day)) != None: # if we found a holiday
            md_file.write(f"{holiday_prompt}**{holidays[(month, cur_day)]}**\n\n")
        if admin_dates.get((month, cur_day)) != None:
            md_file.write(f'{admin_prompt}<em>{admin_dates[(month, cur_day)]}</em></p>\n\n')
        if due_dates.get(days[day]) != None: 
            if week > 1:
                this_week = str(week).zfill(2)
                last_week = str(week-1).zfill(2)
#due_str = due_dates[days[day]].replace("PA", "PA"+this_week).replace("CA", "CA"+last_week).replace("LA", "LA"+last_week).replace("Chapter X", "Chapter "+this_week)
                due_str = due_dates[days[day]]
                if week == 9:
                    due_str = due_str.replace(" and done with the CAs for its first 4-5 sections", "")
                if week < 10:
                    due_str = due_str.replace("Chapter Y", f"Chapter {int(this_week)+1}").replace("Start on PA", f"Start on **PA{int(this_week)+1:0>2}**")
                else: # last week of the term (week 10) 
#due_str = due_str.replace("\n : _Finish CA{{: .label .label-blue } + Start on PA{{: .label .label-orange }_", "")

                    #print(due_str)
                    #due_str = due_str.replace("+**Quiz**\{\{: .label .label-red\}\}", "")
                    #due_str = due_str.replace("+**Quiz**\{{: .label .label-red\}}", "")
                    due_str = due_str.replace("+**Quiz**{: .label .label-red }", "")
                    due_str = due_str.replace(", **Reflection**{: .label .label-yellow }", "") # dont include it, since there's one for the final project
                    due_str = due_str.replace(", **CA**{: .label .label-blue }","" ) # there are none in Ch10 (Files)
                    #print(due_str)

                due_str = due_str.replace("**PA**", f"**PA{this_week}**").replace("**CA**", f"**CA{this_week}**").replace("**LA**", f"**LA{last_week}**").replace("Chapter X", "Chapter "+this_week)
                due_str = due_str.replace("Finish CA", f"Finish **CA{this_week}**")

                ### Remove an extra colon from the first line of each non-empty day
                due_str = due_str.replace(": :", ":")

                md_file.write(due_str + "\n\n")
            else:
                md_file.write(": [](#)\n\n")
        else:
            md_file.write(": [](#)\n\n")
        cur_day += 1

    if month == end_month and cur_day >= end_day:
        md_file.close()
        break # Finish processing

    md_file.close() # finish writing this week's dates
    week += 1
    if exclude_weekends:
        cur_day +=2
