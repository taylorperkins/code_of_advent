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

        self.work_load = list()

    def pick_up_task(self, step):
        # pass a step to a worker, given that there is one just sitting around
        if self.available_workers:
            self.work_load.append(step)
            self.available_workers -= 1

    def work_on_tasks(self):
        # whip it. Create a new list now that a second has passed based on step status updates
        updated_workload = list()
        finished_steps = list()

        for step in self.work_load:
            # update the steps second requirement
            step.seconds_to_complete -= 1

            # it's finished
            if not step.seconds_to_complete:
                step.finished = True
                finished_steps.append(step.name)

                # unassign the step from the worker
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

        # Outsource ittttt
        self.workers = Workers(num_workers=num_workers)

    def add_step(self, step, relies_on=''):
        if step not in self.steps:
            self.steps[step] = Step(step)

        if relies_on:
            self.steps[step].relies_on.add(relies_on)
            self.steps[step].available = False

    def determine_order(self):
        """This is pretty similar to pt 1, but now it passes off a lot of status handling to a worker to deal with.
        It keeps going until it has gone through all of the steps."""
        original_step_len = len(self.steps)

        # initial second count
        seconds = 0
        while len(self.finished_steps) != original_step_len:
            # need to check if I even have workers I can use
            if self.workers.workers_available():
                # see if the workers have finished any steps
                available_steps = self.get_available_steps()

                for step in available_steps:
                    if step.name not in self.workers.get_work_queue() and self.workers.workers_available():
                        # if there is a step that can be worked on, and workers are available, pass off the step
                        self.workers.pick_up_task(step)

            # always make sure the worker does what hes supposed to
            self.workers.work_on_tasks()

            # make sure that for any step that just got finished, the other steps no longer rely on it.
            # Also removes the finished step from the queue
            self.finish_steps()
            seconds += 1

        return ''.join(self.finished_steps), seconds

    def finish_steps(self):
        # marks everything appropriately so the next iteration picks up on the changes
        for key, step in self.steps.items():
            if step.finished:
                self.finished_steps.append(key)

                # take it out of the queue
                del self.steps[key]

                # Since we just finished a step, it's important to go through the other steps specify that
                # they no longer rely on the finished step
                for step in self.steps.values():
                    if key in step.relies_on:
                        step.relies_on.remove(key)

                        # mark it as available for a worker to pick up
                        if not step.relies_on:
                            step.available = True

                return

    def get_available_steps(self):
        return [step for key, step in sorted(self.steps.items(), key=lambda x: x[0]) if step.available]


if __name__ == '__main__':
    """This one was definitely more complicated than the first one. There are a lott of moving parts.. So 
    I decided to really separate it into each individual piece: Step, Workers, and OrderOfOps
    
    Each step really only handles maintaining different statuses.
    Workers are responsible for updating the steps statuses as seconds go by.
    OrderOfOps is responsible for supplying the workers with available steps to complete and moving the steps along.
    """
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
