/*

   DEX Repair
   -----------------------------------------

   Anestis Bechtsoudis <anestis@census-labs.com>
   Copyright 2015 by CENSUS S.A. All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

*/

#include <sys/mman.h>
#include <string.h>
#include <fcntl.h>
#include <getopt.h>

#include "common.h"
#include "log.h"
#include "utils.h"
#include "dex.h"

/* Module global variables */
static int logLevel = l_INFO;

/* Help page */
static void usage(bool exit_success)
{
    printf("%s",
        "  " AB "-I,  --input-files=DIR" AC " : "
            "input files dirs (1 level recursion only) or single file\n"
        "  " AB "-h,  --help" AC "            : "
            "this help\n"
        "  " AB "-v,  --debug=LEVEL" AC "     : "
            "debug level (0 - FATAL ... 4 - DEBUG), default: '" AB "3" AC "' (INFO)\n" 
    );

    if (exit_success) exit(EXIT_SUCCESS);
    else exit(EXIT_FAILURE);
}

int main(int argc, char **argv)
{
    int c;

    /* Default values */
    infiles_t pFiles = {
        .inputFile = NULL,
        .files = NULL,
        .fileCnt = 0,
    };

    printf("\t\t"AB PROG_NAME" ver. "PROG_VERSION"\n\n"PROG_AUTHORS AC "\n\n");
    if (argc < 1) usage(true);

    struct option longopts[] = {
        {"input-files", required_argument, 0, 'I'}, 
        {"help",        no_argument,       0, 'h'},
        {"debug",       required_argument, 0, 'v'},
        //{"repair-sha",  no_argument,       0, 'S'}, /* TODO */
        {0,             0,                 0, 0  }
    };

    while (( c = getopt_long(argc, argv, "I:hv:S", longopts, NULL)) != -1) {
        switch (c) {
        case 'I':
            pFiles.inputFile = optarg;
            break;
        case 'h':
            usage(true);
            break;
        case 'v':
            logLevel = atoi(optarg);
            break;
        default:
            break;
        }
    }
    
    /* adjust log level */
    log_setMinLevel(logLevel);
    
    /* initialize input files */
    if (!utils_init(&pFiles)) {
        LOGMSG(l_FATAL, "Couldn't load input files");
        exit(EXIT_FAILURE);
    }
    
    size_t repairedCnt = 0;
    
    for (size_t f = 0; f < pFiles.fileCnt; f++) {
        off_t fileSz = 0;
        int srcfd = -1, dstfd = -1;
        uint8_t *buf = NULL;
        
        LOGMSG(l_DEBUG, "Repairing '%s'", pFiles.files[f]);
        
        /* mmap file */
        buf = utils_mapFileToRead(pFiles.files[f], &fileSz, &srcfd);
        if (buf == NULL) {
            LOGMSG(l_ERROR, "open & map failed for R/O mode. Skipping '%s'", 
                    pFiles.files[f]);
            continue;
        }
        
        if ((size_t)fileSz < sizeof(dexHeader)) {
            LOGMSG(l_WARN, "Invalid input file. Skipping '%s'", 
                    pFiles.files[f]);
            munmap(buf, fileSz);
            close(srcfd);
            continue;
        }
        
        const dexHeader *pDexHeader = (const dexHeader*)buf;

        /* Validate DEX magic number */
        if (!dex_isValidDexMagic(pDexHeader)) {
            LOGMSG(l_WARN, "Invalid magic number. Skipping '%s'", 
                    pFiles.files[f]);
            munmap(buf, fileSz);
            close(srcfd);
            continue;
        }
        
        /* Repair CRC */
        dex_repairDexCRC(buf, fileSz);
        
        char outFile[NAME_MAX] = { 0 };
        snprintf(outFile, NAME_MAX, "%s_repaired.dex", pFiles.files[f]);
        
        /* Write repaired file */
        dstfd = open(outFile, O_CREAT | O_EXCL | O_RDWR, 0644);
        if (dstfd == -1) {
            LOGMSG_P(l_ERROR, "Couldn't create output file '%s' in "
                    "input directory", outFile);
            munmap(buf, fileSz);
            close(srcfd);
            continue;
        }

        if (!utils_writeToFd(dstfd, buf, fileSz)) {
            munmap(buf, fileSz);
            close(srcfd);
            close(dstfd);
            LOGMSG(l_WARN, "Skipping '%s'", pFiles.files[f]);
            continue;
        }
        
        repairedCnt++;
        
        /* Clean-up */
        munmap(buf, fileSz);
        buf = NULL;
        close(srcfd);
        close(dstfd);
    }
    
    LOGMSG(l_INFO, "%u our of %u files have been successfully repaired", 
            repairedCnt, pFiles.fileCnt);
    LOGMSG(l_INFO, "Repaired DEX files available at '%s'", pFiles.inputFile);
    
    return EXIT_SUCCESS;
}