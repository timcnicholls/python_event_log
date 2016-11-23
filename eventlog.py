from collections import deque

class EventLog(deque):

    def __init__(self, max_len=None):
        deque.__init__(self)
        self.max_len = max_len

    def _full_append(self, event):
        deque.append(self, event)
        self.popleft()

    def append(self, event):
        deque.append(self, event)
        if len(self) == self.max_len:
            self.append = self._full_append

    def tolist(self):
        return list(self)


if __name__ == '__main__':

    max_len = 10
    event_log = EventLog(max_len)

    for event in ['one', 'two', 'three', 'four', 'five']:
        event_log.append(event)

    print event_log, len(event_log)
    for event in event_log:
        print event

    for event in ['six', 'seven', 'eight', 'nine', 'ten']:
        event_log.append(event)

    print event_log, len(event_log)
    for event in event_log:
        print event

    for event in ['eleven', 'twelve']:
        event_log.append(event)

    print event_log, len(event_log)
    for event in event_log:
        print event
