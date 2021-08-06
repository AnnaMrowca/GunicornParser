from optparse import OptionParser
from datetime import datetime
from os import error
import sys


def read_file(fileName):
    try:
        with open(fileName) as file:
            content = file.read().splitlines()[1:]
    except FileNotFoundError as e:
        print('Wrong file name: {}'.format(e))
        sys.exit()
    else:
        return content

#parsing arguments from cmd
parser = OptionParser()
parser.add_option("-f", "--from", help="Parse FROM date", dest='fromDate')
parser.add_option("-t", "--to", help="Parse TO date", dest='toDate')
(options, args) = parser.parse_args()
# options - dict
# args - list of args without flag
#checking if the file name was passed in the cmd
if args:
    file = args[0]
else:
    print('You need to pass in name of the file you want to parse.')
    sys.exit()


#preparing all statictics when without no data frames (--from and --to) are given
if options.fromDate is None and options.toDate is None:
    content = read_file(file)
    iteration = 0
    logs = []#for counting req/sec
    codes = {}#for counting each type od response ex:{'200':10,'404':2}
    sizes = []#for counting avg size of response
    for line in content:
        code = line.split(' ')[13]
        if code == '200':
            sizeOfResponse = int(line.split(' ')[-1])
            sizes.append(sizeOfResponse)
        try:
            codes[code] += 1
        except KeyError:
            codes[code] = 1
        lineDate = datetime.strptime(line.split(' ')[8], '[%d/%b/%Y:%H:%M:%S')
        #checking if it's the first iteration
        if iteration == 0:
            lineBefore = ''
        else:
            lineBefore = content[iteration-1]

        if lineBefore:
            beforeDate = datetime.strptime(lineBefore.split(' ')[
                                           8], '[%d/%b/%Y:%H:%M:%S')
            if lineDate == beforeDate:
                logsInSec += 1
            else:
                logs.append(logsInSec)
                logsInSec = 1
        else:
            logsInSec = 1

        iteration += 1
    print('Requests: {}'.format(len(content)))
    print('Requests/sec: {}'.format(round(sum(logs)/len(logs), 2)))
    print('Responses: {}'.format(codes))
    print('Avg size of 2xx responses: {} Mb'.format(
        round(sum(sizes)/len(sizes)/1024/1024, 2)))


#preparing all statistics when dataframes (--from and --to) are given
elif options.fromDate and options.toDate:
    fromDate = datetime.strptime(options.fromDate, '%d-%m-%Y_%H-%M-%S')
    toDate = datetime.strptime(options.toDate, '%d-%m-%Y_%H-%M-%S')
    content = read_file(file)
    logCount = 0
    iteration = 0
    start = 0  # starting iteration in beetwen dates --from and --to
    logs = []
    codes = {}
    sizes = []
    for line in content:
        lineDate = datetime.strptime(line.split(' ')[8], '[%d/%b/%Y:%H:%M:%S')
        if lineDate >= fromDate and lineDate <= toDate:
            code = line.split(' ')[13]
            if code == '200':
                sizeOfResponse = int(line.split(' ')[-1])
                sizes.append(sizeOfResponse)
            try:
                codes[code] += 1
            except KeyError:
                codes[code] = 1
            logCount += 1
            if start == 0:
                lineBefore = ''
            else:
                lineBefore = content[iteration-1]

            if lineBefore:
                beforeDate = datetime.strptime(lineBefore.split(' ')[
                    8], '[%d/%b/%Y:%H:%M:%S')
                if lineDate == beforeDate:
                    logsInSec += 1
                else:
                    logs.append(logsInSec)
                    logsInSec = 1
            else:
                logsInSec = 1
            start += 1
        elif lineDate < fromDate:
            logs.append(logsInSec)
            break
        iteration += 1

    print('Requests: {}'.format(logCount))
    print('Requests/sec: {}'.format(round(sum(logs)/len(logs), 2)))
    print('Responses: {}'.format(codes))
    print('Avg size of 2xx responses: {} Mb'.format(
        round(sum(sizes)/len(sizes)/1024/1024, 2)))

#preparing all statictics when only --from dataframe is given
elif options.fromDate:
    fromDate = datetime.strptime(options.fromDate, '%d-%m-%Y_%H-%M-%S')
    content = read_file(file)
    logCount = 0
    iteration = 0
    start = 0  
    logs = []
    codes = {}
    sizes = []
    for line in content:
        lineDate = datetime.strptime(line.split(' ')[8], '[%d/%b/%Y:%H:%M:%S')
        if lineDate >= fromDate:
            code = line.split(' ')[13]
            if code == '200':
                sizeOfResponse = int(line.split(' ')[-1])
                sizes.append(sizeOfResponse)
            try:
                codes[code] += 1
            except KeyError:
                codes[code] = 1
            logCount += 1
            if start == 0:
                lineBefore = ''
            else:
                lineBefore = content[iteration-1]

            if lineBefore:
                beforeDate = datetime.strptime(lineBefore.split(' ')[
                    8], '[%d/%b/%Y:%H:%M:%S')
                if lineDate == beforeDate:
                    logsInSec += 1
                else:
                    logs.append(logsInSec)
                    logsInSec = 1
            else:
                logsInSec = 1
            start += 1
        elif lineDate < fromDate:
            logs.append(logsInSec)
            break
        iteration += 1

    print('Requests: {}'.format(logCount))
    print('Requests/sec: {}'.format(round(sum(logs)/len(logs), 2)))
    print('Responses: {}'.format(codes))
    print('Avg size of 2xx responses: {} Mb'.format(
        round(sum(sizes)/len(sizes)/1024/1024, 2)))

#preparing all statictics when only --to dataframe is given
elif options.toDate:
    toDate = datetime.strptime(options.toDate, '%d-%m-%Y_%H-%M-%S')
    content = read_file(file)
    logCount = 0
    iteration = 0
    start = 0  
    logs = []
    codes = {}
    sizes = []
    for line in content:
        lineDate = datetime.strptime(line.split(' ')[8], '[%d/%b/%Y:%H:%M:%S')
        if lineDate <= toDate:
            code = line.split(' ')[13]
            if code == '200':
                sizeOfResponse = int(line.split(' ')[-1])
                sizes.append(sizeOfResponse)
            try:
                codes[code] += 1
            except KeyError:
                codes[code] = 1
            logCount += 1
            if start == 0:
                lineBefore = ''
            else:
                lineBefore = content[iteration-1]

            if lineBefore:
                beforeDate = datetime.strptime(lineBefore.split(' ')[
                    8], '[%d/%b/%Y:%H:%M:%S')
                if lineDate == beforeDate:
                    logsInSec += 1
                else:
                    logs.append(logsInSec)
                    logsInSec = 1
            else:
                logsInSec = 1
            start += 1
        if iteration == len(content)-1:
            logs.append(logsInSec)
        iteration += 1

    print('Requests: {}'.format(logCount))
    print('Requests/sec: {}'.format(round(sum(logs)/len(logs), 2)))
    print('Responses: {}'.format(codes))
    print('Avg size of 2xx responses: {} Mb'.format(
        round(sum(sizes)/len(sizes)/1024/1024, 2)))
