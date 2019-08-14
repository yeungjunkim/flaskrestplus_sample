#!/usr/bin/python
# -*- coding: utf-8 -*-

import git
import os
import sys
import time

if __name__ == "__main__":

        #for i in range(len(sys.argv)):
        #       print("sys.argv[%d] = '%s'" % (i, sys.argv[i])

        #repo = git.Repo.clone_from( URL_SOURCE, PATH_TARGET )


        if len(sys.argv) < 2:
                sys.exit('Usage: %s repository-name' % sys.argv[0])

        if not os.path.isdir(sys.argv[1]):
                sys.exit('ERROR: Repository %s was not found!' % sys.argv[1])


        PATH_TARGET = sys.argv[1]
        repo = git.Repo( PATH_TARGET )

        for remote in repo.remotes : 
                print ("test")
                #print("[ " + str(remote) + " branches ]"

                for branch in getattr(repo.remotes, str(remote)).refs:
                        print (" " + str(branch).replace( str(remote)+"/", "" ))

                        for commit in repo.iter_commits(branch, max_count=3):

                                print ("")
                                print ("         Commit          : ", commit)
                                print("         Author          : ", commit.author, ", (")
                                print(time.asctime(time.gmtime(commit.authored_date)), ")")
                                print("         Committer       : ", commit.committer, ", (")
                                print (time.asctime(time.gmtime(commit.committed_date)), ")")
                                print("         Encoding        : ", commit.encoding)
                                print("         Summary         : ", commit.summary)
                                print("         Delta LOC       : ", commit.stats.total['lines'], " (+")
                                print (commit.stats.total['insertions'], ", -")
                                print (commit.stats.total['deletions'], ")")
                                #print commit.stats.files
                                #print("                Message         : ", commit.message
                                #print("                Parents         : ", commit.parents

        print("")

        print("[ Local branches ]")
        for branch in repo.branches:
                print(" " + str(branch))

                #commits = list( repo.iter_commits(branch, max_count=10) )

                for commit in repo.iter_commits(branch, max_count=3):

                        print("")
                        print("         Commit          : ", commit)
                        print("         Author          : ", commit.author, ", (")
                        print (time.asctime(time.gmtime(commit.authored_date)), ")")
                        print("         Committer       : ", commit.committer, ", (")
                        print (time.asctime(time.gmtime(commit.committed_date)), ")")
                        print("         Encoding        : ", commit.encoding)
                        print("         Summary         : ", commit.summary)
                        print("         Delta LOC       : ", commit.stats.total['lines'], " (+")
                        print (commit.stats.total['insertions'], ", -")
                        print (commit.stats.total['deletions'], ")")
                        #print commit.stats.files
                        #print("                Message         : ", commit.message
                        #print("                Parents         : ", commit.parents
