input_file = open("train.txt", 'r')
#input_file = open("dev.txt", 'r')
#input_file = open("test.txt", 'r')
check_list1 = ["make","makes","made","making"]
check_list2 = ["me","you","him","her","my"]
def main():
    for line in input_file:
        line = line.split("\t")
        tweet_id  = line[0]
        tweet_class = line[1]
        tweet_text = line[2].strip("\n")
        words = tweet_text.split()
        counter = 0
        default = "N"
        for word in words:
            counter += 1
            if word in check_list1 and words[counter] in check_list2:
               # print "%s %s\n" %(tweet_class,tweet_text)
                default = "Y"
                break
        print default

if __name__ == "__main__":
    main()


