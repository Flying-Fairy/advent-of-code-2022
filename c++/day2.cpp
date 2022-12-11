#include <iostream>
#include <map>
#include <fstream>
#include <string>

int main() {
    std::map<std::string, int> combinations;
    std::map<std::string, int> combinations2;
    // A: Rock, B: Paper, C: Scissors
    // X: Rock, Y: Paper, Z: Scissors 
    
    const int rock = 1, paper = 2, scissors = 3, win = 6, draw = 3, lose = 0;
    
    // rock
    combinations["A X"] = rock + draw, combinations["A Y"] = paper + win, combinations["A Z"] = scissors + lose;
    // paper
    combinations["B X"] = rock + lose, combinations["B Y"] = paper + draw, combinations["B Z"] = scissors + win;
    // scissors
    combinations["C X"] = rock + win, combinations["C Y"] = paper + lose, combinations["C Z"] = scissors + draw;

    // rock
    combinations2["A X"] = scissors + lose, combinations2["A Y"] = rock + draw, combinations2["A Z"] = paper + win;
    // paper
    combinations2["B X"] = rock + lose, combinations2["B Y"] = paper + draw, combinations2["B Z"] = scissors + win;
    // scissors
    combinations2["C X"] = paper + lose, combinations2["C Y"] = scissors + draw, combinations2["C Z"] = rock + win;

    std::fstream myFile;
    int totalScore = 0;
    int totalScore2 = 0;

    myFile.open("../inputs/input2.txt", std::ios::in);
    if (myFile.is_open()) {
        std::string line;
        while (std::getline(myFile, line)) {
            totalScore += combinations[line];
            totalScore2 += combinations2[line];
        }
        myFile.close();
    }
    std::cout << totalScore << std::endl;
    std::cout << totalScore2 << std::endl;
}
