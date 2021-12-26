# Solidity Exercises

1- Turn this python code into Solidity.

```python

import math

start=7
end=4


def f(ipt):
    opt = 0
    for i in range(start + end + 1):
        x_i = pow(2, start-i)
        ipt_i = math.exp(x_i)

        if (ipt >= ipt_i):
            ipt /= ipt_i
            opt += x_i

    return opt 



print("result: ",f(4))
-- result:  1.375
```

[Solution -> contracts/Question.sol](contracts/Question.sol)

[Deployed Contract (Ropsten)](https://ropsten.etherscan.io/address/0x0A553FAa97F011F72dBa798fA04A1C4F7bA16151#readContract)

```
Output with 18 precision
1375000000000000000 is 1.375
```


2- The Binomial tree algorithm

An optimal algorithm - O(1) memory space and O(n − a) running time

Turn this python code into Solidity.

```python
# Binomial tree algorithm using a single variable instead of
# a whole array and linear running time        
import numpy as np
import math
def optimalEuropean(S, X, r, sigma,
                            T, N, optionType):
    dt = T/N
    u = math.exp(sigma*math.sqrt(dt))
    d = 1/u
    disc = math.exp(-r*T)
    p = (math.exp(r*dt)-d)/(u-d)
    q = 1-p
    a = math.log(X/(S*(d**N)))/math.log(u/d)
    a = math.ceil(a)
    S = S * (u**a) * (d**(N-a))
    b = (math.factorial(N)/(math.factorial(N-a)*math.factorial(a))) \
    * (p**a) * (q**(N-a))
    C = disc * b * (S-X)
    for j in range(a+1,N+1):
        b = ((p*(N-j+1)) / (q*j)) * b
        S = S * (u/d)
        C = C + disc * b * (S-X)
return C
        
        
C = optimalEuropean(100,100,0.06,0.10,1,3,'C')
print(C)
-- 7.617083110621771
```

[WIP -> contracts/Question2.sol](contracts/Question2.sol)


```
No output yet
```


# Commands

```shell
yarn compile
yarn deploy
yarn test 
```

Don't forget to create your own .env file from provided example .env.example
# How to use this repo


Try running some of the following tasks:

```shell
npx hardhat accounts
npx hardhat compile
npx hardhat clean
npx hardhat test
npx hardhat node
npx hardhat help
REPORT_GAS=true npx hardhat test
npx hardhat coverage
npx hardhat run scripts/deploy.ts
TS_NODE_FILES=true npx ts-node scripts/deploy.ts
npx eslint '**/*.{js,ts}'
npx eslint '**/*.{js,ts}' --fix
npx prettier '**/*.{json,sol,md}' --check
npx prettier '**/*.{json,sol,md}' --write
npx solhint 'contracts/**/*.sol'
npx solhint 'contracts/**/*.sol' --fix
```

# Etherscan verification

To try out Etherscan verification, you first need to deploy a contract to an Ethereum network that's supported by Etherscan, such as Ropsten.

In this project, copy the .env.example file to a file named .env, and then edit it to fill in the details. Enter your Etherscan API key, your Ropsten node URL (eg from Alchemy), and the private key of the account which will send the deployment transaction. With a valid .env file in place, first deploy your contract:

```shell
hardhat run --network ropsten scripts/deploy.ts
```

Then, copy the deployment address and paste it in to replace `DEPLOYED_CONTRACT_ADDRESS` in this command:

```shell
npx hardhat verify --network ropsten DEPLOYED_CONTRACT_ADDRESS
```

# Performance optimizations

For faster runs of your tests and scripts, consider skipping ts-node's type checking by setting the environment variable `TS_NODE_TRANSPILE_ONLY` to `1` in hardhat's environment. For more details see [the documentation](https://hardhat.org/guides/typescript.html#performance-optimizations).
