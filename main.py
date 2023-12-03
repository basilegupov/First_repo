import sys


def parse_args():
    result =""
    
    if len(sys.argv)>1:
        result += sys.argv[1]
        for count in range(2,len(sys.argv)):
            result+=' '+sys.argv[count]
            
    return result

print(parse_args())
