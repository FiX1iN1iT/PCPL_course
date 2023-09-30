//
//  Calculation.swift
//  Biquadrate
//
//  Created by MacBook on 30.09.2023.
//

import Foundation

struct Calculation {
    
    // # Linear Equation Solver
    func linearSolve(a: Double, b: Double) -> [Double] {
        if a == 0 {
            return []
        }
        
        return [Double(-b/a)]
    }
    
    
    // # Quadratic Equation Solver
    func quadraticSolve(a: Double, b: Double, c: Double, threshold: Double = 0.0001) -> [Double] {
        if a == 0 { return linearSolve(a: b, b: c) }
        
        var roots = [Double]()
        
        var d = pow(b, 2) - 4*a*c
        
        // Check if discriminate is within the 0 threshold
        if -threshold < d && d < threshold { d = 0 }
        
        if d > 0 {
            let x_1 = Double((-b + sqrt(d))/(2*a))
            let x_2 = Double((-b - sqrt(d))/(2*a))
            roots = [x_1, x_2]
        } else if d == 0 {
            let x = Double(-b/(2*a))
            roots = [x, x]
        }
        
        return roots
    }


    // # Biquadratic Equation Solver
    func biquadrateSolve(_ a: Double, _ b: Double, _ c: Double) -> [Double] {
        var result = [Double]()
        let solutions = quadraticSolve(a: a, b: b, c: c)
        for root in solutions {
            if root > 0 {
                result.append(-root.squareRoot())
                result.append(root.squareRoot())
            } else if root == 0 {
                result.append(0)
            }
        }
        return result
    }
}
