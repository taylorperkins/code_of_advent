import re
from collections import deque


class MarbleMania:
    def __init__(self, num_players, final_marble):
        # I dont really need a hash lookup since the players are going to be rotating
        # It's a bit simpler to just keep track of the players score as it becomes their turn
        # and add it up there
        self.players = deque([[i + 1, 0] for i in range(num_players)])

        # Dont go past this marble
        self.final_marble = final_marble

        # start with one marble in the middle of the circle
        self.marbles = deque([0])

    def start(self):
        # the first marble is already established on init, start at 1
        for marble in range(1, self.final_marble + 1):
            if marble % 23 == 0:
                self.special_move(marble=marble)
            else:
                self.normal_move(marble=marble)

        return self.get_player_scores()

    def next_player(self):
        # clockwise
        self.players.rotate(-1)

    def normal_move(self, marble):
        """No one gets any points, no marbles are removed.
        Marbles are rotated, and the new marble is inserted at the 0 index, making it the current marble.

        :return: None
        """
        # clockwise
        self.marbles.rotate(-2)
        self.marbles.appendleft(marble)

        self.next_player()

        self.print_status(marble)

    def special_move(self, marble):
        # current player
        player_id, score = self.players.popleft()

        # add marble to players score
        score += marble

        # remove marble 7 marbles counter-clockwise and add to players score
        self.marbles.rotate(7)
        score += self.marbles.popleft()

        # put the player back and rotate players
        self.players.appendleft([player_id, score])
        self.next_player()

        self.print_status(marble)

    def print_status(self, marble):
        # print('{0}: {1:<5}'.format(marble, str(self.marbles)))
        pass

    def get_player_scores(self):
        player_id, score = sorted(self.players, key=lambda x: x[1], reverse=True)[0]
        print('\n{0}: {1:<5}'.format(player_id, str(score)))

        return player_id, score


if __name__ == '__main__':
    # pattern = re.compile('^(?P<player_count>\d+) players; last marble is worth (?P<last_marble>\d+) points: high score is (?P<high_score>\d+)')
    pattern = re.compile('^(?P<player_count>\d+) players; last marble is worth (?P<last_marble>\d+) points')

    with open('./input.txt') as f:
        for line in f.read().splitlines():
            m = re.match(pattern, line)

            game_1 = MarbleMania(
                num_players=int(m.group('player_count')),
                final_marble=int(m.group('last_marble')))

            game_1_player_id, game_1_score = game_1.start()
            # assert score == int(m.group('high_score'))

            # part 2..
            game_2 = MarbleMania(
                num_players=int(m.group('player_count')),
                final_marble=int(m.group('last_marble')) * 100)  # might be crazy!

            game_2_player_id, game_2_score = game_2.start()
