//
//  QuickTests.swift
//  QuickTests
//
//  Created by MacBook on 01.10.2023.
//

import Quick
import Nimble
@testable import Biquadrate

class WorkingQuickTests: QuickSpec {
    
    override class func spec() {
    
        var a: Double!
        var b: Double!
        var c: Double!
        var calculation: Calculation!
    
        beforeEach {
            calculation = Calculation()
        }
    
        describe("Biquadrate equation") {
    
            it("zero roots") {
                a = 1
                b = 0
                c = 10
                expect(calculation.biquadrateSolve(a, b, c)).to(equal([]))
            }
    
            it("two roots") {
                a = 1
                b = 0
                c = -4
                expect(calculation.biquadrateSolve(a, b, c)).to(equal([-1.4142135623730951, 1.4142135623730951]))
            }
    
            it("three roots") {
                a = -4
                b = 16
                c = 0
                expect(calculation.biquadrateSolve(a, b, c)).to(equal([0.0, -2.0, 2.0]))
            }
    
            it("four roots") {
                a = 1
                b = -13
                c = 36
                expect(calculation.biquadrateSolve(a, b, c)).to(equal([-3.0, 3.0, -2.0, 2.0]))
            }
        }
    }
}
