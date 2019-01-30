# AgentBasedModeling

Sensitivity analysis:
Input variables:
- Agent level:
	- memory
	- strategy evaluation memory
	- number of strategies
	- positivity
	- "strategy category"
		- Prioritize Past vs Present
		- Single vs many
- Market level:
	- memory of all agents
	- percentage random agents

Output variables:
- Agent level:
	- profit
		- individual
		- average
		- of all agents
		- of non-random agents
	- number of matches
- Market level:
	- stability
		- variance / standard deviation

Experiments:
- Memory vs Profit (agent level)
- Strategy evaluation memory vs Profit (agent level)
- Memory vs Match number (agent level)
- Strategy evaluation memory vs Match number (agent level)
- Feed in real market data --> So how our market deviates
- Seed different markets to check how agents perform in them



Curent ideas and To-Dos:
Have a look at exponential growth
--> until match up work
-->  until strategies work
- several strategies
- select best (Maybe Westerhoff)
	- comparing older results
	- memory...
- price adjusted (Maybe Westerhoff as well)
- volatitlity clustering?
- strategies adapted for information arrival/speed of price adjustment
- influence of memory on market
- influence of market on strategy/memory (if some eovlution)
- check stability,, total sales, price change...


The stock market (El Farol = bar example)

Steps for the (artificial) stock market: 
1. Building the simplest version of the minority game - binary: yes/no 
  In every round the agents decides whether to buy or sell
  Class: Model: Time, List of agent, Whether agent wins/loses
  Class: Agent: Saves own score, History of own choices
2. Extend this to the agents: the amount of money they have
3. Connect buyer and seller (Order sale price list or randomize sale list and pick random?)
4. Estimation of the price --> sell or won't sell
  e.g. lowest sale price in previous round - won't sell
5. Strategies of the agents: ('hard part')
  e.g. fixed strategies (always being possitive/negative about the market)
  e.g. above amount of money: sell, below amount of money: buy
  e.g. Group of agents: Always overbuy, always oversell
  e.g. Group of agents: Negative buyers, positive sellers
6. Statistics: 
  e.g. min/max/average price --> based on this agent make new decision 
  e.g. Volumes/ how many units (amount of money)
7. Model Gini coefficient (measure of wealth inequality) 

Multiple ideas: 
- Introduce mutations
- Learning: Adapt neighbors --> number of strategies stays fixed --> random chance of adapting
- Reenforcement learning/Neural agent: copying strategy of other agents 
- Shill (happens with bitcoins) --> pump and dump
- El farol with coefficients - to decide the price (current price and difference of average of N last weeks) 
(Looking at own OR sharing strategies of agents: -force it- to copy strategy)  
- Netlogo: Social science --> Bidding market, El Farol, Minority game, Oil kartel hubnet

MIKE: Work backwards: What is the research question (possible experiments or hypothesis -- before you code)

Research questions:
- How much influence is needed to stirr the market?
- Are certain markets (many well-behaved, many crazy traders) more easily stirred?
- Is the market more stable with a heterogeneous or a homogeneous set of traders?
- Do traders with certain strategies prefer traders with certain other strategies?
- What is the best strategy for a trader?
- Which strategies will lead to a stable market?
