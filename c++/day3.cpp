#include <fstream>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::fstream myFile;
    int result = 0, result2 = 0;

    myFile.open("../inputs/input3.txt", std::ios::in);
    if (myFile.is_open()) {
        std::string line;
        while (std::getline(myFile, line)) {
            int middle = line.length() / 2;
            size_t currentIndex = 0;
            std::set<char> s1, s2;
            
            for (char c: line) {
                if (currentIndex < middle) {
                    s1.insert(c); 
                }
                else {
                    s2.insert(c); 
                }
                currentIndex += 1;
            }

            std::set<char> pair;
            std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), std::inserter(pair, pair.begin()));
       
            char item = *pair.begin();

            if (islower(item)) {
                result += item - 96;
            }
            else {
                result += item - 38;
            }
        }
        myFile.close();
    }
    std::cout << "part 1: " << result << std::endl;
}