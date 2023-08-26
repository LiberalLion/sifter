#!/usr/bin/env python3
CVIOLET = '\33[35m'
CGREENBG2  = '\33[104m'
CRED = '\033[91m'
CBLUE = '\33[94m'
CYELLOW = '\33[33m'
CEND = '\033[0m'
UGREEN = '\33[92m'
WHITE = '\33[37m'
def showbanner():
        print(CVIOLET + '''
                 ____.__  ________         __ _________  ______
           _____/_   |  | \_____  \  _____/  |\______  \/  __  \\
  ______  /  ___/|   |  |   _(__  < /    \   __\  /    />      <   ______
 /_____/  \___ \ |   |  |__/       \   |  \  |   /    //   --   \ /_____/
         /____  >|___|____/______  /___|  /__|  /____/ \______  /
              \/       ''' + WHITE + "Gemin1" + CEND + " " + CVIOLET + '''    \/    \/      ''' + UGREEN + "Version" + CBLUE + " 10" + CEND + CVIOLET + '''    \/    ''' + CEND)
        print(
            f"                                  {CYELLOW}Revision {CBLUE}1{CEND}                                                  "
        )
showbanner()