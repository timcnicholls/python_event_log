from collections import deque
from uuid import uuid1
import datetime

class Event(object):

    def __init__(self, event=None, uuid=None):

        if uuid is not None:
            self.uuid = uuid
        else:
            self.uuid = uuid1()

        self.time = datetime.datetime.fromtimestamp((self.uuid.time - 0x01b21dd213814000L)*100/1e9)
        self.event = event

    def __hash__(self):
        return hash(self.uuid)

    def __eq__(self, other):

        return isinstance(other, type(self)) and (self.uuid == other.uuid)

    def __str__(self):

        return str(self.event)

class EventLogBuffer(deque):

    def __init__(self, max_len=None):
        deque.__init__(self)
        self.max_len = max_len

    def _full_append(self, event):
        deque.append(self, Event(event))
        self.popleft()

    def append(self, event):
        deque.append(self, Event(event))
        if len(self) == self.max_len:
            self.append = self._full_append

    def tolist(self):
        return list(self)

    def __contains__(self, uuid):

        e = Event(uuid=uuid)
        for event in self:
            if e == event:
                return True
        return False

def testEvent():

    e = Event("This is an event")
    print e.uuid, hash(e), hash(e.uuid)
    print e.time, e.time.strftime('%X %x %Z')
    print e.event

    f = Event(uuid=e.uuid)
    print f.uuid, hash(f), hash(f.uuid)

    print f == e

def testEventLogBuffer():

    max_len = 10
    event_log_buffer = EventLogBuffer(max_len)

    for event in ['one', 'two', 'three', 'four', 'five']:
        event_log_buffer.append(event)

    print event_log_buffer, len(event_log_buffer)
    for event in event_log_buffer:
        print event

    for event in ['six', 'seven', 'eight', 'nine', 'ten']:
        event_log_buffer.append(event)

    print event_log_buffer, len(event_log_buffer)
    for event in event_log_buffer:
        print event

    for event in ['eleven', 'twelve']:
        event_log_buffer.append(event)

    print event_log_buffer, len(event_log_buffer)
    for event in event_log_buffer:
        print event.uuid, event

    event0 = event_log_buffer[0].uuid
    event1 = Event("not in buffer")
    print event0 in event_log_buffer
    print event1 in event_log_buffer

if __name__ == '__main__':

    testEvent()
    testEventLogBuffer()
