import datetime
class TODO:
    def __init__(self,ToDo):
        self.ToDo=ToDo

    def list_schedule(self):
        for list_schedules in ToDo:
            print(list_schedules)

    def Del_Task(self,Del_Task):
        if Del_Task in self.ToDo:
            print(Del_Task)
            self.ToDo.remove(Del_Task)

    def pending_tasks(self,pending_tasks):
        if pending_tasks in self.ToDo:
            print("complected tasks:")
            self.ToDo.remove(pending_tasks)

    def completed_tasks(self,completed_tasks):
        if completed_tasks in self.ToDo:
            print("pendig tasks")
            self.ToDo.remove(completed_tasks)

ToDo=[]
c=TODO(ToDo)
c.list_schedule()
b=datetime.datetime.today()
print(b)
a=input("Enter your 'TODAY SCHEDULE':")
ToDo.append(a)
while True:
    a=input("Enter your 'TODAY SCHEDULE':")
    ToDo.append(a)
    if a=="YES":
        while True:
            ch=input("Enter here..! what do you want in this ToDo App:")
            if ch == "schedule_list":
                c.list_schedule()
            elif ch== "Del_task":
                ToDo=input("Please enter delete task here:")
                c.Del_Task(ToDo)
            elif ch=="pending_task":
                ToDo=input("Please enter pending task here:")
                c.pending_tasks(ToDo)
            elif ch=="complected_task":
                ToDo=input("Please enter complected task here")
                c.completed_tasks(ToDo)
            else:
                print("Thank you for given this type of task It's helps to me learn new things at the same time improve my confidatent")
                quit()