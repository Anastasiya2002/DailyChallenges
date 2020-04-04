#Complete the checkMagazine function in the editor below. It must print Yes
#if the note can be formed using the magazine, or No.

from collections import Counter
def checkMagazine(magazine, note):
    print(Counter(magazine) - Counter(note))
    if Counter(magazine)- Counter(note) =={}:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))