//
//  CalculationTests.swift
//  BiquadrateTests
//
//  Created by MacBook on 30.09.2023.
//

import XCTest
@testable import Biquadrate

final class CalculationTests: XCTestCase {

    func testZeroRootsInBiqudrateEquation() {
        // Given (Arrange)
        let a: Double = 1
        let b: Double = 0
        let c: Double = 10
        let calculation = Calculation()
        
        // When (Act)
        let roots = calculation.biquadrateSolve(a, b, c)
        
        // Then (Assert)
        XCTAssertEqual(roots, [])
    }
    
    
    func testTwoRootsInBiqudrateEquation() {
        // Given (Arrange)
        let a: Double = 1
        let b: Double = 0
        let c: Double = -4
        let calculation = Calculation()
        
        // When (Act)
        let roots = calculation.biquadrateSolve(a, b, c)
        
        // Then (Assert)
        XCTAssertEqual(roots, [-1.4142135623730951, 1.4142135623730951])
    }
    
    
    func testThreeRootsInBiqudrateEquation() {
        // Given (Arrange)
        let a: Double = -4
        let b: Double = 16
        let c: Double = 0
        let calculation = Calculation()
        
        // When (Act)
        let roots = calculation.biquadrateSolve(a, b, c)
        
        // Then (Assert)
        XCTAssertEqual(roots, [0.0, -2.0, 2.0])
    }
    
    
    func testFourRootsInBiqudrateEquation() {
        // Given (Arrange)
        let a: Double = 1
        let b: Double = -13
        let c: Double = 36
        let calculation = Calculation()
        
        // When (Act)
        let roots = calculation.biquadrateSolve(a, b, c)
        
        // Then (Assert)
        XCTAssertEqual(roots, [-3.0, 3.0, -2.0, 2.0])
    }
}
