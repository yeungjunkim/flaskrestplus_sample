from git import Repo
repo = Repo('.')  # if repo is CWD just do '.'

repo.index.add(['bla.txt'])
repo.index.commit('my commit description')
origin = repo.remote('origin')
origin.push()