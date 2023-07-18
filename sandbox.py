
import githup as gp
import time

gp.create_file("my file", "txt", "Hello World", "local")

gp.init_repo("https://github.com/cyrilfrl/githup-sandbox", "noreadme", "local")
gp.commit_files("main", "hillu", "local")
