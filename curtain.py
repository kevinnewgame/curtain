class Curtain:

    def __init__(self, n_slot, n_hook, hook_slot=4):
        n_gap = n_hook - 1
        self.container = [None] * (n_hook + n_gap)

        self.hook_slot = hook_slot
        self._n_slot = n_slot
        self._n_hook = n_hook

        self._idx = 0

    def arrange_hooks(self):
        self._idx = 0
        self._place_two_hooks()
        self._place_hooks()

    def _place_hooks(self):
        """If n_hook >= 2, place two gaps then two hooks in the order.
        If n_hook is 1, place one hook in the middle first then two gaps.
        """
        if self._n_hook == 0:
            self.container[self._idx] = self._n_slot
            return
        elif self._n_hook == 1:
            # place one hook in the middle
            self.container[self._idx + 1] = 'h'
            self._n_slot -= self.hook_slot
            self._place_two_gaps()
            return

        self._place_two_gaps()
        self._place_two_hooks()
        self._place_hooks()

    def _place_two_hooks(self):
        self.container[self._idx] = self.container[-(self._idx + 1)] = 'h'
        self._n_hook -= 2
        self._n_slot -= 2 * self.hook_slot
        self._idx += 1

    def _place_two_gaps(self):
        # calculate number of slots for hook gap
        n_gap = self._n_hook + 1
        if self._n_hook == 1:
            left_gap_slot = self._n_slot // 2
            right_gap_slot = self._n_slot - left_gap_slot
            self.container[self._idx] = left_gap_slot
            self.container[self._idx + 2] = right_gap_slot
        else:
            gap_slot = (self._n_slot - self.hook_slot * self._n_hook) // n_gap
            self.container[self._idx] = self.container[-(self._idx + 1)] = gap_slot
            self._n_slot -= 2 * gap_slot
        self._idx += 1


if __name__ == '__main__':
    curtain = Curtain(n_slot=82, n_hook=11)
    curtain.arrange_hooks()
    print(curtain.container)

    curtain = Curtain(n_slot=82, n_hook=10)
    curtain.arrange_hooks()
    print(curtain.container)
