def string_to_log(string, log):
    string = string.split()
    line = ''
    for i in string:
        if len(line + i + ' ') > 66:
            log.append(line)
            line = ''
        else:
            line += i
            line += ' '
        

log = []
string = 'Hello there hoiw aaioa daw awkaw awakw aawkaw awka waawkawaw kddawdaw dawdkawdaw dawdkawdaw dawdkaw dawd awdk awdk awdawk dakwd awk dawkd awkd awkd awdkaw dawk dawkd awkd awkd akwd kawd awd awkd awkd awk dkawd awkd aw awk'
string_to_log(string, log)

for i in log:
    print(i)