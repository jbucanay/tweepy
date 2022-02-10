#tweets analyziser 
#find tweets that mention rams
#tweets that mention patriots
#tweets for both
#tweets that mention neither

import json
import string

def has_rams(str):
    rams_count = 0
    
def has_pats(str):
    pats_count = 0

def main():
    ffile = open('superbowltweets.json', 'r')
    jfile = json.loads(ffile.read())

    print(dir(string))

    # print(f'this is the first line for testing levels: {jfile[0]["full_text"]}')
    # print(f'second one hopefully: {jfile[1]["full_text"]}')













if __name__ == "__main__":
    main()