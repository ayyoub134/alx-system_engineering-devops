<<<<<<< HEAD
#!/usr/bin/python3
import sys
=======
mport sys
>>>>>>> 66f9c4e411d7ea9546c0d7d105d83ec2a0f7d566

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
