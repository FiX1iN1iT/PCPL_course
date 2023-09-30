import Foundation

extension String {
    subscript(index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

extension String {
    public func levenshtein(_ other: String) -> Int {
        guard self != other else {
            return 0
        }
        guard self.count != 0 else {
            return other.count
        }
        guard other.count != 0 else {
            return self.count
        }
        
        let line: [Int]  = Array(repeating: 0, count: other.count + 1)
        var matrix: [[Int]] = Array(repeating: line, count: self.count + 1)
        
        for i in 0...self.count {
            matrix[i][0] = i
        }
        
        for j in 0...other.count {
            matrix[0][j] = j
        }
        
        for j in 1...other.count {
            for i in 1...self.count {
                if self[i - 1] == other[j - 1] {
                    matrix[i][j] = matrix[i - 1][j - 1]
                } else {
                    let deletion = matrix[i - 1][j] + 1
                    let insertion = matrix[i][j - 1] + 1
                    let substitution = matrix[i - 1][j - 1] + 1
                    matrix[i][j] = min(min(deletion, insertion), substitution)
                }
            }
        }
        
        return matrix[self.count][other.count]
    }
}


// Usage
print("Input first word:")
var a = readLine()!
print("Input second word:")
var b = readLine()!
// Levenshtein distance calculation
print("Levenshtein distance =", a.levenshtein(b))

// ex: abc, adb (2)
