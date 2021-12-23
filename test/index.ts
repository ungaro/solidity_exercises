import { expect } from "chai";
import { ethers } from "hardhat";

describe("Question", function () {
  it("Should return the correct calculations", async function () {
    const Question = await ethers.getContractFactory("Question");
    const question = await Question.deploy();
    await question.deployed();

    expect(await question.f(4)).to.equal("1375000000000000000");
    expect(await question.f(1000000000)).to.equal("20687500000000000000");
    expect(await question.f(121212)).to.equal("11687500000000000000");


  });
});


