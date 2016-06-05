/*
Crash-Mon daemon - Anto Joseph
*/

#include <sys/ptrace.h>
#include <sys/user.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <assert.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <signal.h>

int main(int argc, char* argv[]) {   


  pid_t child;


  char* chargs[argc];
  int i = 0;

  while (i < argc - 1) {
    chargs[i] = argv[i+1];
    i++;
  }

  chargs[i] = NULL;

  child = fork();
  if(child == 0) {

    // ur child goes here !!!
    fprintf(stderr,"tracing child process : %s\n",(char*)chargs[0]);
    execvp(chargs[0], chargs);

 
  } else {
    // ur parent goes here !!
    int status;
    fprintf(stderr,"parent   process monitoring for crashes in : %s\n",(char*)chargs[0]);
    while(waitpid(child, &status, 0) && ! WIFEXITED(status)) {
        if (WIFSIGNALED(status)){
          // It was terminated by a signal
            if (WTERMSIG(status) == SIGSEGV){
                fprintf(stderr,"SEGFAULT FOUND \n");

                //to do : dump register states of the child process
                //to do : dump mem info of the child process
                exit(0);
            }
      }
    }
  }
  exit(0);
}
