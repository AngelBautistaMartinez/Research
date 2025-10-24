#include <stdio.h>
#include <windows.h>
#include <winhttp.h>
#include <iphlpapi.h> // -liphlpapi
#include <string.h>
#include <winsock2.h> //-lws2_32


typedef unsigned char BYTE;


void xorEncrypt(BYTE *data, size_t dataLen, const BYTE *key, size_t keyLen){
    for(size_t i = 0; i < dataLen; i++){
        data[i] ^= key[i % keyLen];
    }
}

int xorIP(char *ObfuscatedIP, size_t bufSize, const BYTE obf[], size_t obfLen) {
    BYTE temp[512];

    memcpy(temp, obf, obfLen);

    
    BYTE key[] = {
        0x3A, 0x7F, 0x01, 0xB2, 0xC3, 0x4D, 0x55, 0x99,
        0x10, 0xAB, 0xCD, 0xEF, 0x00, 0x11, 0x22, 0x33
    };

    
    xorEncrypt(temp, obfLen, key, sizeof(key));


    if (obfLen + 1 > bufSize) {
        SecureZeroMemory(temp, obfLen);
        SecureZeroMemory(key, sizeof(key));
        return -1;
    }

    
    memcpy(ObfuscatedIP, temp, obfLen);

    ObfuscatedIP[obfLen] = '\0';  

    
    SecureZeroMemory(temp, obfLen);
    SecureZeroMemory(key, sizeof(key));

    return 0;
}


int sendHTTPRequest(char *IP){

    //get a handle to a WinHTTP request
    HINTERNET hSession = WinHttpOpen(L"WinHTTP/1.0", WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY, WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0);

    if(!hSession){
        printf("Windows HTTP Handle error: %lu\n", GetLastError());
        return -1;
    }

    wchar_t wIP[256];
    mbstowcs(wIP, IP, sizeof(wIP)/sizeof(wIP[0]));


    //make a HTTP session handle by providing server info
    HINTERNET hConnect = WinHttpConnect(hSession, wIP, 5000, 0);

    if(!hConnect){
        printf("HTTP session handle error: %lu\n", GetLastError());
        WinHttpCloseHandle(hSession);
        return -1;
    }

    //HTTP request handle very basic js sends data
    HINTERNET hRequest = WinHttpOpenRequest(hConnect, L"POST", L"/send", NULL, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, 0);

    if(!hRequest){
        printf("HTTP request handle error: %lu\n", GetLastError());
        WinHttpCloseHandle(hConnect);
        WinHttpCloseHandle(hSession);
        return -1;
    }
    

    //json data we send to server
    

    // JSON payload
    const char *json = "{\"name\":\"\",\"msg\":\"Hello\"}";

    BOOL result = WinHttpSendRequest(hRequest,
                                       L"Content-Type: application/json\r\n",
                                       -1,
                                       (LPVOID)json,
                                       (DWORD)strlen(json),
                                       (DWORD)strlen(json),
                                       0);


    if(!result){
        printf("HTTP request failed. Error: %lu\n", GetLastError());
    }
    
    //close all handles 
    WinHttpCloseHandle(hConnect);
    WinHttpCloseHandle(hSession);
    WinHttpCloseHandle(hRequest);
    return 0;
}

void checkTCPConnections(char IP[65]){
    //structure to hold tcp table info

    int count = 0;

    PMIB_TCPTABLE tcpTable;
    DWORD size = 0;
    

    //ask tcp table how much memory do we need to allocate
    //NULL in struc tells the func "just tell me the size"
    //FALSE = dont sort
    GetTcpTable(NULL, &size, FALSE);
    //allocate the memory needed
    tcpTable = (PMIB_TCPTABLE)malloc(size);

    if(GetTcpTable(tcpTable, &size, FALSE) == NO_ERROR){
        //-> a pointer to a item in a structure
        

		for(int i = 0; i < tcpTable->dwNumEntries; i++){
			MIB_TCPROW row = tcpTable->table[i];

			if(row.dwState != MIB_TCP_STATE_ESTAB){
				continue;
			}

			struct in_addr addr;
            //putting raw number into winsock format
			addr.S_un.S_addr = row.dwRemoteAddr;
            //convert IP to string
			char* ip = inet_ntoa(addr);

            if(strcmp(ip, IP) == 0){
                printf("Connection Secured.\n");
            }

			if(strcmp(ip, "127.0.0.1") == 0){
				continue;
			}
			count++;

            printf("TCP REMOTE IP: %s\n", ip);
            
            
		}
    }else{
        printf("Error: %lu\n", GetLastError());
    }

    printf("TCP connections: %d\n", count);
    free(tcpTable); //clean up mem
}