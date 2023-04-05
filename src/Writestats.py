import time

def write():
    f = open("demofile2.txt", "a")
    f.write("/n")
    f.write("Date:")
    f.write("/n")
    f.write("Post Title:")
    f.write("/n")
    f.write("Current Follower Count:")
    f.write("/n")
    f.write("Current Like Total:")
    f.write("/n")
    f.write("Total # of Videos:")
    f.close()
