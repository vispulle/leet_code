"""
The problem is to reverse a Sentence exactly including spaces.
I/P: "Hi, How are you?" 
O/P: "you? are How, Hi"
"""
# we are not using a ny external libraries, time complexity: O(n), space is O(n)
def reverseString(string):
    buffer = []
    sub_buffer =''
    for i in string:
        if i == ' ':
            if len(sub_buffer):
                buffer.append(sub_buffer)
                sub_buffer = ''
            buffer.append(' ')
        else:
            sub_buffer += i
    buffer.append(sub_buffer)
    buffer.reverse()

    final = "".join(buffer)
    return final