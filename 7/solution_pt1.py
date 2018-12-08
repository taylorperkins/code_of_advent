import re


class Step(object):
    def __init__(self, name):
        self.name = name

        self.relies_on = set()
        self.finished = True

    def __repr__(self):
        return self.name


class OrderOfOps(object):

    def __init__(self):
        self.steps = dict()
        self.finished_steps = list()

    def add_step(self, step, relies_on=''):
        if step not in self.steps:
            self.steps[step] = Step(step)

        if relies_on:
            self.steps[step].relies_on.add(relies_on)
            self.steps[step].finished = False

    def determine_order(self):
        original_step_len = len(self.steps)

        while len(self.finished_steps) != original_step_len:
            for key in sorted(self.steps):
                if self.steps[key].finished:
                    self.finished_steps.append(key)

                    del self.steps[key]

                    for step in self.steps.values():
                        if key in step.relies_on:
                            step.relies_on.remove(key)
                            if not step.relies_on:
                                step.finished = True

                    break

        return ''.join(self.finished_steps)


if __name__ == '__main__':
    with open('./input.txt') as f:
        data = f.read().splitlines()

    order_of_ops = OrderOfOps()

    pattern = re.compile(r'Step (?P<relies_on>[A-Z]) must be finished before step (?P<step>[A-Z])')
    for line in data:
        m = re.match(pattern, line)

        step = m.group('step')
        relies_on = m.group('relies_on')

        order_of_ops.add_step(relies_on)
        order_of_ops.add_step(step, relies_on)

        print(step, relies_on)

    print(order_of_ops.determine_order())
