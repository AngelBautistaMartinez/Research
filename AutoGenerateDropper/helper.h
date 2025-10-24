#define BIN		 256
#define IDR_BIN1 101

// Next default values for new objects
// 
#ifdef APSTUDIO_INVOKED
#ifndef APSTUDIO_READONLY_SYMBOLS
#define _APS_NEXT_RESOURCE_VALUE        102
#define _APS_NEXT_COMMAND_VALUE         40001
#define _APS_NEXT_CONTROL_VALUE         1001
#define _APS_NEXT_SYMED_VALUE           101
#endif
#endif
#ifndef HELPER_H
#define HELPER_H

#include <stddef.h>

typedef unsigned char BYTE;

#ifdef __cplusplus
extern "C" {
#endif
    

    int sendHTTPRequest(char *IP);
    int xorIP(char *ObfuscatedIP, size_t bufSize, const BYTE obf[], size_t obfLen);
    void checkTCPConnections(char IP[65]);



#ifdef __cplusplus
}
#endif
#endif