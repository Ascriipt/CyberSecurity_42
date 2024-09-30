#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void ok() {
	puts("Good job.");
	return;
}

void no() {
	printf("Nope.");
	exit(1);
}

int main() {
	int ret;
	size_t len;
	char tmp[4];
	char val[9];
	char input[24];
	bool boule;

	printf("Please enter key: ");
	ret = scanf("%s23s", input);
	if (ret != 1)
		no();
	if (input[0] != '0')
		no();
	if (input[1] != '0')
		no();
	fflush(0);
	memset(val, 0, 9);
	val[0] = 'd';
	tmp[3] = 0;
	int i = 2;
	int j = 1;
	while (1) {
		boule = false;
		if (strlen(val) < 8) {
			len = i;
			boule = len < strlen(input);
		}
		if (boule != true)
			break;
		tmp[0] = input[i];
		tmp[1] = input[i + 1];
		tmp[2] = input[i + 2];
		val[j] = atoi(tmp);
		i += 3;
		j += 1;
	}
	if (strcmp(val, "delabere") == 0)
		ok();
	else
		no();
	return 0;
}