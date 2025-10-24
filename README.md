For SQLite make "C:\flask_data" dir <br><br>
Docker: docker run -p 5000:5000 -v C:\flask_data:/data flaskserver <br><br>
Compile: gcc -c helper.c -o helper.o g++ -c replace.cpp -o replace.o g++ replace.o helper.o -o replace.exe -lwinhttp -liphlpapi -lws2_32 <br><br>
Auto Generate can auto compile the file too if needed.<br><br>

How to generate dropper:<br><br>
1.Enter of the name you want your dropper to be called (no need to add .cpp)<br><br>
2.Enter the IP's you want to be embedded into the dropper.<br><br>
  The First IP is just for strings the second IP is the real Server and the last one is for disassembling<br>
  Then your dropper.cpp file should be ready to go<br><br>
<br>
<img width="1165" height="393" alt="Screenshot 2025-10-23 170948" src="https://github.com/user-attachments/assets/38b21f69-4def-4c20-820f-edf0f9452495" />
<br>
<br>
3.It will ask if you want to auto compile the file (with g++/gcc) you can pick yes or no<br><br>
4.Then you should get your dropper.exe file ready to go.
<br>
<br>
<img width="1601" height="844" alt="Screenshot 2025-10-23 171012" src="https://github.com/user-attachments/assets/56bfd550-9012-4b37-a6bd-c22aed424c3b" />
