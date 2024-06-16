<<<<<<< HEAD
#!/usr/bin/python3
import sys
=======
mport sys
>>>>>>> 66f9c4e411d7ea9546c0d7d105d83ec2a0f7d566

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
    if result is not None:
        print(len(result))
    else:
        print("None")
