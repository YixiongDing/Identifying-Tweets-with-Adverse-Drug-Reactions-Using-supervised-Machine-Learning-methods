input_file = open("train.txt", 'r')
#input_file = open("dev.txt", 'r')
#input_file = open("test.txt", 'r')
medication = ["fluoxetine","prozac","olanzapine","quetiapine",
        "trazodone","lamotrigine","effexor","vyvanse","cipro","rivaroxaban","venlafaxine",
     "seroquel","paxil","sertraline","lithium","viibryd","diazepam"]
symptom  = ["restless","obese","sick","addiction" ,"addict","painful" ,
        "munchies.","allergic","nose","paralysis","worse","pain","tired","panic","dizzy","awful","sleepy",
        "humungous","headache","hard","terrible","zombie","gain","feel","rash","syndrome","orgasm","tapering"]

def main():
    for line in input_file:
        line = line.split("\t")
        tweet_id  = line[0]
        tweet_class = line[1]
        tweet_text = line[2].strip("\n")
        drug_counter = 0
        symp_counter = 0
        words = tweet_text.split()
        for word in words:
            for check_word in medication:
                if word.lower().find(check_word) >0 or word.lower() == check_word :
                    drug_counter += 1

            for check_word in symptom:
                if word.lower() == check_word:
                    symp_counter += 1

        if drug_counter >0 and symp_counter>0:
            # print "%d %d %s %s\n " %(drug_counter, symp_counter, tweet_class,tweet_text)
             print "Y"
        else :
             print "N"
                    

if __name__ == "__main__":
    main()

