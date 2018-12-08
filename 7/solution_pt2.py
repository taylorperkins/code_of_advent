import re
letters = list(map(chr, range(65, 91)))


class Step(object):
    def __init__(self, name):
        self.name = name

        # steps needed to be complete before work can begin
        self.relies_on = set()

        # worker assigns as finished after checking it's state
        self.finished = False

        # ready to be picked up by a worker
        self.available = True

        self.seconds_to_complete = letters.index(name) + 61

    def __repr__(self):
        return self.name


class Workers(object):
    def __init__(self, num_workers):
        self.available_workers = num_workers
        self.status = 'available'

        self.work_load = list()

    def pick_up_task(self, step):
        if self.available_workers:
            self.work_load.append(step)
            self.available_workers -= 1
            self.status = 'busy'

    def work_on_tasks(self):
        updated_workload = list()
        finished_steps = list()

        for step in self.work_load:
            step.seconds_to_complete -= 1

            # it's finished
            if not step.seconds_to_complete:
                step.finished = True
                finished_steps.append(step.name)
                self.available_workers += 1

            else:
                updated_workload.append(step)

        self.work_load = updated_workload
        return finished_steps

    def workers_available(self):
        return self.available_workers > 0

    def get_work_queue(self):
        return [step.name for step in self.work_load]


class OrderOfOps(object):

    def __init__(self, num_workers):
        self.steps = dict()
        self.finished_steps = list()

        self.workers = Workers(num_workers=num_workers)

    def add_step(self, step, relies_on=''):
        if step not in self.steps:
            self.steps[step] = Step(step)

        if relies_on:
            self.steps[step].relies_on.add(relies_on)
            self.steps[step].available = False

    def determine_order(self):
        original_step_len = len(self.steps)

        seconds = 0
        while len(self.finished_steps) != original_step_len:
            if self.workers.workers_available():
                available_steps = self.get_available_steps()

                for step in available_steps:
                    if step.name not in self.workers.get_work_queue() and self.workers.workers_available():
                        self.workers.pick_up_task(step)

            self.workers.work_on_tasks()
            self.finish_steps()
            seconds += 1

        return ''.join(self.finished_steps), seconds

    def finish_steps(self):
        for key, step in self.steps.items():
            if step.finished:
                self.finished_steps.append(key)

                del self.steps[key]

                # remove all instances of steps that rely on the finished key
                for step in self.steps.values():
                    if key in step.relies_on:
                        step.relies_on.remove(key)

                        if not step.relies_on:
                            step.available = True

                return

    def get_available_steps(self):
        return [step for key, step in sorted(self.steps.items(), key=lambda x: x[0]) if step.available]


if __name__ == '__main__':
    with open('./input.txt') as f:
        data = f.read().splitlines()

    order_of_ops = OrderOfOps(num_workers=5)

    pattern = re.compile(r'Step (?P<relies_on>[A-Z]) must be finished before step (?P<step>[A-Z])')
    for line in data:
        m = re.match(pattern, line)

        step = m.group('step')
        relies_on = m.group('relies_on')

        order_of_ops.add_step(relies_on)
        order_of_ops.add_step(step, relies_on)

        print(step, relies_on)

    # higher than 236..
    print(order_of_ops.determine_order())
