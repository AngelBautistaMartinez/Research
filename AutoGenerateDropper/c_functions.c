#include <stdio.h>
#include <string.h>
#include <windows.h>

typedef unsigned char BYTE;


void xor_encrypt(unsigned char *data, size_t dataLen, const unsigned char *key, size_t keyLen){ 
    for(size_t i = 0; i < dataLen; i++){ 
        data[i] ^= key[i % keyLen]; 
    } 
}

__declspec(dllexport) char* encrypt_ip(const char *text) {
    //key
    unsigned char key[] = {
        0x3A, 0x7F, 0x01, 0xB2, 0xC3, 0x4D, 0x55, 0x99,
        0x10, 0xAB, 0xCD, 0xEF, 0x00, 0x11, 0x22, 0x33
    };

    size_t textLen = strlen(text);
    unsigned char buffer[256];
    if (textLen > sizeof(buffer)) return NULL;

    memcpy(buffer, text, textLen);
    xor_encrypt(buffer, textLen, key, sizeof(key));

    // Each byte needs 6 characters: "0x%02X, "
    size_t resultLen = textLen * 6 + 1;
    char *result = (char *)malloc(resultLen);
    if (!result) return NULL;

    result[0] = '\0';
    for (size_t i = 0; i < textLen; ++i) {
        char temp[8];
        sprintf(temp, "0x%02X", buffer[i]);
        strcat(result, temp);
        if (i < textLen - 1) strcat(result, ", ");
    }

    return result;

}

__declspec(dllexport) void free_buffer(void *ptr){
    free(ptr);
}