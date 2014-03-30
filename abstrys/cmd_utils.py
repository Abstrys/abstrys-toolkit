# Abstrys Command Line Utility library
#
# Provides classes and functions useful for writing command-line scripts.
import sys

def print_error(string):
    """Print an error message."""
    print "*** Dhop error: %s" % (string)
    return


def confirm(query):
    """Asks the user a Y/N question, and returns true/false depending on their
    answer."""
    answer = raw_input("%s (y/n): " % (query))
    return answer.lower() == 'y'


# adapted from http://www.python.org/dev/peps/pep-0257/
def format_doc(string, extra_indent=0, line_start=0, line_end=-1):
    """
    Remove significant leading space from all lines and return the resulting
    string."""

    if not string:
        return ''

    # Convert tabs to spaces and split into a list of lines:
    lines = string.expandtabs(4).splitlines()

    # Determine minimum indentation (first line doesn't count, and blank lines
    # don't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))

    # if line_end is negative, then set it to the last line in the list.
    if line_end == -1:
        line_end = len(lines)

    # put the lines together, removing the first num_spaces characters from
    # each line (except for line 0).
    result_text = ""

    if line_start == 0:
        result_text = lines[0] + '\n'
        line_start = 1

    # convert the extra indent number into spaces
    extra_indent = ' ' * extra_indent

    # add each line to the result.
    for cur_line in lines[line_start:line_end]:
        result_text += "%s%s\n" % (extra_indent, cur_line[indent:])

    return result_text


class TempMessage:
    """A class for displaying temporary (eraseable) messages.
    Typical use:
       a = TempMessage("some text")
       a.show()
       # something happens...
       a.erase()
       # continue onward!
    """
    text = ""
    erase_string = ""

    def set(self, text):
        """Sets the message text."""
        self.text = text
        l = len(text)
        e = '\b' * l
        self.erase_string = "%s%s%s" % (e, ' '*l, e)

    def __init__(self, text=""):
        """Initializes a TempMessage with some optional text"""
        self.set(text)

    def show(self, text=""):
        """Shows the existing message text, or sets and shows new text."""
        if text != "":
            self.set(text)
        sys.stdout.write(self.text)
        sys.stdout.flush()

    def erase(self):
        """Erase the current msg frame from sys.stdout."""
        sys.stdout.write(self.erase_string)
        sys.stdout.flush()

    def __len__(self):
        """Get the length of the msg frame, in characters."""
        return len(self.text)


class TwirlingProgressIndicator:
    """A console text-based twirling progress indicator."""
    temp_message = None

    def __init__(self):
        self.temp_message = TempMessage()
        self.progress_frames = ['-', '\\', '|', '/', '-', '\\', '|']
        self.progress_string = ' %s '
        self.progress_string_len = 3
        # self.cur_frame will be incremented to zero on the first get_next()
        self.cur_frame = -1

    def show(self):
        """Write the next progress frame to sys.stdout."""
        self.cur_frame += 1
        if self.cur_frame == len(self.progress_frames):
            self.cur_frame = 0
        self.temp_message.erase()
        self.temp_message.show(self.progress_string %
                self.progress_frames[self.cur_frame])

    def erase(self): self.temp_message.erase()


class ProgressBar:
    """A console text-based bar-style progress indicator."""
    progress_left_bound = '['
    progress_right_bound = ']'
    progress_fill = '#'
    bar_size = 0
    bar_percent = 0
    temp_message = None

    def __init__(self, size=10):
        self.temp_message = TempMessage()
        self.bar_size = size

    def show(self, percent=None):
        if percent:
            self.bar_percent = percent
        fill_amount = int((self.bar_percent * self.bar_size) / 100.0)
        self.temp_message.erase()
        self.temp_message.show('%s%s%s%s' % (self.progress_left_bound,
            self.progress_fill
            * int(fill_amount), ' ' * int(self.bar_size - fill_amount),
            self.progress_right_bound))

    def erase(self):
        self.temp_message.erase()
