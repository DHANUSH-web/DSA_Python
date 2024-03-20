#include <iostream>
#include <cstring>
using namespace std;

const char* filter_string(const char* content) {
    int size = strlen(content);
    char* extracted_string = (char*)malloc(size);
    int i = 0, j = 0;

    for (i = 0; i < size; i++)
        if (isalpha(content[i]))
            extracted_string[j++] = tolower(content[i]);

    return extracted_string;
}

const bool is_palindrome(const char* content) {
    int size = strlen(content);

    for (int i = 0; i < size/2; i++)
        if (content[i] != content[size-i-1])
            return false;

    return true;
}

int main() {
    char* user_content = (char*)malloc(2000);
    
    cout << "Enter a string: ";
    cin.getline(user_content, 2000);

    const char* extracted_string = filter_string(user_content);
    cout << "Extracted String: " << extracted_string << endl;
    cout << (is_palindrome(extracted_string) ? "Yes, it is" : "No, it is not") << endl;
    return 0;
}