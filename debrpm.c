#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argn, char *argv[]) {
    if((argv[1][0] == '-' && argv[1][1] == 'h')||(argv[1][0] == '-' && argv[1][1] == '-' && argv[1][2] == 'h' && argv[1][3] == 'e' && argv[1][4] == 'l' && argv[1][5] == 'p')) {
        printf("\033[;32mUsage\033[0m: debrpm [OPTIONS]\n");
        printf("\n\t-h, --help\t\tPrint this help message\n");
        printf("\t-di, --deb-install [FILE.].deb\tInstall the [FILE].deb packet\n");
        printf("\t-ri, --rpm-install [FILE.].rpm\tInstall the [FILE].rpm packet\n\n");
        printf("The file that have been added to your system are saved in the /var/log/gentoodebrpm directory.\n");
    }
    if((argv[1][0] == '-' && argv[1][1] == 'd' && argv[1][2] == 'i')||(argv[1][0] == '-' && argv[1][1] == '-' && argv[1][2] == 'd' && argv[1][3] == 'e' && argv[1][4] == 'b' && argv[1][5] == '- '&& argv[1][6] == 'i' && argv[1][7] == 'n' && argv[1][8] == 's' && argv[1][9] == 't' && argv[1][10] == 'a' && argv[1][11] == 'l' && argv[1][12] == 'l')) {
        printf("Installing the \033[1;31m%s\033[0m file.\n", argv[2]);
        char command[100] = "sudo ar x ";
        char command2[100] = "sudo tar xpvf /data.tar.xz >> /var/log/debrpm/";
        strcat(command, argv[2]);
        strcat(command2, argv[2]);
        system(command);
        system("sudo rm debian-binary control.tar.xz");
        system("sudo mv data.tar.xz /");
        system(command2);
    }
    if((argv[1][0] == '-' && argv[1][1] == 'r' && argv[1][2] == 'i')||(argv[1][0] == '-' && argv[1][1] == '-' && argv[1][2] == 'r' && argv[1][3] == 'p' && argv[1][4] == 'm' && argv[1][5] == '- '&& argv[1][6] == 'i' && argv[1][7] == 'n' && argv[1][8] == 's' && argv[1][9] == 't' && argv[1][10] == 'a' && argv[1][11] == 'l' && argv[1][12] == 'l')) {
        printf("Available soon\n");
    }
    return 0;
}
