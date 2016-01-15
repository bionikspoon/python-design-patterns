#!/usr/bin/env python
# coding=utf-8
from textwrap import dedent


def output_parser(log_lines):
    state = 'header'
    program, end_time, send_failure = None, None, False

    for line in log_lines:
        if state == 'header':
            program = line.split(', ', 1)[0]
            state = 'body'
        elif state == 'body':
            if 'send_failure' in line:
                send_failure = True

            if '======' in line:
                state = 'footer'
        elif state == 'footer':
            end_time = line.split(', ', 1)[0]
    return program, end_time, send_failure


if __name__ == '__main__':
    sample_log = dedent("""
        turtles, turtles are real!
        log line 1: I like turtles
        log line 2: send_failure
        =====================
        30th Jul 2016, END
    """)[1:]

    print(output_parser(sample_log.splitlines(False)))
