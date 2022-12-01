def pytest_sessionfinish(session, exitstatus):
    session.config.exitstatus = exitstatus


def pytest_unconfigure(config):
    if config.exitstatus == 0:
        print(
            """
       __ 
    .-'  |
   /   <\\|
  /     \\'
  |_.- o-o
  / C  -._)\\
 /',        |
|   `-,_,__,'
(,,)====[_]=|
  '.   ____/
   | -|-|_
   |____)_)
        """
        )
