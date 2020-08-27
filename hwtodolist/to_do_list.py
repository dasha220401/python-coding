import json
from datetime import datetime


class Item:
    def __init__(self, done, info, last_updated, dead_line, delta_time):
        self.done = done
        self.info = info
        self.dead_line = dead_line
        self.last_updated = last_updated
        self.delta_time = delta_time

    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'dead_line': str(self.dead_line),
            'last_updated': str(self.last_updated),
            'delta_time': str(self.delta_time),
        }

    def __repr__(self):
        return self.info


class TodoList:
    def __init__(self, name, owner, ):
        self.name = name
        self.owner = owner
        # self.file_name = 'tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(f'{self.name}.json', 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item['done'], item['info'], item['last_updated'], item['dead_line'], item['delta_time']))
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\t  {item.dead_line}\t {item.last_updated}\t {item.delta_time}'
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.done:
                tasks += f'\n {item.done}\t {item.info}\t {item.last_updated}\t {item.dead_line}\t {item.delta_time}'
        return tasks

    def done_task(self, index):
        task = self.tasks[index]
        task.done = True
        task.last_updated = datetime.datetime.now()
        task.delta_time = None

    def undone_task(self, index):
        task = self.tasks[index]
        task.done = False
        task.last_updated = datetime.datetime.now()


    def add_task(self, task):
            self.tasks.append(task)

     def get_task_index(self, task):
            return self.tasks.index(task)

     def to_json(self):
          with open(f'{self.name}.json', 'w') as file:
            tasks = []
             for task in self.tasks:
                tasks.append(task.as_dict())
             json.dump(tasks, file, indent=4)

def init_todo_list():
    list_name = input('list_name')
    owner = input('Owner:')
    return TodoList(list_name, owner)

def main():
    todo_list = init_todo_list()
    try:
        while True:
            action = input('Choose your action - add tasks ("add"; view ("tasks") or , '
                           '("tasks_not_ready"), note("done_task"); exit ("exit"): ')
            if action == 'add':
                done = input('Choose status of action ("1 or 0"): ')
                if done not in {'1', '0'}:
                    continue
                done = bool(int(done))
                info = input('Which task is it?: ')
                dead_line_entry = input('Enter deadline in YYYY-MM-DD HH:MM format: ')
                dead_line = datetime.strptime(dead_line_entry, "%Y-%m-%d %H: %M")
                now = datetime.now()
                last_updated = now.strftime("%Y-%m-%d %H:%M")
                delta_time = str(dead_line - now)
                todo_list.add_task(Item(done, info, last_updated, dead_line, delta_time))
              elif action == 'tasks':
                 print(todo_list.tasks_list)
              elif action == 'tasks_not_ready':
                 print(todo_list.not_ready_tasks)
              elif action == 'done_task':
                  index = int(input('Chose index of the task that you have done: '))
                  todo_list.done_task(index)

              elif action == 'exit':
                   todo_list.to_json()
                   return
except Exception:
    todo_list.to_json()


if __name__ == '__main__':
    main()










