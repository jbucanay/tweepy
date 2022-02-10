#tweets analyziser 
#find tweets that mention rams
#tweets that mention patriots
#tweets for both
#tweets that mention neither

import json


def has_rams(strng):
    lower_str = strng.lower()
    return lower_str.count('rams')
    
def has_pats(strng):
    lower_str = strng.lower()
    return lower_str.count('patriots')

def main():
    ffile = open('superbowltweets.json', 'r')
    jfile = json.loads(ffile.read())

    rams_count = 0
    pats_count = 0
    both_count = 0
    neither_count = 0
    
    
    for item in jfile:
        full_tweet = item['full_text']
        print(full_tweet)
        if has_rams(full_tweet) > 0:
            rams_count += 1
        if has_pats(full_tweet) > 0:
            pats_count += 1
        if has_pats(full_tweet) > 0 and has_rams(full_tweet) > 0:
            both_count +=1
        elif has_pats(full_tweet) <= 0 and has_rams(full_tweet) <= 0:
            neither_count +=1
    print(f'{rams_count} Tweets mentioned Rams in them')
    print(f'{pats_count} Tweets mentioned Patriots in them')
    print(f'{rams_count} Tweets mentioned Rams and Patriots in them')
    print(f'{neither_count} Tweets did not mentioned Rams nor Patriots ')

        
    
    
    













if __name__ == "__main__":
    main()