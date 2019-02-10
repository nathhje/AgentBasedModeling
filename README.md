# An Agent-Based Model of Stock Market Prices

Financial markets are of great importance in the world of trade, but due to the number of involved parties and the complexity of interactions, they can not be easily predicted. While no model can fully grasp such a complex system, an agent based model (ABM) is a good avenue to acquire some insights about the inner workings of the market. Based on the El Farol bar problem, an ABM was build to emulate the development of a stock price over time. After tweaking the system to show dynamics similar to a real market, the effect of different model components was investigated. It was shown that the market becomes more stable when many agents with a large memory are present, an individual trader can profit in such a market by having a shorter memory, and thereby adapt to current trends. Agents, displaying a random strategy when making there next offer, have been shown to be be relevant to keep the market from stalling. Paradoxically, however, increasing there number over a certain threshold will cover the effects of the non-random agents, and dampen market trends. Overall, while the ABM not grasp all the aspects and dynamics of a real stock market, it can still be used to gain some insights into the inner workings of one.

## Getting started
In order to start the model, the prerequisites are given. Besides that, an installing example shows how to run the 'main.py' file. 

### Prerequisites
To run the ABM simulation, you first need to install the following libraries: 
- numpy
- random
- math
- matplotlib
- SALib
- seaborn
 
 ### Installing 
 Moreover, after installing all the necessary libraries, you can run a development environment with the command window and typing 'python main.py' in the correct map. 
 
 ### Running the model
 To run the model regularly, refer to main.py. Other alternatives to running the model for experiments and analysis can be found in sensitivityanalysis.py, Rmain.py and verify.py.
 Supporting code files can be found in the helpers and classes directories.

### Running the interactive analysing tool
In order to create a dynamic graph of the output, go to the main directory and run the command "python -m SimpleHTTPServer 8000" in your terminal. Then open local "http://localhost:8000/" in your webbrowser. This will automatically open the index.html page and show the graph.

The graph has multiple colors: blue for the buyers, green for the sellers and oranges for traders who've had a match. Opaque dots represent the traders who have used a strategy. If clicked upon, information over the price and the agent appear, as well the information of other offer of the same trader over time. The index.html is not automatically updated whenever the users runs the model. To update the data, add "make_csv(modelA)" to the end of the main() function in main.py, run the main function, go to the browser and press ctrl+shift+R.
