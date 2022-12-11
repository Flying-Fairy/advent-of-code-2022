#include <iostream>
#include <string>
#include <fstream>
#include <set>

int main() {

    std::fstream myFile;
    const int signalLength = 14;

    myFile.open("../inputs/input6.txt", std::ios::in);
    std::string line;
    
    while (std::getline(myFile, line)) {
        int start = 0, end = signalLength;
        for (auto i = 0; i < line.length(); i++) {
            std::string subString = line.substr(start, signalLength);
            std::set<char> signalSet(std::begin(subString), std::end(subString));
            
            if (signalSet.size() == signalLength) {
                std::cout << end << std::endl;
                break;
            }
            start += 1;
            end += 1;
        }
    }
    myFile.close();
}