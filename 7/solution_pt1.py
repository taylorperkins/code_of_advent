import re


class Step(object):
    def __init__(self, name):
        self.name = name

        self.relies_on = set()
        self.finished = True

    def __repr__(self):
        """Helps me debug a bit"""
        return self.name


class OrderOfOps(object):

    def __init__(self):
        self.steps = dict()
        self.finished_steps = list()

    def add_step(self, step, relies_on=''):
        """Just build the steps and specify if they rely on another step before being started"""
        if step not in self.steps:
            self.steps[step] = Step(step)

        if relies_on:
            self.steps[step].relies_on.add(relies_on)
            self.steps[step].finished = False

    def determine_order(self):
        # so you can track when youre done
        original_step_len = len(self.steps)

        while len(self.finished_steps) != original_step_len:
            # Alphabetically sort (important)
            for key in sorted(self.steps):
                if self.steps[key].finished:
                    # marks everything appropriately so the next iteration picks up on the changes
                    self.finished_steps.append(key)

                    del self.steps[key]

                    # Since we just finished a step, it's important to go through the other steps specify that
                    # they no longer rely on the finished step
                    for step in self.steps.values():
                        if key in step.relies_on:
                            step.relies_on.remove(key)
                            if not step.relies_on:
                                step.finished = True

                    break

        # all there is
        return ''.join(self.finished_steps)


if __name__ == '__main__':
    """It was a bit tricky to figure this one out. It took a bit of brainpower to map out the "business rules" for 
    this problem.
    """
    with open('./input.txt') as f:
        data = f.read().splitlines()

    order_of_ops = OrderOfOps()

    # build out all of the steps and which ones require what. Then you can determine what order they need to
    # happen to be finished.
    pattern = re.compile(r'Step (?P<relies_on>[A-Z]) must be finished before step (?P<step>[A-Z])')
    for line in data:
        m = re.match(pattern, line)

        # two steps are either created or referenced in every line of the input.. so you have to create or update both
        step = m.group('step')
        relies_on = m.group('relies_on')

        order_of_ops.add_step(relies_on)
        order_of_ops.add_step(step, relies_on)

        print(step, relies_on)

    print(order_of_ops.determine_order())
