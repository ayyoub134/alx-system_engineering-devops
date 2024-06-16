<<<<<<< HEAD
#!/usr/bin/python3
import sys
=======
mport sys
>>>>>>> 66f9c4e411d7ea9546c0d7d105d83ec2a0f7d566


if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
