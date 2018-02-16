import sys
import webget

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for url in sys.argv[1:]:
            webget.download(url)
        sys.exit()
    else:
        input_lines = sys.stdin.read().split("\n")
        for line in input_lines:
            webget.download(line)
